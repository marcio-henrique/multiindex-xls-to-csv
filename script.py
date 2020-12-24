import pandas as pd
import numpy as np

path='uso_de_reds.xlsx'
sh_n='E3A'

xcel = pd.read_excel(
     path,
     engine='openpyxl',
     sheet_name=sh_n,
     header=[1, 2],
     index_col=[0, 1]
)

xcel = xcel.replace('-', 0)


xcel.columns = [ '_'.join(x) for x in xcel.columns ]

xcel.index = [ '_'.join(x) for x in xcel.index ]

xcel.to_excel('testando2.xlsx')
