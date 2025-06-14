import random

from src.aula.aula import Aula

#Inicializa uma agenda de professores, usada para verificação de conflitos globais
def construir_agenda_professores():
    agenda = {
        prof: {dia: [0] * 15 for dia in ['segunda', 'terça', 'quarta', 'quinta', 'sexta']}
        for prof in range(1,19)
    }
    return agenda

# particiona aulas com mais de 3 creditos em duas aulas com as mesmas caracteristicas, como maneira de facilitar a distribuição
def particionar_aulas(aulas):
    aulas_temp = {}
    for aula in aulas:
        if aulas[aula].get_ch() > 3:
            novo_ch = int(aulas[aula].get_ch()/2)
            curso = aulas[aula].get_curso()
            pcc = aulas[aula].get_pcc()
            periodo = aulas[aula].get_periodo()
            codigo = aulas[aula].get_codigo()
            disciplina = aulas[aula].get_disciplina()
            professores = aulas[aula].get_professores()
            nova_aula = Aula(curso, pcc, periodo, codigo, disciplina, str(novo_ch), professores)
            nova_chave = len(aulas) + len(aulas_temp)
            aulas_temp[nova_chave] = nova_aula
            aulas[aula].set_ch(aulas[aula].get_ch() - novo_ch)
    aulas.update(aulas_temp)


# Traduz a solução final em uma agenda
def construir_agenda_aulas(solucao):
    agenda = {
        dia: {hora: [] for hora in range(1, 16)}
        for dia in ['segunda', 'terça', 'quarta', 'quinta', 'sexta']
    }
    for aula in solucao:
        for horario in solucao[aula]:
            if horario < 16:
                agenda['segunda'][horario].append(aula)
            elif horario > 15 and horario < 31:
                agenda['terça'][horario - 15].append(aula)
            elif horario > 30 and horario < 46:
                agenda['quarta'][horario - 30].append(aula)
            elif horario > 45 and horario < 61:
                agenda['quinta'][horario - 45].append(aula)
            else :
                agenda['sexta'][horario - 60].append(aula)
    return agenda

# aloca aula na agenda dos professores, como meio de facilitar a verificação dos limites de aulas consecutivas e aulas diarias
def alocar_aula_agenda_professores(agenda, horarios, professores):
    for professor in professores:
        for horario in horarios:
            if horario < 16:
                agenda[professor]['segunda'][horario-1] = 1
            elif horario > 15 and horario < 31:
                agenda[professor]['terça'][horario - 16] = 1
            elif horario > 30 and horario < 46:
                agenda[professor]['quarta'][horario - 31] = 1
            elif horario > 45 and horario < 61:
                agenda[professor]['quinta'][horario - 46] = 1
            else:
                agenda[professor]['sexta'][horario - 61] = 1

#Desaloca aulas da agenda dos professores quando ocorre um conflito qualquer
def desalocar_aula_agenda_professores(agenda, horarios, professores):
    for professor in professores:
        for horario in horarios:
            if horario < 16:
                agenda[professor]['segunda'][horario-1] = 0
            elif horario > 15 and horario < 31:
                agenda[professor]['terça'][horario - 16] = 0
            elif horario > 30 and horario < 46:
                agenda[professor]['quarta'][horario - 31] = 0
            elif horario > 45 and horario < 61:
                agenda[professor]['quinta'][horario - 46] = 0
            else:
                agenda[professor]['sexta'][horario - 61] = 0

#Verifica se um professor não esta dando mais de 6 aulas diarias
def conflito_max_aulas_diarias(agenda, horarios, professores):
    for professor in professores:
        for horario in horarios:
            if horario < 16:
                if sum(agenda[professor]['segunda']) > 6:
                    return True
            elif horario > 15 and horario < 31:
                if sum(agenda[professor]['terça']) > 6:
                    return True
            elif horario > 30 and horario < 46:
                if sum(agenda[professor]['quarta']) > 6:
                    return True
            elif horario > 45 and horario < 61:
                if sum(agenda[professor]['quinta']) > 6:
                    return True
            else:
                if sum(agenda[professor]['sexta']) > 6:
                    return True
    return False

#Verifica se o professor se o professor não esta dando mais de 4 aulas consecutivas no dia
def conflito_max_aulas_seguidas(agenda, horarios, professores):
    for professor in professores:
        for horario in horarios:
            if horario < 16:
                if '11111' in ''.join(map(str ,agenda[professor]['segunda'])):
                    return True
            elif horario > 15 and horario < 31:
                if '11111' in ''.join(map(str ,agenda[professor]['terça'])):
                    return True
            elif horario > 30 and horario < 46:
                if '11111' in ''.join(map(str ,agenda[professor]['quarta'])):
                    return True
            elif horario > 45 and horario < 61:
                if '11111' in ''.join(map(str ,agenda[professor]['quinta'])):
                    return True
            else:
                if '11111' in ''.join(map(str ,agenda[professor]['sexta'])):
                    return True
    return False

