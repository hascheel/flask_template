# A Flask template with Bootstrap
 Flask GUI template for client-server apps. Ready to use to start a new project. Contains Bootstrap and jQuery.

## Info
Based on:
- https://code.visualstudio.com/docs/python/tutorial-flask
- https://github.com/monkeymademe/picamera2-WebUI-Lite

## Prerequisite

```shell
# create a directory
mkdir flask_template
cd flask_template

# create a Python virtual environment
python -m venv .venv

# install dependencies with pip
python -m pip install flask
```

If you experience Python package compilation errors or if some Python modules cannot be found then include global Python packages to your Python virtual environment.

Open: *pyvenv.cfg* in *.venv directory*

```shell
# in pyvenv.cfg change the following line from:
include-system-site-packages = false
# to
include-system-site-packages = true
```
