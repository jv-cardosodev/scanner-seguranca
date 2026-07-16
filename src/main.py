import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from utils.banner import mostrar_banner
from scanner import Scanner


def main():

    mostrar_banner()

    alvo = input(
        "\nDigite o alvo: "
    )

    scanner = Scanner(alvo)

    scanner.iniciar()


if __name__ == "__main__":
    main()