#verifica se uma aula não esta começando em um turno e acabando em outro
def conflito_turnos(horarios):
    for i in range(5,71,5):
        if f'{i}{i+1}' in ''.join(map(str, horarios)):
            return True
    return False

#verifica se um par de aulas não está sendo divido por um intervalo qualquer
def sao_consecutivos(horarios):
    if not horarios:
        return False
    return len(set(horarios)) == len(horarios) and max(horarios) - min(horarios) + 1 == len(horarios)

#verifica se as aulas estão a começar em horarios padrões para começo de aulas
def inicia_em_horario_padrao(horarios):
    horarios_padrao_par = [1,2,4,6,8,11,13,16,17,19,21,23,26,28,31,32,34,36,38, 41, 43, 46, 47, 49, 51, 53, 56, 58, 61, 62, 64, 66, 68, 71, 73]
    horarios_padrao_impar = [1,4,8,13,16,19,23,28,31,34,38, 43, 46, 49, 53, 58, 61, 64, 68, 73]
    if len(horarios) == 2:
        if horarios[0] in horarios_padrao_par:
            return True
    else:
        if horarios[0] in horarios_padrao_impar:
            return True
    return False

#verifica todas as restrições globais
def restricoes_globais(agenda, horarios, professores):
    return (conflito_max_aulas_seguidas(agenda, horarios, professores) or conflito_max_aulas_diarias(agenda, horarios, professores))

#verifica algumas caracteristicas desejáveis para a alocação da aula
def caracteristicas_desejaveis(horarios):
    return not(inicia_em_horario_padrao(horarios)) or not(sao_consecutivos(horarios)) or conflito_turnos(horarios) or aula_7_da_manha(horarios)

#aloca a aula na agenda temporaria usada para alguma verificação de caracteristicas desejaveis
def alocar_aula_agenda_temp(agenda, aula, aulas, horario):
    if horario < 16:
        agenda['segunda'].append(f'{aulas[aula].get_disciplina()}{aulas[aula].get_curso()}')
    elif horario > 15 and horario < 31:
        agenda['terça'].append(f'{aulas[aula].get_disciplina()}{aulas[aula].get_curso()}')
    elif horario > 30 and horario < 46:
        agenda['quarta'].append(f'{aulas[aula].get_disciplina()}{aulas[aula].get_curso()}')
    elif horario > 45 and horario < 61:
        agenda['quinta'].append(f'{aulas[aula].get_disciplina()}{aulas[aula].get_curso()}')
    else:
        agenda['sexta'].append(f'{aulas[aula].get_disciplina()}{aulas[aula].get_curso()}')

# verifica se uma mesma aula não está sendo ministrada em dois horairos difertentes no mesmo dia
def aula_se_repete_no_dia(agenda, aula, aulas, horario):
    if horario < 16:
        if f'{aulas[aula].get_disciplina()}{aulas[aula].get_curso()}' in agenda['segunda']:
            return True
    elif horario > 15 and horario < 31:
        if f'{aulas[aula].get_disciplina()}{aulas[aula].get_curso()}' in agenda['terça']:
            return True
    elif horario > 30 and horario < 46:
        if f'{aulas[aula].get_disciplina()}{aulas[aula].get_curso()}' in agenda['quarta']:
            return True
    elif horario > 45 and horario < 61:
        if f'{aulas[aula].get_disciplina()}{aulas[aula].get_curso()}' in agenda['quinta']:
            return True
    else:
        if f'{aulas[aula].get_disciplina()}{aulas[aula].get_curso()}' in agenda['sexta']:
            return True
    return False

# Verifica se a aula não está a começar as 7 da manhã
def aula_7_da_manha(horarios):
    if horarios[0] in [1,16, 31, 46, 61]:
        return True
    return False

#Tentiva de dar uma melhor distribuida nas aulas durante a semana
def alta_densidade_de_aulas_no_dia(agenda, horario):
    densidade = 24
    if horario < 16:
        if len(agenda['segunda'])>=densidade:
            return True
    elif horario > 15 and horario < 31:
        if len(agenda['terça'])>=densidade:
            return True
    elif horario > 30 and horario < 46:
        if len(agenda['quarta'])>=densidade:
            return True
    elif horario > 45 and horario < 61:
        if len(agenda['quinta'])>=densidade:
            return True
    else:
        if len(agenda['sexta'])>=densidade:
            return True
    return False

#Verifica se uma optativa de periodo X não está no mesmo horario que uma aula de SIN ou CCO no mesmo horario
def conflito_opt_cco_sin(aula_i, aula_j, aulas):
    curso_i = aulas[aula_i].get_curso()
    curso_j = aulas[aula_j].get_curso()
    if (curso_i in ['CCO', 'SIN']) or (curso_j in ['CCO', 'SIN']):
        if aulas[aula_i].get_periodo() == aulas[aula_j].get_periodo():
            return True
    return False


