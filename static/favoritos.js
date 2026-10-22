document.addEventListener("click", async (e) => {
    const btn = e.target.closest(".btn-favorito");
    if (!btn) return;

    btn.disabled = true;

    try {
        const resp = await fetch("/livro/favoritar", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                titulo: btn.dataset.titulo,
                imagem: btn.dataset.imagem
            })
        });

        if (!resp.ok) throw new Error("Falha na requisição");

        const data = await resp.json();

        btn.classList.toggle("ativo", data.favorito);
        btn.setAttribute("aria-pressed", data.favorito);

        if (!data.favorito && document.body.dataset.pagina === "perfil") {
            btn.closest(".card-livro").remove();
        }
    } catch (erro) {
        alert("Não foi possível atualizar seus favoritos. Tente novamente.");
    } finally {
        btn.disabled = false;
    }
});