import os
from yt_dlp import YoutubeDL

def descargar_audio(url):
    # Asegúrate de que el archivo 'ffmpeg.exe' esté en la carpeta './ffmpeg/'
    ffmpeg_path = os.path.join(os.getcwd(), 'ffmpeg', 'bin/ffmpeg.exe')

    opciones = {
        'format': 'bestaudio/best',  # Selecciona el mejor formato de audio disponible
        'outtmpl': '%(title)s.%(ext)s',  # Usa el título del video como nombre del archivo
        'extractaudio': True,  # Solo extrae el audio
        'noplaylist': True,  # Evita descargar listas de reproducción
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Usa ffmpeg para la conversión
            'preferredcodec': 'mp3',  # Convierte a mp3
            'preferredquality': '192',  # Calidad de 192 kbps
        }],
        'ffmpeg_location': ffmpeg_path,  # Ubicación local de ffmpeg
        'audioquality': 1,  # Mejor calidad de audio
        'verbose': True,  # Muestra información detallada
    }

    with YoutubeDL(opciones) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    url = input("Introduce la URL del video de YouTube: ")
    descargar_audio(url)
