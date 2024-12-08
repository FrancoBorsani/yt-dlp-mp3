from cx_Freeze import setup, Executable
import os

# Define la ubicación de ffmpeg.exe
ffmpeg_path = os.path.join(os.getcwd(), 'ffmpeg', 'bin/ffmpeg.exe')

# Configuración del ejecutable
executables = [Executable("yt-dlp-mp3.py")]

# Setup
setup(
    name="Descargador",
    version="1.0",
    description="Descargador de audio de YouTube en formato MP3",
    executables=executables,
    options={
        "build_exe": {
            "include_files": [(ffmpeg_path, "ffmpeg/bin/ffmpeg.exe")]  # Incluir ffmpeg en el ejecutable
        }
    }
)