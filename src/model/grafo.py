import networkx as nx
import matplotlib.pyplot as plt

def grafo(aulas_dict: dict, save_path):
    # Cria um MultiGraph não direcionado
    G = nx.MultiGraph()

    # Adiciona os nós com atributos
    for aula_key in aulas_dict:
        aula = aulas_dict[aula_key]
        if aula.get_curso() == 'CCO':
            color = '#00FF00' #lima
        elif aula.get_curso() == 'SIN':
            color = 'orange'
        elif aula.get_curso() == 'OutrosCursos':
            color = 'yellow'
        elif aula.get_curso() == 'Optativas':
            color = '#00FFFF' # azul claro
        else:
            color = '#FF00FF' #fuchsia

        G.add_node(aula, color=color, aula_obj=aula)

    # Lista de códigos (nomes dos nós)
    nodes = list(G.nodes)
    num_restricoes_professores = 0
    num_restricoes_periodos = 0
    # Cria as arestas com base nas restrições
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):  # evita duplicação
            nome_i = nodes[i]
            nome_j = nodes[j]
            aula_i = G.nodes[nome_i]["aula_obj"]
            aula_j = G.nodes[nome_j]["aula_obj"]

            profs_i = set(aula_i.get_professores())
            profs_j = set(aula_j.get_professores())

            profs_em_comum = profs_i & profs_j

            for prof in profs_em_comum:
                G.add_edge(nome_i, nome_j, professor=prof, color='red')
                num_restricoes_professores += 1

            mesmo_curso_e_periodo = (
                aula_i.get_curso() == aula_j.get_curso() and
                aula_i.get_periodo() == aula_j.get_periodo()
            )

            if mesmo_curso_e_periodo:
                G.add_edge(nome_i, nome_j, curso="Curso", color='blue')
                num_restricoes_periodos += 1

            optativa_relacionada = (
                (aula_i.get_curso() == 'Optativas' and aula_j.get_curso() in ['CCO', 'SIN']) or
                (aula_j.get_curso() == 'Optativas' and aula_i.get_curso() in ['CCO', 'SIN'])
            ) and aula_i.get_periodo() == aula_j.get_periodo()

            if optativa_relacionada:
                G.add_edge(nome_i, nome_j, curso="Curso", color='blue')
                num_restricoes_periodos += 1

    print(f"A instancia referente ao {save_path[-15:-4]} possui um total de {G.number_of_nodes()} variveis e {G.number_of_edges()} conflitos locais.")
    print(f"{num_restricoes_periodos} conflitos relacionados aos periodos em comum.")
    print(f"{num_restricoes_professores} conflitos relacionados aos professores em comum.")

    plt.figure(figsize=(7, 7))
    fig = plt.gcf()
    fig.set_constrained_layout(True)

    pos = nx.circular_layout(G)
    node_colors = [G.nodes[n]['color'] for n in G.nodes]

    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=400)

    # labels mostrando o código da aula
    labels = {n: n.get_codigo() for n in G.nodes}

    nx.draw_networkx_labels(G, pos, labels=labels, font_size=4.5, font_weight='bold')

    red_edges = [(u, v, k) for u, v, k, d in G.edges(keys=True, data=True) if d.get('color') == 'red']
    blue_edges = [(u, v, k) for u, v, k, d in G.edges(keys=True, data=True) if d.get('color') == 'blue']

    nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='red', width=1, connectionstyle='arc3,rad=0.2')
    nx.draw_networkx_edges(G, pos, edgelist=blue_edges, edge_color='blue', width=1, connectionstyle='arc3,rad=0.2')

    plt.axis('off')
    plt.savefig(save_path, dpi=600)
    plt.clf()

