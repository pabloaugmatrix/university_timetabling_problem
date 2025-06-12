from pandas.core.interchange import dataframe
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape, portrait, A3
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, PageBreak
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import KeepTogether


def buscar_na_agenda(dia, horario, curso, aulas, solucao):
    if curso == 'OutrosCursos':
        return [aulas[i].get_disciplina() for i in solucao[dia][horario] if aulas[i].get_curso() == curso]
    return [f'{aulas[i].get_codigo()}' for i in solucao[dia][horario] if aulas[i].get_curso() == curso]

def alocar_horarios(solucao, aulas, curso):

    horarios = [
        ["07:00 - 07:55", ", ".join(buscar_na_agenda('segunda',1,curso, aulas, solucao)), ", ".join(buscar_na_agenda('terça',1,curso, aulas, solucao)),", ".join(buscar_na_agenda('quarta',1,curso, aulas, solucao)), ", ".join(buscar_na_agenda('quinta',1,curso, aulas, solucao)), ", ".join(buscar_na_agenda('sexta',1,curso, aulas, solucao)),],
        ["07:55 - 08:50", ", ".join(buscar_na_agenda('segunda',2,curso, aulas, solucao)), ", ".join(buscar_na_agenda('terça',2,curso, aulas, solucao)),", ".join(buscar_na_agenda('quarta',2,curso, aulas, solucao)), ", ".join(buscar_na_agenda('quinta',2,curso, aulas, solucao)), ", ".join(buscar_na_agenda('sexta',2,curso, aulas, solucao)),],
        ["08:50 - 09:45", ", ".join(buscar_na_agenda('segunda',3,curso, aulas, solucao)), ", ".join(buscar_na_agenda('terça',3,curso, aulas, solucao)),", ".join(buscar_na_agenda('quarta',3,curso, aulas, solucao)), ", ".join(buscar_na_agenda('quinta',3,curso, aulas, solucao)), ", ".join(buscar_na_agenda('sexta',3,curso, aulas, solucao)),],
        ["10:10 - 11:05", ", ".join(buscar_na_agenda('segunda',4,curso, aulas, solucao)), ", ".join(buscar_na_agenda('terça',4,curso, aulas, solucao)),", ".join(buscar_na_agenda('quarta',4,curso, aulas, solucao)), ", ".join(buscar_na_agenda('quinta',4,curso, aulas, solucao)), ", ".join(buscar_na_agenda('sexta',4,curso, aulas, solucao)),],
        ["11:05 - 12:00", ", ".join(buscar_na_agenda('segunda',5,curso, aulas, solucao)), ", ".join(buscar_na_agenda('terça',5,curso, aulas, solucao)),", ".join(buscar_na_agenda('quarta',5,curso, aulas, solucao)), ", ".join(buscar_na_agenda('quinta',5,curso, aulas, solucao)), ", ".join(buscar_na_agenda('sexta',5,curso, aulas, solucao)),],
        ["13:30 - 14:25", ", ".join(buscar_na_agenda('segunda',6,curso, aulas, solucao)), ", ".join(buscar_na_agenda('terça',6,curso, aulas, solucao)),", ".join(buscar_na_agenda('quarta',6,curso, aulas, solucao)), ", ".join(buscar_na_agenda('quinta',6,curso, aulas, solucao)), ", ".join(buscar_na_agenda('sexta',6,curso, aulas, solucao)),],
        ["14:25 - 15:20", ", ".join(buscar_na_agenda('segunda',7,curso, aulas, solucao)), ", ".join(buscar_na_agenda('terça',7,curso, aulas, solucao)),", ".join(buscar_na_agenda('quarta',7,curso, aulas, solucao)), ", ".join(buscar_na_agenda('quinta',7,curso, aulas, solucao)), ", ".join(buscar_na_agenda('sexta',7,curso, aulas, solucao)),],
        ["15:45 - 16:40", ", ".join(buscar_na_agenda('segunda',8,curso, aulas, solucao)), ", ".join(buscar_na_agenda('terça',8,curso, aulas, solucao)),", ".join(buscar_na_agenda('quarta',8,curso, aulas, solucao)), ", ".join(buscar_na_agenda('quinta',8,curso, aulas, solucao)), ", ".join(buscar_na_agenda('sexta',8,curso, aulas, solucao)),],
        ["16:40 - 17:35", ", ".join(buscar_na_agenda('segunda',9,curso, aulas, solucao)), ", ".join(buscar_na_agenda('terça',9,curso, aulas, solucao)),", ".join(buscar_na_agenda('quarta',9,curso, aulas, solucao)), ", ".join(buscar_na_agenda('quinta',9,curso, aulas, solucao)), ", ".join(buscar_na_agenda('sexta',9,curso, aulas, solucao)),],
        ["17:35 - 18:30", ", ".join(buscar_na_agenda('segunda',10,curso, aulas, solucao)), ", ".join(buscar_na_agenda('terça',10,curso, aulas, solucao)),", ".join(buscar_na_agenda('quarta',10,curso, aulas, solucao)), ", ".join(buscar_na_agenda('quinta',10,curso, aulas, solucao)), ", ".join(buscar_na_agenda('sexta',10,curso, aulas, solucao)),],
        ["19:00 - 19:55", ", ".join(buscar_na_agenda('segunda',11,curso, aulas, solucao)), ", ".join(buscar_na_agenda('terça',11,curso, aulas, solucao)),", ".join(buscar_na_agenda('quarta',11,curso, aulas, solucao)), ", ".join(buscar_na_agenda('quinta',11,curso, aulas, solucao)), ", ".join(buscar_na_agenda('sexta',11,curso, aulas, solucao)),],
        ["19:55 - 20:50", ", ".join(buscar_na_agenda('segunda',12,curso, aulas, solucao)), ", ".join(buscar_na_agenda('terça',12,curso, aulas, solucao)),", ".join(buscar_na_agenda('quarta',12,curso, aulas, solucao)), ", ".join(buscar_na_agenda('quinta',12,curso, aulas, solucao)), ", ".join(buscar_na_agenda('sexta',12,curso, aulas, solucao)),],
        ["21:00 - 21:55", ", ".join(buscar_na_agenda('segunda',13,curso, aulas, solucao)), ", ".join(buscar_na_agenda('terça',13,curso, aulas, solucao)),", ".join(buscar_na_agenda('quarta',13,curso, aulas, solucao)), ", ".join(buscar_na_agenda('quinta',13,curso, aulas, solucao)), ", ".join(buscar_na_agenda('sexta',13,curso, aulas, solucao)),],
        ["21:55 - 22:50", ", ".join(buscar_na_agenda('segunda',14,curso, aulas, solucao)), ", ".join(buscar_na_agenda('terça',14,curso, aulas, solucao)),", ".join(buscar_na_agenda('quarta',14,curso, aulas, solucao)), ", ".join(buscar_na_agenda('quinta',14,curso, aulas, solucao)), ", ".join(buscar_na_agenda('sexta',14,curso, aulas, solucao)),],
        ["22:50 - 23:40", ", ".join(buscar_na_agenda('segunda',15,curso, aulas, solucao)), ", ".join(buscar_na_agenda('terça',15,curso, aulas, solucao)),", ".join(buscar_na_agenda('quarta',15,curso, aulas, solucao)), ", ".join(buscar_na_agenda('quinta',15,curso, aulas, solucao)), ", ".join(buscar_na_agenda('sexta',15,curso, aulas, solucao)),],
    ]
    return horarios


