import asyncio
from fastapi import FastAPI, Response, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from autoresearcher import literature_review
# Placeholder function for literature_review for fast testing
# async def literature_review(q: str):
#     return "answer to: " + q

app = FastAPI()

# List of allowed origins (you can replace these with your own domain names)
allowed_origins = [
    "*",
    "https://restfox.dev",  # Testing
    "http://localhost:3000",  # Local development
    "https://example.com",    # Production domain
]

# Add CORS middleware to the FastAPI application
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Placeholder class for BrowserError (replace with your implementation)
class BrowserError(Exception):
    pass

# Define a Pydantic model for the POST request body
# this should be for ALL tools + workflows
class QuestionModel(BaseModel):
    research_question: str

# this is purely for testing and memes
# return a text response @ get
# @app.get("/literature-review")
@app.get("/q/{q}")
async def get_literature_review(q: str):
    print('[GET] New Question:', q)
    try:
        if q is None:
           return "type a question after /q/type your question here "
        researcher = literature_review(q)
        return researcher
    except BrowserError as e:
        return {"error": str(e)}

# return a JSON response @ POST
# optionally return a streamed response
# Define the POST endpoint and accept the JSON request body
@app.post("/")
async def get_literature_review(request: QuestionModel):
    q = request.research_question
    print('[POST] New Question:', q)
    try:
        researcher = literature_review(q)
        return {"researcher": researcher}
    except BrowserError as e:
        return {"error": str(e)}

# to support plugins
@app.get("/.well-known/ai-plugin.json")
async def load_plugin(request: Request):
    host = request.headers["host"]
    try:
        with open("./.well-known/ai-plugin.json") as file:
            text = file.read()
    except FileNotFoundError:
        return Response(status_code=404, content="Not found")
    text = text.replace("PLUGIN_HOSTNAME", f"http://{host}")
    return Response(content=text, media_type="text/json")

@app.get("/openapi.yaml")
async def load_openapi(request: Request):
    host = request.headers["host"]
    try:
        with open("openapi.yaml") as file:
            text = file.read()
    except FileNotFoundError:
        return Response(status_code=404, content="Not found")
    text = text.replace("PLUGIN_HOSTNAME", f"http://{host}")
    return Response(content=text, media_type="text/yaml")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


