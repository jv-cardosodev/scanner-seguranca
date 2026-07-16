from flask import Flask, render_template, request
import sys
import os

sys.path.append(
    os.path.dirname(__file__)
)

from scanner import Scanner


app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)


@app.route("/", methods=["GET", "POST"])
def index():

    resultado = None

    if request.method == "POST":

        alvo = request.form["alvo"]

        scanner = Scanner(alvo)

        scanner.iniciar()

        resultado = scanner.portas_abertas


    return render_template(
        "index.html",
        resultado=resultado
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )