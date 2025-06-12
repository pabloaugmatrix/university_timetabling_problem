from src.aula.aula import Aula
from src.aula.aula_dict import create_aulas_dict
from src.data.criar_pdf import criar_pdf
from src.data.read_data import read_data
from src.model.grafo import grafo
from src.solvers.mac import mac
from src.solvers.mac2 import mac2
from src.solvers.mac3 import mac3

if __name__ == "__main__":
    path = "data/input/Cenário 5 -  1º Semestre.pdf"
    dataframe = read_data(path)
    aulas = create_aulas_dict(dataframe)
    grafo(aulas, "data/output/grafo_1º_Semestre.png")
    solucao = mac3(aulas)
    criar_pdf("1º_Semestre", solucao, aulas)
    path = "data/input/Cenário 5 -  2º Semestre.pdf"
    dataframe = read_data(path)
    aulas = create_aulas_dict(dataframe)
    grafo(aulas, "data/output/grafo_2º_Semestre.png")
    solucao = mac3(aulas)
    criar_pdf("2º_Semestre", solucao, aulas)