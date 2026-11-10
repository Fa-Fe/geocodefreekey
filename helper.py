def addEnderecoCompleto(df):
    df['endereco_completo'] = (
    df['endereco'].astype(str) + '; ' +
    df['municipio'].astype(str) + '; ' +
    'Pará; Brasil'
)
    df['endereco_completo'] = df['endereco_completo'].str.replace("S/N", "", case=False, regex=False)
    df['endereco_completo'] = df['endereco_completo'].str.replace("S / N", "", case=False, regex=False)
    df['endereco_completo'] = df['endereco_completo'].str.replace("s/n", "", case=False, regex=False)
    df['endereco_completo'] = df['endereco_completo'].str.replace("s / n", "", case=False, regex=False)

    df['endereco_completo'] = df['endereco_completo'].str.replace("°", "", case=False, regex=False)
    
    return df

def replaceEnderecoCompletoText(df):
    df['endereco_completo'] = df['endereco_completo'].str.replace("S/N", "", case=False, regex=False)
    df['endereco_completo'] = df['endereco_completo'].str.replace("S / N", "", case=False, regex=False)
    df['endereco_completo'] = df['endereco_completo'].str.replace("s/n", "", case=False, regex=False)
    df['endereco_completo'] = df['endereco_completo'].str.replace("s / n", "", case=False, regex=False)

    df['endereco_completo'] = df['endereco_completo'].str.replace("°", "", case=False, regex=False)

    return df


def AjustaDF(df):
    df = addEnderecoCompleto(df)
    df = replaceEnderecoCompletoText(df)

    return df