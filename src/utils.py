import pandas as pd

def change_map(df, column_name):
    marital_status_map = {
        1: "CASADO OU UNIÃO ESTÁVEL",
        2: "DIVORCIADO",
        3: "SEPARADO",
        4: "SOLTEIRO",
        5: "VIÚVO",
    }

    df[column_name] = df[column_name].map(marital_status_map)

# Converte colunas para o tipo categórico
def convert_category(dataframe, List_column):
    
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