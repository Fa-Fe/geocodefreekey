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


def fazer_requisicao(local, key):
    import requests

    base = "https://geocode.googleapis.com/v4/geocode/address"
    url = base + '/' + local
    headers = {
        "X-Goog-Api-Key": key
    }
    
    try:

        response = requests.get(url, headers=headers, timeout=30)

        dados = response.json()

        if response.status_code != 200:
            print(f"Erro HTTP {response.status_code}: {dados}")

            if response.status_code == 429:
                return {"status":"Error", "Code":429}

            return {"status":"Error", "Code":response.status_code}

        return {"status":"Sucess","Code":200, "resposta": dados}

    except Exception as e:
        print(f"Erro na requisição para {local} | {e}")
        return {"status":"Error", "Code":response.status_code,"resposta": e}

import json
import os

def validar_arquivo(arch_output):
    """
    Impede de refazer requisições
    Verifica se o arquivo existe, cria se necessário
    e retorna os IDs já registrados.
    """

    os.makedirs(os.path.dirname(arch_output), exist_ok=True)

    if not os.path.exists(arch_output):
        open(arch_output, "w", encoding="utf-8").close()

    ids_processados = set()

    with open(arch_output, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            try:
                registro = json.loads(linha)
                ids_processados.add(registro["id"])

            except (json.JSONDecodeError, KeyError):
                continue

    return ids_processados