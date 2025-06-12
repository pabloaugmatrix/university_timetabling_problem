from src.aula.aula_dict import create_aulas_dict
from src.data.criar_pdf import criar_pdf
from src.data.read_data import read_data
from src.model.grafo import grafo
from src.solvers.fowardChecking import foward_checking

if __name__ == "__main__":
    path = "data/input/Cenário 5 -  1º Semestre.pdf"
    dataframe = read_data(path)
    aulas = create_aulas_dict(dataframe)
    grafo(aulas, "data/output/grafo_1º_Semestre.png")
    solucao = foward_checking(aulas)
    if solucao != None:
        criar_pdf("1º Semestre", solucao, aulas)
    else:
        print(f"Não foi possivel constuir uma solução para {path}")

    path = "data/input/Cenário 5 -  2º Semestre.pdf"
    dataframe = read_data(path)
    aulas = create_aulas_dict(dataframe)
    grafo(aulas, "data/output/grafo_2º_Semestre.png")
    solucao = foward_checking(aulas)
    if solucao != None:
        criar_pdf("2º Semestre", solucao, aulas)
    else:
        print(f"Não foi possivel constuir uma solução para {path}")