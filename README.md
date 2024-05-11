# ig-scrapper

### Instalar la librería `instaloader`
```bash
pip install instaloader
```

### Ejecutar el script:
Al momento de ejecutar, declarar variables globales del sistema 
con el usuario y password de mi cuenta. (Es porque la api no funciona sin login)
```bash
export IG_USERNAME="mi_usuario_ig"
export IG_PASSWORD="mi_password_ig"

python3.10 scrapper.py
```

### Extraccion:
Se guarda un json en la carpeta data.

