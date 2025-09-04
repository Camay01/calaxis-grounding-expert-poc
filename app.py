from fastapi import FastAPI
from pydantic import BaseModel
import os
import httpx

app = FastAPI()

class Statement(BaseModel):
    statement: str

@app.post("/validate")
async def validate(statement: Statement):
    provider = os.getenv("PROVIDER", "none")
    api_key = os.getenv("OPENAI_API_KEY", None)
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    if provider == "openai" and api_key:
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                "https://api.openai.com/v1/chat/completions",
                headers={"Authorization": f"Bearer {api_key}"},
                json={
                    "model": model,
                    "messages": [
                        {"role": "system", "content": "You are a factual accuracy checker."},
                        {"role": "user", "content": f"Statement: {statement.statement}. Respond with JSON {{ 'verdict': one of Factually Correct/Incorrect/Uncertain, 'justification': short explanation }}."}
                    ],
                    "temperature": 0
                }
            )
            data = resp.json()
            return {
                "verdict": data.get("choices", [{}])[0].get("message", {}).get("content", "").strip(),
                "provider": provider,
                "model": model,
                "raw": data
            }

    return {
        "verdict": "Uncertain",
        "justification": "No LLM configured; returning Uncertain by default in PoC.",
        "provider": provider,
        "model": model,
        "raw": None
    }
