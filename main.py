"""############################
### Desenvolvido por Gustavo Eli###"""
import pandas as pd
import streamlit as st


def gerar_planilha_com_cabecalho(produto, po, numeros_serie):
    # Gerar o nome do arquivo com o formato desejado
    output_file = f"NS-H3C-{po}-{produto}.csv"

    # Tratamento de dados: se o número de série tiver 20 caracteres, remove os dois primeiros
    def tratar_numero_serie(ns):
        if len(ns) == 20:
            return ns[2:]
        return ns

    # Linha inicial com os dados
    linha_inicial = [produto, tratar_numero_serie(numeros_serie[0]), po]

    # Lista para armazenar as novas linhas (a partir da segunda linha)
    novas_linhas = []
    for ns in numeros_serie:
        novas_linhas.append([produto, tratar_numero_serie(ns), po])

    # Incluir a linha inicial e as novas linhas
    df_final = pd.DataFrame([linha_inicial] + novas_linhas)

    # Salvar como um novo arquivo sem cabeçalho
    df_final.to_csv(output_file, index=False, sep=';', header=False)
    return output_file


# Interface Streamlit
st.title("Automação de Planilha para Numero de serie | :green[INTELBRAS]")

# Entrada de dados
produto = st.text_input("Digite o código do produto:")
po = st.text_input("Digite o número do PO:")
numeros_serie_raw = st.text_area(
    "Cole os números de série (um por linha):",
    help="Cole os números de série separados por quebra de linha."
)

# Botão para gerar a planilha
if st.button("Gerar Planilha"):
    if produto and po and numeros_serie_raw.strip():
        numeros_serie = [ns.strip() for ns in numeros_serie_raw.splitlines() if ns.strip()]

        if numeros_serie:
            output_file = gerar_planilha_com_cabecalho(produto, po, numeros_serie)
            with open(output_file, "rb") as f:
                st.download_button(
                    label="Baixar Planilha",
                    data=f,
                    file_name=output_file,
                    mime="text/csv"
                )
            st.success("Planilha gerada com sucesso!")
        else:
            st.error("Nenhum número de série válido foi encontrado.")
    else:
        st.error("Por favor, preencha todos os campos corretamente.")
