import pandas as pd


def format_table(path_name, directory_name, sheet_name, header_list, join_columns, suffix_name):
    xcel = pd.read_excel(
         path_name,
         engine='openpyxl',
         sheet_name=sheet_name,
         header=header_list,
         index_col=[0, 1]
    )

    xcel = xcel.replace('-', 0)

    xcel.index = ['_'.join(x) for x in xcel.index]

    if join_columns:
        xcel.columns = [sheet_name + '.' + '_'.join(x) for x in xcel.columns]
    else:
        xcel.columns = [sheet_name + '.' + x for x in xcel.columns]

    xcel.to_excel(directory_name + sh_n + suffix_name)


path = 'Demanda - Escolas Urbanas LIMPO OK' + '.xlsx'    #nome do arquivo que você quer extrair
directory_name = 'demandas/'                                       #pasta para onde vão as tabelas extraídas
suffix_name = '.demanda.escolas_urbanas' + '.xlsx'         #sufixo do arquivo
sheets_normals = ['D31', 'D33C']                                                                  #lista das tabelas que possuem colunas de cabeçalho simples
sheets_column_join = ['D1', 'D1A1', 'D1B']                                                 #lista das tabelas que possuem colunas de cabeçalho compostas por 2 linhas

for sh_n in sheets_normals:
    format_table(path, directory_name, sh_n, [1], False, '.SIMPLECOLUMNS.' + suffix_name)

for sh_n in sheets_column_join:
    format_table(path, directory_name, sh_n, [1, 2], True, '.JOINCOLUMNS.' + suffix_name)

