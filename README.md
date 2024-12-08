# yt-dlp-mp3

Software que utiliza el paquete "yt_dlp" e integra "ffmpeg" para convertir a .mp3 los recursos obtenidos.

Para generar el ejecutable para cualquier usuario se utilizó el biblioteca "cx_Freeze". La misma integra la herramienta "ffmpeg" para que no haga falta tenerla instalada. El software está adjunto en este repositorio y se puede utilizar descomprimiendo el archivo "build.rar".


> [!Ejecutable]
> Comando para crear archivo ejecutable a partir del código y de la configuración establecida.

```
python build_setup.py build
```