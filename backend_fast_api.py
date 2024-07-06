from fastapi import FastAPI, UploadFile, File
import uvicorn

app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    with open(f"uploaded_file/{file.filename}", "wb") as f:
        f.write(contents)
    return {"filename": file.filename}

if __name__ == "__main__":
    uvicorn.run("backend_fast_api:app", host="127.0.0.1", port=8000)