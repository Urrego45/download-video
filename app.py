from fastapi import FastAPI
from pydantic import BaseModel
from pytube import YouTube
import os
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

HTML_ADDRESS = "./public/templates/index.html"


app = FastAPI()


app.mount("/static", StaticFiles(directory="./public/templates"))


@app.get('/', response_class=HTMLResponse)
def get_template():

    return FileResponse(HTML_ADDRESS, status_code=200)


@app.post('/download/{url}')
def post_download(url: str):
    # data = {
    #     "url": url.url
    # }
    url = f'https://www.youtube.com/watch?v={url}'
    path = 'Downloads'

    video = YouTube(url)

    url_download = str(Path.home() / path)
    print(url_download)
    print(Path.home())

    video.streams.get_highest_resolution().download(output_path=os.path.join(url_download))

    return FileResponse(HTML_ADDRESS, status_code=200)

