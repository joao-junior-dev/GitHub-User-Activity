import requests
import argparse


class UsuarioGit:
    def __init__(self, nome):
        self.nome = nome

    def requisicao_get(self):
        url = f'https://api.github.com/users/{self.nome}/events'
        resposta = requests.get(url)

        if resposta.status_code == 200:
            return resposta.json()
        else:
            print(f"Erro: código {resposta.status_code}")
            return None

    def imprime_eventos(self):
        dados_api = self.requisicao_get()
        if not dados_api:
            return

        print("Output:")
        for evento in dados_api:
            tipo = evento["type"]
            repo = evento["repo"]["name"]

            if tipo == "PushEvent":
                commits = len(evento["payload"].get("commits", []))
                print(f"- Pushed {commits} commits to {repo}:\n...{evento["payload"]["commits"][0]['message']}")
                print("-" * 100)
            elif tipo == "IssuesEvent":
                action = evento["payload"].get("action", "updated")
                print(f"- {action.capitalize()} a new issue in {repo}")
                print("-" * 100)
            elif tipo == "WatchEvent":
                print(f"- Starred {repo}")
                print("-" * 100)
            elif tipo == "ForkEvent":
                print(f"- Forked {repo}")
                print("-" * 100)
            elif tipo == "CreateEvent":
                ref_type = evento["payload"].get("ref_type", "repository")
                print(f"- Created a new {ref_type} in {repo}")
                print("-" * 100)
            else:
                print(f"- {tipo} in {repo}")
                print("-" * 100)


def main():
    parser = argparse.ArgumentParser(
        description="Ver atividades recentes de um usuário do GitHub."
    )
    parser.add_argument(
        "usuario",
        help="Nome de usuário do GitHub (ex: joao-junior-dev)"
    )

    args = parser.parse_args()
    usuario = UsuarioGit(args.usuario)
    usuario.imprime_eventos()


if __name__ == "__main__":
    main()

