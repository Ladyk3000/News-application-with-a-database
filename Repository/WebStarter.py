from fastapi import FastAPI
import uvicorn
from PySide6 import QtCore
from Repository.DatabaseUpdater import DataBaseUpdater

app = FastAPI()
class WebStarter(QtCore.QThread):
    patience = 0
    stress = 0
    def run(self) -> None:
        uvicorn.run(app, host='127.0.0.1', port= 8000)

@app.get("/upload/")
def read_item(patience: int = 0, stress: int = 0):
    WebStarter.patience = patience
    WebStarter.stress = stress
    db_updater = DataBaseUpdater()
    db_updater.update_data(WebStarter.stress, WebStarter.patience)
    return ('OK')

# http://127.0.0.1:8000/upload/?patience=0&stress=0
