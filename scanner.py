import requests

def verificar_seguranca(url):
    if not url.startswith('http'):
        url = 'https://' + url
    
    print(f"\n--- ANALISANDO SEGURANÇA DE: {url} ---\n")
    
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers
        
        alertas = {
            "Content-Security-Policy": "Protege contra scripts maliciosos.",
            "Strict-Transport-Security": "Força o uso de HTTPS seguro.",
            "X-Content-Type-Options": "Impede farejamento de arquivos.",
            "X-Frame-Options": "Protege contra Clickjacking."
        }
        
        for h, desc in alertas.items():
            if h in headers:
                print(f"[OK] {h}: ATIVO")
            else:
                print(f"[!!] {h}: AUSENTE -> {desc}")
                
    except Exception as e:
        print(f"Erro ao conectar: {e}")

# ESTA É A LINHA QUE ESTAVA DANDO ERRO (NÃO MEXA):
if __name__ == "__main__":
    print("================================")
    print("   SCANNER RODANDO COM SUCESSO")
    print("================================")
    alvo = input("Digite o site (ex: google.com): ")
    verificar_seguranca(alvo)