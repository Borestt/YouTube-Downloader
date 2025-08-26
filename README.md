# YouTube Downloader

Vamos fazer um passo a passo extremamente detalhado de como baixar vídeos do YouTube
diretamente para seu computador usando menos de 15 linhas de código em Python!

**Caso preferir, apenas clone o repositório**

## Passo 1
Abra seu editor de código, geralmente é o Visual Studio Code e crie uma pasta onde hospedará seu projeto

## Passo 2
Crie um arquivo em Python *Exemplo*: **main.py**  
Crie uma pasta onde ficará salvo seus futuros vídeos *Exemplo* **videos**

## Passo 3
Abra um terminal no arquivo main.py e digite `pip install pytubefix`  
Aqui você irá instalar a biblioteca necessária para baixar os vídeos
>É necessário ter o [Python](https://www.python.org/downloads/) instalado antes de mais nada!

## Passo 4
Agora com tudo instalado e prestes a ser usado, use este código:

from pytubefix import YouTube  
from pytubefix.cli import on_progress  
from pathlib import Path

url = "" # Coloque a URL do vídeo entre as aspas duplas  
destino = Path("videos")  
destino.mkdir(exist_ok=True)

yt = YouTube(url, on_progress_callback=on_progress)  
print(f"Título: {yt.title}\nDuração: {yt.length}s")

yt.streams.get_highest_resolution().download(output_path=destino)  
print(f"Vídeo baixado em: {destino}")

## Passo 5
Tudo está pronto, basta executar o comando que o vídeo que você colocou ficará salvo na pasta videos que você criou! 

## ⚖️ Aviso legal

Respeite os Direitos Autorais e os Termos de Serviço do YouTube. Baixe apenas conteúdos de sua autoria, domínio público ou com permissão explícita do detentor dos direitos
