import uvicorn
import os
import json
from fastapi import Body
from fastapi import FastAPI

app = FastAPI()

from MyPyTalks.PyTalk import GenerateScript, ExplainScript, SaveScriptFile,GetScript, ExecuteScript

@app.post("/api/run_command")
async def run_command(data: str = Body(...)):
    dataObj = json.loads(data)
    cmd = dataObj['command']
    processed = ExecuteScript(cmd)
    return {"response": processed}

@app.post("/api/user_command")
async def user_command(data: str = Body(...)):
    dataObj = json.loads(data)
    cmd = dataObj['command']
    script = GenerateScript(cmd)
    explain = ExplainScript(script)
    processed = explain
    return {"response": processed, "script": script}

@app.post("/api/get_recent_script")
async def user_command():
    processed = GetScript()
    return {"response": processed}

import MyPyTalks.Config as Config

def GetZipContent(file):
    return Config.ResourceManager.Get(file, "UI")

from fastapi import Request, Response
from mimetypes import guess_type

@app.get("/{filename:path}")
async def UI(request: Request, filename: str):
    import re
    if not bool(re.search('\.[^\./]{2,5}$', filename)): filename += "/MyPyTalks.html"

    if Config.UX_Internal:
        content = GetZipContent(filename)
        if content != None:            
            return Response(content, media_type = guess_type(filename)[0])
    else:
        filename = os.environ["UI"] + "/" + filename 
        if not os.path.isfile(filename): return Response(status_code=404)

        with open(filename,"rb") as f: content = f.read()

        content_type, _ = guess_type(filename)
        return Response(content, media_type=content_type)


def Main():
    uvicorn.run("MyPyTalks.UiChat:app", host="0.0.0.0", port= int(os.environ["UI_PORT"]))