def criar_pdf(semestre, solucao, aulas):

    cursos = ['CCO', 'SIN', 'OutrosCursos', 'Optativas', 'PósGraduação']

    horarios = []
    for curso in cursos:
        horarios.append(alocar_horarios(solucao, aulas, curso))

    # Dados da tabela: cabeçalho e horários
    dias = ["Hora", "Segunda", "Terça", "Quarta", "Quinta", "Sexta"]

    # Estilos para os títulos
    styles = getSampleStyleSheet()

    # Cria 4 tabelas com título
    tabelas = []
    for i in range(len(cursos)):
        titulo_texto = f"{cursos[i]} - {semestre}"
        titulo = Paragraph(titulo_texto, styles["Heading2"])

        data = [dias] + horarios[i]
        colWidths = [3 * cm] + [7 * cm] * 5
        tabela = Table(data, repeatRows=1, hAlign='CENTER', colWidths=colWidths)
        tabela.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightblue),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ]))

        bloco = KeepTogether([titulo, Spacer(1, 12), tabela])
        tabelas.append(bloco)


    # Criação do PDF
    doc = SimpleDocTemplate(f"data/output/{semestre} - horarios.pdf", pagesize=landscape(A3), leftMargin=6 * cm,
    rightMargin=6 * cm,)
    elements = []

    for tabela in tabelas:
        elements.append(tabela)
        elements.append(Spacer(1, 12))  # Espaço entre tabelas

    doc.build(elements)
