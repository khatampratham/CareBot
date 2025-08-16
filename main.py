from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime, timedelta

app = FastAPI(title="CareBot", version="0.1.0")

class Reminder(BaseModel):
    text: str
    minutes_from_now: int = 10

reminders = []

@app.post("/remind")
def remind(r: Reminder):
    due = datetime.utcnow() + timedelta(minutes=r.minutes_from_now)
    reminders.append({"text": r.text, "due": due.isoformat()})
    return {"scheduled": True, "due": due.isoformat()}

@app.get("/reminders")
def list_reminders():
    return {"reminders": reminders}

# Run: uvicorn app.main:app --reload --port 8010
