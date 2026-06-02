import pandas as pd

# Converte colunas para o tipo categórico
def convert_for_category(dataframe, List_column):
    
    for column in List_column:
        dataframe[column] = dataframe[column].astype('category')

# Converte colunas de string para datetime no formato DD/MM/YYYY
def convert_datetime(df, column_name):
  
    if not datetime_ok(df, column_name):
        return "Formatação inválida"

    df[column_name] = pd.to_datetime(df[column_name], format='%d/%m/%Y', errors='coerce')
    
    return "Conversão bem-sucedida"

# Verificar se alguma string não está no formato DD/MM/AAAA
def datetime_ok(df, column_name):
    
    date_pattern = r"^\d{2}/\d{2}/\d{4}$"

    # Retorna True se todas as strings na coluna corresponderem ao padrão, caso contrário, retorna False
    return df[column_name].astype(str).str.contains(date_pattern, regex=True).all()