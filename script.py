import pandas as pd

path = 'tic_educacao_urbanas_professores_2019_total.xlsx'

xcell = pd.ExcelFile(path)

sheets = xcell.sheet_names

print(sheets)
