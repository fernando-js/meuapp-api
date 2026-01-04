from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"ok": True, "msg": "rodando no windows → hetzner → easypanel"}
