import requests

def get_livros(pesquisa):
    url = "https://pricematch.dnltech.dev/api/products/search"

    try:
        response = requests.get(url,params={"produto":f"Livro {pesquisa}"}, timeout=10)
        response.raise_for_status()

        dados = response.json()

        livros = []
        for livro in dados:
            lojas= livro.get("loja", [])

            lojas = sorted(
                lojas, key=lambda loja: loja.get("price")
                if loja.get("price") is not None else float("inf")
            )

            livros.append({
                "titulo": livro.get("titulo"),
                "moeda": livro.get("moeda", "BRL"),
                "lojas": lojas
            })

        return livros

    except requests.RequestException as e:
        print(f"Erro ao consultar a API: {e}")
        return []

    # if():
    #     livros.append(livro)
    #
    # livros=[{
    #     "isbn": livro["key"].split("/")[2] if "key" in livro else None,
    #     "autor":livro["author_name"][0] if "author_name" in livro else None,
    #     "titulo":livro["title"] if "title" in livro else None,
    #     "anoPublicado":livro["first_publish_year"] if "first_publish_year" in livro else None,
    #     "linguagem":livro["language"] if "language" in livro else None,
    #     }for livro in response.json()["docs"]]
    # print(livros)
    # return livros


if(__name__ == "__main__"):
    pesquisa = input("Insira o nome do livro: ")
    resultadoLivro= get_livros(pesquisa)
    print(resultadoLivro)