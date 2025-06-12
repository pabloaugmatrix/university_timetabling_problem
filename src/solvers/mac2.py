import random


def mac2(aulas: dict):
    # inicializa o conjunto de dominios
    aulas_dominio = {aula: list(range(1,16)) for aula in aulas}
    # Inicializa a lista de adjacentes
    lista_adjacentes = {}
    for i in aulas:
        lista_adjacentes[i] = []
        for j in aulas:
            if i == j: # verificação para nao comparar a aula com ela mesma
                continue
            #se as aulas forem do mesmo curso e periodo, cria uma aresta
            if (aulas[i].get_curso() == aulas[j].get_curso()) and (aulas[i].get_periodo() == aulas[j].get_periodo()):
                lista_adjacentes[i].append(j)
                continue
            #se as aulas compartilharem o mesmo professor, cria uma aresta
            if set(aulas[i].get_professores()) & set(aulas[j].get_professores()):
                lista_adjacentes[i].append(j)
                continue

    while lista_adjacentes:
        aulas_validas = [aula for aula in aulas_dominio if aula in lista_adjacentes]
        aula_atual = min(aulas_validas, key=lambda x: len(aulas_dominio[x]))
        print(aula_atual)
        novo_domonio = aulas_dominio[aula_atual][:1]
        print(aulas_dominio[aula_atual])
        novo_domonio.append(aulas_dominio[aula_atual][-1])
        print(novo_domonio)

        aulas_dominio[aula_atual] = novo_domonio
        for adjacente in lista_adjacentes[aula_atual]:
            for i in aulas_dominio[aula_atual]:
                if i in aulas_dominio[adjacente]:
                    aulas_dominio[adjacente].remove(i)
                if len(aulas_dominio[adjacente]) == 0:
                    print("erro")
                    return None
            lista_adjacentes[adjacente].remove(aula_atual)
        del lista_adjacentes[aula_atual]
    return aulas_dominio