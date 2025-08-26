from pytubefix import YouTube
from pytubefix.cli import on_progress
from pathlib import Path

url = "" # Joga a URL do vídeo aqui
destino = Path("videos")
destino.mkdir(exist_ok=True)

yt = YouTube(url, on_progress_callback=on_progress)
print(f"Título: {yt.title}\nDuração: {yt.length}s")

yt.streams.get_highest_resolution().download(output_path=destino)
print(f"Vídeo baixado em: {destino}")