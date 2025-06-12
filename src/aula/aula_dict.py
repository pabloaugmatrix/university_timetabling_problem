from src.aula.aula import Aula


def create_aulas_dict(dataframe):
    aulas = {}
    for i in range(len(dataframe)):
        curso = dataframe.loc[i, "Curso"]
        ppc = dataframe.loc[i, "PPC"]
        periodo = dataframe.loc[i, "Periodo"]
        codigo = dataframe.loc[i, "Codigo"]
        disciplina = dataframe.loc[i, "Disciplina"]
        ch = dataframe.loc[i, "CH"]
        professores = []
        for j in range(18):
            j+=1
            if dataframe.loc[i, f"Prof {j}"] != "":
                professores.append(j)
        aula = Aula(curso, ppc, periodo, codigo, disciplina, ch, professores)
        aulas[i] = aula
    return aulas