import pdfplumber
import pandas as pd

def read_data(path):
    with pdfplumber.open(path) as pdf:
        page = pdf.pages[0]
        table = page.extract_table()
        dataframe = pd.DataFrame(table[1:], columns=table[0])
        dataframe.columns = [
            'Curso',
            'PPC',
            'Periodo',
            'Codigo',
            'Disciplina',
            'CH',
            'Prof 1',
            'Prof 2',
            'Prof 3',
            'Prof 4',
            'Prof 5',
            'Prof 6',
            'Prof 7',
            'Prof 8',
            'Prof 9',
            'Prof 10',
            'Prof 11',
            'Prof 12',
            'Prof 13',
            'Prof 14',
            'Prof 15',
            'Prof 16',
            'Prof 17',
            'Prof 18'
        ]
    dataframe.drop(index=0, inplace=True)
    dataframe['Curso'] = dataframe['Curso'].ffill().fillna('CCO')
    dataframe.reset_index(drop=True, inplace=True)
    return dataframe
