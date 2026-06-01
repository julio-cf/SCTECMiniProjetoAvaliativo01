def convert_for_category(dataframe, List_column):
    for column in List_column:
        dataframe[column] = dataframe[column].astype('category')