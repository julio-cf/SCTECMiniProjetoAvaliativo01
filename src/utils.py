import pandas as pd

# Converte colunas para o tipo categórico
def convert_for_category(dataframe, List_column):
    
    for column in List_column:
        dataframe[column] = dataframe[column].astype('category')

# Converte colunas de string para datetime no formato DD/MM/YYYY
def convert_datetime(df, column_name):
  
    df[column_name] = pd.to_datetime(df[column_name], format='%d/%m/%Y', errors='coerce')

# Verificar se alguma string não está no formato DD/MM/AAAA
def check_date_format(df, column_name):
    
    date_pattern = r"^\d{2}/\d{2}/\d{4}$"

    # Listar valores que não correspondem ao padrão de data
    is_valid = df[column_name].astype(str).str.contains(date_pattern, regex=True)
    unformated_date = df.loc[~is_valid, column_name].tolist()

    return unformated_date