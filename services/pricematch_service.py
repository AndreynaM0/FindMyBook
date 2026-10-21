from typing import Any
import requests

def get_livros(pesquisa):
    url = "https://pricematch.dnltech.dev/api/products/search"

    try:
        response = requests.get(url,params={"produto":pesquisa}, timeout=10)
        response.raise_for_status()

        dados = response.json()

        livros: list[Any] = []
        for livro in dados:
            lojas= livro.get("loja", [])

            lojas = sorted(
                lojas, key=lambda loja: loja.get("price")
                if loja.get("price") is not None else float("inf")
            )

            livros.append({
                "titulo": livro.get("titulo"),
                "moeda": livro.get("moeda", "BRL"),
                "imagem": livro.get("imagem"),
                "lojas": lojas,
                "preco_minimo": lojas[0].get("price") if lojas else None
            })

        return livros

    except requests.RequestException as e:
        print(f"Erro ao consultar a API: {e}")
        return []

if __name__ == "__main__":
    pesquisa = input("Insira o nome do livro: ")
    print(get_livros(pesquisa))