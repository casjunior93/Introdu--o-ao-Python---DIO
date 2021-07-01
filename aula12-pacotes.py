#pip freeze - mostra pacotes instalados
#pip install <pacote>
import requests

def ret_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))

    print(response.status_code)
    print(response.text)
    print(type(response.text))#<class 'str'>
    dados_cep = response.json()
    print(dados_cep['localidade'])

def retorna_site(url):
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    ret_dados_cep('13995000')
    #response = retorna_site('https://casjunior93.github.io/')
    #print(response)
