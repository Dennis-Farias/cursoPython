import requests

def siteAcessível(url):
    try:
        response = requests.get(url)
        # Verificar o código de status da resposta
        if response.status_code == 200:
            print("\033[0;33mConsegui acessar o site Pudim com sucesso!\033[m")
    except requests.exceptions.RequestException as e:
        print("\033[0;31mO site Pudim não está acessível no momento.\033[m")

# Exemplo de uso
urlsite = "http://pudim.com.br/"
siteAcessível(urlsite)
