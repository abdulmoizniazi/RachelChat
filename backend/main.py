from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai
from functions.openai_requests import conver_audio_to_text

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:4174",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials= True,
    allow_methods= ["*"],
    allow_headers= ["*"]
)

@app.get('/health')
async def check_health():
    # print('good time is here!')
    return {"message": "2025 is the new start"}

@app.get("/post-audio-get/")
async def get_audio():
    audio_input = open("voice.mp3", "rb")
    message_decoded = conver_audio_to_text(audio_input)
    print(message_decoded)
    return "Done"


@app.post("/post-audio/")
async def post_audio(file: UploadFile = File(...)):
    pass