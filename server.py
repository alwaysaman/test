from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
import aiofiles

app = FastAPI()

@app.get('/')
def homepage():
    return 'welcome to k means cluster'

@app.post('/cluster')
def cluster(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        df = contents
        with open(file.filename, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    
    finally:
        file.file.close()

    # return {"message": f"Successfully uploaded {file.filename}"}
    async def iterfile():
       async with aiofiles.open(file.filename, 'rb') as f:
            while chunk := await f.read():
                yield chunk
    headers = {'Content-Disposition': 'attachment; filename='+file.filename}
    return StreamingResponse(iterfile(), headers=headers, media_type='application/x-tar')
