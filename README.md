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
git clone https://github.com/Camay01/calaxis-grounding-expert-poc.git
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
docker run --rm -p 8000:8000 --env-file .env grounding-expert

```

---

## 🔎 Usage Example

```bash
$response = Invoke-RestMethod -Uri "http://localhost:8000/validate" `
  -Method POST `
  -Headers @{"Content-Type"="application/json"} `
  -Body '{"statement":"The first person to walk on the moon was Neil Armstrong."}'

# Parse the inner JSON string
$verdict = $response.verdict | ConvertFrom-Json
$verdict

```

**Response:**
```json
verdict         justification
-------         -------------
Factually Correct  Neil Armstrong was indeed the first person to walk on the moon on July 20, 1969, during the Apollo 11 mission.

```

---

## 🛡️ Security Notes
- Do **not** commit your `.env` file with real API keys.
- Use `.env.example` for sharing config.

---

## 📜 License
MIT
