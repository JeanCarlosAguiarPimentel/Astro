from pathlib import Path

def listar_notas(pasta):
    nomes = []

    for arquivo in pasta.glob("*.md"):
        nomes.append(arquivo.name)

    return nomes

pasta = Path(__file__).resolve().parent / "laboratorio"
print(listar_notas(pasta))