def foward_checking(aulas: dict):
    particionar_aulas(aulas) # particiona aulas com mais de 3 creditos em duas aulas com as mesmas caracteristicas, como maneira de facilitar a distribuição
    # inicializa o conjunto de dominios
    aulas_dominio = {aula: list(range(1,76)) for aula in aulas}
    # Inicializa a lista de adjacentes
    lista_adjacentes = {}
    #cria as arestas de conflito
    for i in aulas:
        lista_adjacentes[i] = []
        for j in aulas:
            if i == j: # verificação para nao comparar a aula com ela mesma
                continue
            #se as aulas forem do mesmo curso e periodo, cria uma aresta
            if ((aulas[i].get_curso() == aulas[j].get_curso()) and (aulas[i].get_periodo() == aulas[j].get_periodo())):
                lista_adjacentes[i].append(j)
                continue
            if aulas[i].get_curso() == 'Optativas' or aulas[j].get_curso() == 'Optativas': #esse trecho esta aqui para garantir que que optativas de periodo X tenham conflito com SIN ou CCO no mesmo periodo
                if conflito_opt_cco_sin(i, j, aulas):
                    lista_adjacentes[i].append(j)
                    continue
            #se as aulas compartilharem o mesmo professor, cria uma aresta
            if set(aulas[i].get_professores()) & set(aulas[j].get_professores()):
                lista_adjacentes[i].append(j)
                continue

    agenda_professores = construir_agenda_professores() #Inicializa uma agenda de professores, usada para verificação de conflitos globais

    agenda_temp_aulas = {
        dia: []
        for dia in ['segunda', 'terça', 'quarta', 'quinta', 'sexta']
    }

    #Dentro desse laço ocorre o algoritmo de arco consistencia
    backtracking_count = 0
    while lista_adjacentes:
        aulas_validas = [aula for aula in aulas_dominio if aula in lista_adjacentes]
        aula_atual = random.choice(aulas_validas)
        conflito = True
        shift = 0
        # Dentro desse laço ocorre a escolha de dominio para a Aula em análise no momento
        while conflito:
            backtracking = False
            if backtracking_count > 100: #Controle para que não entre em um loop infinito
                return None
            potencial_aulas_dominio = aulas_dominio[aula_atual][shift:aulas[aula_atual].get_ch()+shift]
            alocar_aula_agenda_professores(agenda_professores, potencial_aulas_dominio, aulas[aula_atual].get_professores())
            if caracteristicas_desejaveis(potencial_aulas_dominio) or restricoes_globais(agenda_professores, potencial_aulas_dominio, aulas[aula_atual].get_professores()) or aula_se_repete_no_dia(agenda_temp_aulas, aula_atual, aulas, potencial_aulas_dominio[0]) or alta_densidade_de_aulas_no_dia(agenda_temp_aulas, potencial_aulas_dominio[0]):
                desalocar_aula_agenda_professores(agenda_professores, potencial_aulas_dominio, aulas[aula_atual].get_professores())
                shift += 1
            else:
                conflito = False
        backup_dominio = aulas_dominio[aula_atual]
        aulas_dominio[aula_atual] = potencial_aulas_dominio
        #Dentro desse laço o dominio da aula atual é subtraido dos dominios de todos os seus adjacentes
        for adjacente in lista_adjacentes[aula_atual]:
            for i in aulas_dominio[aula_atual]:
                if i in aulas_dominio[adjacente]:
                    aulas_dominio[adjacente].remove(i)
                if len(aulas_dominio[adjacente]) < aulas[adjacente].get_ch():
                    print(f"Faltou horario disponiveis para {aulas[adjacente].get_disciplina()}")
                    print("Iniando processo de backtracking!!!")
                    backtracking = True
                    backtracking_count += 1
            if backtracking:
                break
            else:
                lista_adjacentes[adjacente].remove(aula_atual)
        # realiza o backtracking aqui
        if backtracking:
            for adjacente in lista_adjacentes[aula_atual]:
                for i in aulas_dominio[aula_atual]:
                    if i not in aulas_dominio[adjacente]:
                        aulas_dominio[adjacente].append(i)
                if aula_atual not in lista_adjacentes[adjacente]:
                    lista_adjacentes[adjacente].append(aula_atual)
            aulas_dominio[aula_atual] = backup_dominio
            continue
        else:
            del lista_adjacentes[aula_atual]
            alocar_aula_agenda_temp(agenda_temp_aulas, aula_atual, aulas, aulas_dominio[aula_atual][0])

    # Traduz a solução final em uma agenda    
    agenda_aulas = construir_agenda_aulas(aulas_dominio)

    return agenda_aulas
