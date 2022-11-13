# RouteWiseApp TF

## Instalación de anadonda

La recomendación es instalar miniconda descargando desde
[aquí](https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe)
e instalar con opciones por defecto

Si ya tiene instalado Anaconda, o prefiere usar Anaconda (versión más grande)
descargue de
[aquí](https://repo.anaconda.com/archive/Anaconda3-2021.05-Windows-x86_64.exe) e
instalar con opciones por defecto.

## Crear un entorno virtual

Cremos entorno virtual para alojar las dependencias de flask. Si usa anaconda
puede usar el explorador gráfico. A continuación mostramos los pasos para
instalar usando línea de comandos:

Primero abrimos `Anaconda Prompt` o `Anaconda Prompt (miniconda3)` y ejecutamos
los siguientes comandos:

```shell
conda update --all
conda create -n comple
conda activate comple
conda update --all
conda install pip
python -m pip install -U pip
python -m pip install Flask
```

Luego con nuestro editor o IDE de python favorito creamos un archivo llamado
`hello.py` y escribimos el siguiente programa:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

Grabamos el archivo en una carpeta de nuestra elección y luego, desde la línea
de comandos previamente abierta, nos dirigimos a dicha carpeta usando el comando
`cd`, por ejemplo `cd "c:\Users\AkiraToriyama\Mis Documentos\tf"`, si su carpeta
está en un disco distinto, primero ponga el nombre del disco y luego el comando
cd, por ejemplo `d:` y luego `cd d:\carpetita\carpetota\tf`.

Finalmente ponga el siguiente comando:

```shell
set FLASK_APP=hello.py
python -m flask run
```

## Setup actualizado

El [venv](https://docs.python.org/3/library/venv.html) módulo admite la creación de "entornos virtuales" livianos, cada uno con su propio conjunto independiente de paquetes de Python instalados en sus site directorios. Se recomienda el uso de entornos virtuales para proyectos de desarrollo de software que, por lo general, se derivan de un solo script de Python, y Python proporciona múltiples formas de crear y usar un entorno virtual.

Para usar venv en su terminal ejecute los siguientes comandos

```shell
py -m venv env
```
### Activar el entorno virtual

.\env\Scripts\activate

### Mira la lista de paquetes instalados en el entorno virtual

pip list

### Descargar las dependencias necesarias

```shell
py -m pip install --upgrade pip
pip install Flask
pip install perlin-noise  
```

### Setup para correr una aplicacion web usando Flask y Python3

```shell
cd "Your project path"
set FLASK_APP=tfapp
set FLASK_DEBUG=1

flask run
```

Comando para cambiar de puerto de ejecución
python -m flask run -p 5000
Ahora, le aparecera una URL con una IP local y un puerto, porjemplo
`http://127.0.0.1:5000`, copie y pegue esa URL en su navegador favorito.

## Nota Importante

Por ahora puede colocar su algoritmo, según se explicó en clase, en la función
peru1 de algorithm.py. Debe desempaquetar el archivo d.json.zip directamente en
la carpeta static/data y ejecutar la aplicación de manera normal, pero con:

```shell
set FLASK_APP=tfapp.py
python -m flask run
```

:D
