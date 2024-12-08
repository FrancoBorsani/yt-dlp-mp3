# yt-dlp-mp3

Software que utiliza el paquete "yt_dlp" e integra "ffmpeg" para convertir a .mp3 los recursos obtenidos.

Para generar el ejecutable para cualquier usuario se utilizó el biblioteca "cx_Freeze". La misma integra la herramienta "ffmpeg" para que no haga falta tenerla instalada.

> [!Important]
> Comando para crear archivo ejecutable a partir del código y de la configuración establecida.

```
python build_setup.py build
```

> [!Iibrerías]
> Paquetes utilizados para el desarrollo.

```
python -m pip install cx_Freeze

python -m pip install yt-dlp
```
