from pydantic import BaseModel
from typing import Dict, Any, Optional
from clients import HttpClient

class PostResponse(BaseModel):
    json: Dict[str, Any]
    url: str

class HttpBinGetResponse(BaseModel):
    args: Dict[str, Any]
    headers: Dict[str, str]
    origin: str
    url: str

with HttpClient("http://localhost:8000", log=True) as client:
    data = client.get_json("/get", HttpBinGetResponse)
    if data:
        print(f"URL: {data.url}")
        print(f"User-Agent: {data.headers.get('User-Agent')}")