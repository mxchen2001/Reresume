from fastapi import FastAPI, File, UploadFile, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from gpt import query_gpt, expansion
from parser import markdown_to_html, parse_pdf
import uvicorn

app = FastAPI()

# Serve the static files, assuming your HTML is in a folder named 'static'
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    # Serve the HTML page
    with open('static/index.html', 'r') as f:
        return f.read()

@app.post("/submit/", response_class=HTMLResponse)
async def handle_form(file: UploadFile = File(...), text: str = Form(...)):
    # Process the file and text here
    file_contents = await file.read()
    
    # Do something with the file contents and text
    resume_contents = parse_pdf(file_contents)
    keywords = expansion(text)
    print(keywords)
    
    prompt = f"""I want to apply for a {text} position format the following resume to fit the job description. Target these keywords {keywords} Remove irrelevant information. Return the response as a Markdown with styling.

{resume_contents}
"""
    response_text = query_gpt(prompt)    
    return markdown_to_html(response_text)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
