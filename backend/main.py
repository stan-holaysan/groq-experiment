from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
import os
from dotenv import load_dotenv
from typing import List, Optional
import logging

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Chat Application API", version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173", "http://127.0.0.1:3000", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Groq client
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    logger.warning("GROQ_API_KEY not found in environment variables")
    groq_client = None
else:
    groq_client = Groq(api_key=groq_api_key)

# Pydantic models
class ChatMessage(BaseModel):
    message: str
    timestamp: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    timestamp: str
    success: bool = True
    error: Optional[str] = None

class HealthResponse(BaseModel):
    status: str
    groq_configured: bool

@app.get("/", response_model=dict)
async def root():
    """Root endpoint"""
    return {"message": "Chat Application API", "status": "running"}

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        groq_configured=groq_client is not None
    )

@app.post("/chat", response_model=ChatResponse)
async def chat_with_groq(message: ChatMessage):
    """
    Send a message to Groq and get a response
    """
    try:
        if not groq_client:
            raise HTTPException(
                status_code=500, 
                detail="Groq API key not configured. Please set GROQ_API_KEY environment variable."
            )
        
        if not message.message.strip():
            raise HTTPException(status_code=400, detail="Message cannot be empty")
        
        logger.info(f"Received message: {message.message}")
        
        # Create chat completion with Groq
        chat_completion = groq_client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful and friendly AI assistant. Provide clear, concise, and helpful responses."
                },
                {
                    "role": "user",
                    "content": message.message
                }
            ],
            model="llama-3.3-70b-versatile",  # Using Llama 3 8B model
            temperature=0.7,
            max_tokens=512,
            top_p=1,
            stream=False
        )
        
        response_content = chat_completion.choices[0].message.content
        
        # Get current timestamp
        from datetime import datetime
        timestamp = datetime.now().isoformat()
        
        logger.info(f"Generated response: {response_content[:100]}...")
        
        return ChatResponse(
            response=response_content,
            timestamp=timestamp,
            success=True
        )
        
    except Exception as e:
        logger.error(f"Error in chat endpoint: {str(e)}")
        
        # Get current timestamp for error response
        from datetime import datetime
        timestamp = datetime.now().isoformat()
        
        return ChatResponse(
            response="I'm sorry, I encountered an error while processing your message. Please try again.",
            timestamp=timestamp,
            success=False,
            error=str(e)
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
