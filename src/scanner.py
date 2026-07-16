import socket
from datetime import datetime


class Scanner:

    def __init__(self, alvo):
        self.alvo = alvo
        self.portas_abertas = []


    def salvar_relatorio(self, ip):

        arquivo = "../reports/scan_report.txt"

        with open(arquivo, "w", encoding="utf-8") as relatorio:

            relatorio.write(
                "SCANNER SEGURANÇA v1.0\n"
            )

            relatorio.write(
                "============================\n\n"
            )

            relatorio.write(
                f"Alvo: {self.alvo}\n"
            )

            relatorio.write(
                f"IP: {ip}\n"
            )

            relatorio.write(
                f"Data: {datetime.now()}\n\n"
            )


            relatorio.write(
                "Portas abertas:\n"
            )


            for porta in self.portas_abertas:

                relatorio.write(
                    f"- Porta {porta}\n"
                )


    def iniciar(self):

        print("\n[+] Iniciando scanner...")
        print("[+] Alvo:", self.alvo)


        try:

            ip = socket.gethostbyname(
                self.alvo
            )


            print(
                "[+] IP encontrado:",
                ip
            )


            for porta in range(1, 101):

                conexao = socket.socket(
                    socket.AF_INET,
                    socket.SOCK_STREAM
                )

                conexao.settimeout(0.5)


                resultado = conexao.connect_ex(
                    (ip, porta)
                )


                if resultado == 0:

                    print(
                        f"[ABERTA] Porta {porta}"
                    )

                    self.portas_abertas.append(
                        porta
                    )


                conexao.close()


            self.salvar_relatorio(ip)


            print(
                "\n[+] Relatório salvo em reports/scan_report.txt"
            )


        except Exception as erro:

            print(
                "[ERRO]",
                erro
            )