from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from openai import OpenAI
from dotenv import load_dotenv
import aiosqlite


# Load environment variables
load_dotenv()
client = OpenAI()

# Initialize FastAPI app
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Function to search in database
async def search_knowledge_base(query):
    async with aiosqlite.connect("database.db") as db:
        cursor = await db.execute(
            "SELECT answer FROM knowledge WHERE LOWER(question) LIKE ?",
            (f"%{query.lower()}%",)
        )
        row = await cursor.fetchone()
        if row:
            return row[0]
    return None

# Route: Home page
@app.get("/", response_class=HTMLResponse)
async def get_chat(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Route: Chat interaction
@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_input = data.get("message")

    # First try to find an answer in the database
    answer = await search_knowledge_base(user_input)
    if answer:
        return {"reply": f"(From database)\n{answer}"}

    # If not found, ask OpenAI
    response = client.chat.completions.create(
        model="gpt-4o-mini-2024-07-18",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )

    reply = response.choices[0].message.content.strip()
    return {"reply": reply}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
