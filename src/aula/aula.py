import re

class Aula:
    def __init__(self,curso, pcc, periodo, codigo, disciplina, ch, professores: list):
        self.__curso = ''.join(re.findall(r'[^\W\d_]', curso, flags=re.UNICODE))#nome do curso
        self.__pcc = pcc #ano do projeto pedagogico
        self.__periodo = periodo #periodo sugerido para cursar
        self.__codigo = codigo #codigo da disciplina
        self.__disciplina = disciplina #nome da disciplina
        self.__ch = int(re.search('[0-9]',ch).group()) #carga horaria da disciplina
        self.__professores = professores #lista de professores escalados para lecionar

    def get_curso(self):
        return self.__curso

    def get_pcc(self):
        return self.__pcc

    def get_periodo(self):
        return self.__periodo

    def get_codigo(self):
        return self.__codigo

    def get_disciplina(self):
        return self.__disciplina

    def get_ch(self):
        return self.__ch

    def get_professores(self):
        return self.__professores

    def set_ch(self, ch):
        self.__ch = ch

    def __str__(self):
        return f'{self.__curso} - {self.__pcc} - {self.__periodo} - {self.__codigo} - {self.__disciplina} - {self.__ch} - {self.__professores}'
