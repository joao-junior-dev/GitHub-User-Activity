# Project: Github User Activity:
# Tasks:
# Criar uma classe que representará o usuário do github
# Criar uma função que irá buscar os eventos do usuario
# Criar um CLI para lidar com pedidos
import requests

class UsuarioGit:
    def __init__(self, nome):
        self.nome = nome

    def requisicao_get(self):
        url = f'https://api.github.com/users/{self.nome}/events'
        resposta = requests.get(url)

        if resposta.status_code == 200:
            return resposta.json()
        else:
            return resposta.status_code

    def imprime_eventos(self):
        dados_api = self.requisicao_get()
        if isinstance(dados_api, int):
            print("Erro:", dados_api)
            return

        for evento in dados_api:
            tipo = evento["type"]
            repo = evento["repo"]["name"]

            if tipo == "PushEvent":
                commits = len(evento["payload"]["commits"])
                print(f"- Pushed {commits} commits to {repo}")
            elif tipo == "IssuesEvent":
                action = evento["payload"]["action"]
                print(f"- {action.capitalize()} a new issue in {repo}")
            elif tipo == "WatchEvent":
                print(f"- Starred {repo}")
            elif tipo == "ForkEvent":
                print(f"- Forked {repo}")
            else:
                print(f"- {tipo} in {repo}")  # fallback para outros eventos

    def __str__(self):
        return self.nome


joao = UsuarioGit("joao-junior-dev")
joao.imprime_eventos()