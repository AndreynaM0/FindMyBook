import requests

def get_livros(pesquisa):
    url = f"https://openlibrary.org/search.json?q={pesquisa}"
    headers = {
        "User-Agent": "MyAppName/1.0 (myemail@example.com)"
    }
    response = requests.get(url, headers=headers)

    # livros = []
    # for livro in response.json()["docs"]:
        # if():
        #     livros.append(livro)

    livros=[{
        "isbn": livro["key"].split("/")[2] if "key" in livro else None,
        "autor":livro["author_name"][0] if "author_name" in livro else None,
        "titulo":livro["title"] if "title" in livro else None,
        "anoPublicado":livro["first_publish_year"] if "first_publish_year" in livro else None,
        "linguagem":livro["language"] if "language" in livro else None,
        }for livro in response.json()["docs"]]
    print(livros)
    return livros

if(__name__ == "__main__"):
    pesquisa = input("Insira o nome do livro: ")
    get_livros(pesquisa)