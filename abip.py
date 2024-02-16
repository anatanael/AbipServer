import pyautogui
import pystray
from flask import Flask, jsonify, request
from dotenv import load_dotenv
from threading import Thread
import pyclip
import os
import sys
from PIL import Image
import signal

IS_BUILD = hasattr(sys, "_MEIPASS")
DEFAULT_PORT_APP = 5002
TITLE_APP = "Abip Server"

app = Flask(__name__)


def getPathCurrent():
    pathCurrent = os.path.dirname(os.path.realpath(__file__))
    return pathCurrent


def loadEnv():
    if IS_BUILD:
        pathEnv = os.path.join(os.path.dirname(sys.executable), "abip.config")
    else:
        pathEnv = os.path.join(getPathCurrent(), ".env")
    load_dotenv(dotenv_path=pathEnv)


loadEnv()


def getIconPath():
    if IS_BUILD:
        return os.path.join(sys._MEIPASS, "assets", "tray.png")
    else:
        return os.path.join(getPathCurrent(), "assets", "tray.png")


def getPortApp():
    if os.getenv("PORT_APP") is not None:
        return int(os.getenv("PORT_APP"))
    else:
        return DEFAULT_PORT_APP


def run_flask():
    app.run(host="0.0.0.0", port=getPortApp(), use_reloader=False)


def on_exit():
    os.kill(os.getpid(), signal.SIGINT)


def getMenuApp():
    return (
        pystray.MenuItem("Porta: {}".format(getPortApp()), lambda icon, item: None),
        pystray.MenuItem("Encerrar", on_exit),
    )


@app.route("/barcode", methods=["POST"])
def barcode():
    try:
        barcode = request.json.get("barcode")
        pyclip.copy(barcode)
        pyautogui.typewrite(barcode)
        pyautogui.press("enter")
        return jsonify({"success": True})
    except Exception as _:
        return jsonify({"success": False})


if __name__ == "__main__":
    flask_thread = Thread(target=run_flask)
    flask_thread.start()

    menu = getMenuApp()
    iconApp = Image.open(getIconPath())
    icon = pystray.Icon(TITLE_APP, iconApp, TITLE_APP, menu)
    icon.run()
