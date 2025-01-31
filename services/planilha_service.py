import pandas as pd


def gerar_planilha(produto, po, numeros_serie):
    # Gerar o nome do arquivo com o formato desejado
    output_file = f"NS-H3C-{po}-{produto}.csv"

    # Tratamento de dados: se o número de série tiver 20 caracteres, remove os dois primeiros
    def tratar_numero_serie(ns):
        return ns[2:] if len(ns) == 20 else ns

    # Criar a lista de dados com cabeçalhos
    dados = [[po, produto, tratar_numero_serie(ns)] for ns in numeros_serie]

    # Criar o DataFrame com cabeçalhos
    df_final = pd.DataFrame(dados, columns=["pedido_compra", "material", "numero_serie"])

    # Salvar o arquivo CSV
    df_final.to_csv(output_file, index=False, sep=';', header=True)

    return output_file

