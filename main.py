from pathlib import Path


def listar_notas(pasta):
    nomes = []

    for arquivo in pasta.glob("*.md"):
        nomes.append(arquivo.name)

    return nomes


def ler_notas(conteudo):
    notas = []

    for arquivo in conteudo("laboratorio/estudos.md"):
        return arquivo.read_text(encoding="utf-8")

    return conteudo


pasta = Path(__file__).resolve().parent / "laboratorio/estudos.md"
print(conteudo)
