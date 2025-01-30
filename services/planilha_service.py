import pandas as pd


def gerar_planilha(produto, po, numeros_serie):
    # Gerar o nome do arquivo com o formato desejado
    output_file = f"NS-H3C-{po}-{produto}.csv"

    # Tratamento de dados: se o número de série tiver 20 caracteres, remove os dois primeiros
    def tratar_numero_serie(ns):
        if len(ns) == 20:
            return ns[2:]
        return ns

    # Linha inicial com os dados
    linha_inicial = [po, produto, tratar_numero_serie(numeros_serie[0])]

    # Lista para armazenar as novas linhas (a partir da segunda linha)
    novas_linhas = []
    for ns in numeros_serie:
        novas_linhas.append([po, produto, tratar_numero_serie(numeros_serie[0])])

    # Incluir a linha inicial e as novas linhas
    df_final = pd.DataFrame([linha_inicial] + novas_linhas)

    # Salvar como um arquivo temporário
    df_final.to_csv(output_file, index=False, sep=';', header=False)
    return output_file
