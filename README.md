# Vue3-FastAPI-Project

This is a Template Project for an SPA (Vuejs/Quasar) with Pythons FastAPI Library as the Backend.
You can however just replace the Frontend Folder with any type of Web App.
Just make sure to adjust the instructions in the Dockerfile and
configure the build to be saved in ```frontend/dist/spa```.

## Usage

### Frontend

Install Quasar with ```npm i -g @quasar/cli``` and follow then instructions in ```frontend/README.md```.

### Backend

Create a virtual environment and install the dependencies with ```pip install -r requirements.txt```.
Afterwards just run ```python main.py``` or ```uvicorn backend.main:app --reload```.

