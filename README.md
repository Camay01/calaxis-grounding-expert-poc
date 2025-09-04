# Calaxis Grounding Expert (PoC)

This is a proof-of-concept implementation of the **Grounding Expert**, a component of the Calaxis "Council of Judges".  
It validates factual accuracy of AI-generated statements using an LLM.

---

## 🚀 Features
- REST API with **FastAPI**
- Fact-checking via **OpenAI GPT models** (or Hugging Face, extendable)
- Dockerized for easy deployment

---

## 📦 Setup

### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/calaxis-grounding-expert-poc.git
cd calaxis-grounding-expert-poc
```

### 2. Configure environment variables
Copy `.env.example` to `.env` and add your OpenAI key:
```env
PROVIDER=openai
OPENAI_API_KEY=sk-xxxxxx
OPENAI_MODEL=gpt-4o-mini
```

### 3. Build & Run with Docker
```bash
docker build -t grounding-expert .
docker run --rm -p 8000:8000 --env-file .env grounding-expert
```

---

## 🔎 Usage Example

```bash
curl -X POST http://localhost:8000/validate   -H "Content-Type: application/json"   -d '{"statement":"The first person to walk on the moon was Neil Armstrong."}'
```

**Response:**
```json
{
  "verdict": "Factually Correct",
  "justification": "Neil Armstrong was the first person to walk on the moon during Apollo 11 in 1969.",
  "provider": "openai",
  "model": "gpt-4o-mini",
  "raw": {...}
}
```

---

## 🛡️ Security Notes
- Do **not** commit your `.env` file with real API keys.
- Use `.env.example` for sharing config.

---

## 📜 License
MIT
