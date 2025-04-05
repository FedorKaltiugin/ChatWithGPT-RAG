# ChatWithGPT + RAG 

A lightweight chatbot powered by OpenAI's GPT and enhanced with a local knowledge base (RAG-style).  
Built with **FastAPI**, **HTML/CSS/JS**.

> ⚡ Instantly answers questions from the built-in database, or falls back to GPT when needed.

---

## 🚀 Features

- 🔍 Answers questions using a local SQLite database
- 🧠 Uses GPT-4o-mini via OpenAI API if no match is found
- 💬 Minimalistic chat interface (HTML + JS)
- ⚙️ Easy to extend with vector search or embeddings later
- 🗃️ Clean architecture — separate logic for DB and GPT

---

## 🛠️ How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Add your OpenAI API key
Create a `.env` file in the root of the project:
```
OPENAI_API_KEY=your_openai_key_here
```

### 3. Run the app
```bash
python main.py
```

Then open your browser and go to:  
http://127.0.0.1:8000

---

## 📌 Example Q&A in DB
These are real questions stored in the local database (`database.db`):

**Give me a tip about the Forth Bridge.**  
→ "The Forth Bridge is an outstanding example of engineering..."

**Add 34,957 and 70,764.**  
→ "The sum of 34,957 and 70,764 is 105,721."

**Do you play chess? My king is on K1 and I have no other pieces. Your king is on K6 and you have a rook on R1. It's your move. What do you do?**  
→ "Yes, I play chess. I would play R1–R2+ to check your king..."
