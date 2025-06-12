import igraph as ig
import matplotlib.pyplot as plt
from matplotlib.font_manager import font_scalings


def grafo(aulas_dict: dict, save_path):
    # Cria um grafo com suporte a múltiplas arestas
    g = ig.Graph(directed=False)

    # Adiciona vértices usando o código da aula como rótulo
    for aula_key in aulas_dict:
        aula = aulas_dict[aula_key]
        if(aula.get_curso() == 'CCO'):
            color = 'green'
        elif(aula.get_curso() == 'SIN'):
            color = 'orange'
        elif(aula.get_curso() == 'OutrosCursos'):
            color = 'yellow'
        elif(aula.get_curso() == 'Optativas'):
            color = 'skyblue'
        else:
            color = 'purple'
        g.add_vertex(name=aula.get_codigo(), aula_obj=aula, color=color )

    # cria as arestas
    for i in range(len(g.vs)):
        for j in range(len(g.vs)):
            if(i==j):
                continue
            aula_i = g.vs[i]["aula_obj"]
            aula_j = g.vs[j]["aula_obj"]

            professores_i = set(aula_i.get_professores())
            professores_j = set(aula_j.get_professores())

            professores_em_comum = professores_i & professores_j

            for prof in professores_em_comum:
                # Cria uma aresta para cada professor em comum
                g.add_edge(i, j, professor=prof, color='red')
            #cria aresta se curso e periodo em comum
            if (g.vs[i]["aula_obj"].get_curso() == g.vs[j]["aula_obj"].get_curso()) and (g.vs[i]["aula_obj"].get_periodo() == g.vs[j]["aula_obj"].get_periodo()):
                g.add_edge(i, j, curso="Curso", color='blue')
            #arestas para optativas do mesmo periodo das aulas de SIN e CCO
            if ((g.vs[i]["aula_obj"].get_curso() == 'Optativas' and (g.vs[j]["aula_obj"].get_curso() in ['CCO', 'SIN'])) or (g.vs[j]["aula_obj"].get_curso() == 'Optativas') and (g.vs[i]["aula_obj"].get_curso() in ['CCO', 'SIN'])) and (g.vs[i]["aula_obj"].get_periodo() == g.vs[j]["aula_obj"].get_periodo()):
                g.add_edge(i, j, curso="Curso", color='blue')


    # Plota o grafo
    layout = g.layout_circle()
    layout.scale(3.0)

    curved = [0.2] * len(g.es)
    ig.plot(
        g,
        target=save_path,
        layout=layout,
        vertex_color=g.vs["color"],
        vertex_label=g.vs["name"],
        vertex_size=60,
        edge_width=3,
        bbox=(1300, 1300),
        margin=50,
        edge_curved= curved,
    )

