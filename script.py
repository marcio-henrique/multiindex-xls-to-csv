import pandas as pd

path = 'uso_de_reds.xlsx'
sh_n = 'E3A'

xcel = pd.read_excel(
     path,
     engine='openpyxl',
     sheet_name=sh_n,
     header=[1, 2],
     index_col=[0, 1]
)
xcel = xcel.replace('-', 0)

with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
     print(xcel)

xcel.to_csv('testando.csv')
# sheets =
#
# print(sheets)
