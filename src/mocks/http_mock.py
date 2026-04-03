from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.post("/payment")
async def payment(amount: float, user_id: int):
    # Имитируем задержку в 100 мс
    import time
    time.sleep(0.1)

    return {"status": "ok", "transaction_id": 12345}


@app.get("/health")
async def health():
    return {"status": "alive"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)