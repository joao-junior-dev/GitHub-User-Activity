# Project: Github User Activity:
# Tasks:
# Criar uma classe que representará o usuário do github
# Criar uma função que irá buscar os eventos do usuario
# Criar um CLI para lidar com pedidos
import requests
import json

class UsuarioGit():
    def __init__(self, nome):
        self.nome = nome

    def requisicao_get(self):
        resposta = requests.get(f'https://api.github.com/users/{self.nome}/events')

        if resposta.status_code == 200:
            return resposta.json()
        else:
            return resposta.status_code

    def imprime_eventos(self):
        dados_api = self.requisicao_get()
        if type(dados_api) is not int:
            for i in range(len(dados_api)):
                print(dados_api[i])
        else:
            print(dados_api)

    def __str__(self):
        print(str(self.nome))

joao = UsuarioGit('joao-junior-dev')
joao.imprime_eventos()
