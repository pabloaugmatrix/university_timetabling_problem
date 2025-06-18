import random
import sys

from src.aula.aula_dict import create_aulas_dict
from src.data.criar_pdf import criar_pdf
from src.data.read_data import read_data
from src.model.grafo import grafo
from src.solvers.fowardChecking import foward_checking

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Uso: python3 -m src.main <nome do arquivo> [seed]')
        exit(1)
    filename = sys.argv[1]
    if len(sys.argv) == 3:
        seed = int(sys.argv[2])
        random.seed(seed)
        print(f"Seed usada: {seed}")
    print(f"Arquivo: {filename}")
    instancia = sys.argv[1]
    path = f"data/input/{instancia}"
    dataframe = read_data(path)
    aulas = create_aulas_dict(dataframe)
    # grafo(aulas, f"data/output/Grafo {instancia[12:-4]}.png") # deixar comentado quando for realizar o benchmark
    solucao = foward_checking(aulas)
    if solucao != None:
        criar_pdf(f"{instancia[12:-4]}", solucao, aulas)
    else:
        print(f"Não foi possivel constuir uma solução para {path}")
