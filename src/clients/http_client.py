import httpx
from typing import Optional, Dict
from src.utils.logger import setup_logger
import time
from typing import TypeVar, Type, Optional
from src.models import User


class HttpClient:
    def __init__(self, base_url: str, timeout: int = 30, log: bool = False):
        self.base_url = base_url.rstrip('/')
        self.client = httpx.Client(timeout=timeout)
        self.log = log
        if self.log:
            self.logger = setup_logger()
        else:
            self.logger = None


    def _url(self, path: str) -> str:
        return f"{self.base_url}/{path.lstrip('/')}"

    def get(self, path: str, params: Optional[Dict] = None, headers: Optional[Dict[str, str]] = None) -> httpx.Response:
        url = self._url(path)
        if self.log:
            self.logger.info(f"Request: GET {url}")

        start = time.time()
        response = self.client.get(url, headers=headers, params=params)
        elapsed = time.time() - start

        if self.log:
            self.logger.info(f"Response: {response.status_code} ({elapsed:.3f}s)")
        return response

    def post(self, path: str, json: Optional[Dict] = None, headers: Optional[Dict[str, str]] = None) -> httpx.Response:
        url = self._url(path)
        if self.log:
            self.logger.info(f"Request: POST {url}")
        start = time.time()
        response = self.client.post(url, headers=headers, json=json)
        elapsed = time.time() - start

        if self.log:
            self.logger.info(f"Response: {response.status_code} ({elapsed:.3f}s)")
        return response

    def put(self, path: str, json: Optional[Dict] = None , headers: Optional[Dict[str, str]] = None) -> httpx.Response:
        url = self._url(path)
        if self.log:
            self.logger.info(f"Request: PUT {url}")
        start = time.time()
        response = self.client.put(url, headers=headers, json=json)
        elapsed = time.time() - start

        if self.log:
            self.logger.info(f"Response: {response.status_code} ({elapsed:.3f}s)")
        return response

    def patch(self, path: str, json, headers: Optional[Dict[str, str]] = None) -> httpx.Response:
        url = self._url(path)
        if self.log:
            self.logger.info(f"Request: PATCH {url}")
        start = time.time()
        response = self.client.patch(url, json=json, headers=headers)
        elapsed = time.time() - start

        if self.log:
            self.logger.info(f"Response: {response.status_code} ({elapsed:.3f}s)")
        return response

    def delete(self, path: str, headers: Optional[Dict[str, str]] = None) -> httpx.Response:
        url = self._url(path)
        if self.log:
            self.logger.info(f"Request: DELETE {url}")
        start = time.time()
        response = self.client.delete(url, headers=headers)
        elapsed = time.time() - start

        if self.log:
            self.logger.info(f"Response: {response.status_code} ({elapsed:.3f}s)")
        return response

    T = TypeVar('T')

    def get_json(self, path: str, response_model: Type[T], params: Optional[Dict] = None) -> Optional[T]:
        """GET запрос с автоматической валидацией ответа через Pydantic"""
        response = self.get(path, params=params)

        if response.status_code != 200:
            if self.log:
                self.logger.error(f"Unexpected status: {response.status_code}")
            return None

        try:
            return response_model(**response.json())
        except Exception as e:
            if self.log:
                self.logger.error(f"Validation failed: {e}")
            return None

    def close(self):
        self.client.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()