# Файл, где живет Flask. Точка входа в интернет
from flask import Flask
from service import service

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def hello():
    return "Hello"

@app.route("/all_materials", methods = ["GET"])
def get_all_materials():
    all_materials_db = service.get_all_materials()
    return all_materials_db

if __name__ == "__main__":
    app.run(debug = True, port = 5000)