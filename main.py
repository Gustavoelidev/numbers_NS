import streamlit as st
from services.planilha_service import gerar_planilha
from utils.file_utils import deletar_arquivo_se_existe

# Título do Aplicativo
st.title("NUMERO DE SERIE | :white_check_mark:")

# Entrada de Dados
produto = st.text_input("Digite o código do produto:")
po = st.text_input("Digite o número do PO:")
numeros_serie_raw = st.text_area(
    "Cole os números de série (um por linha):",
    help="Cole os números de série separados por quebra de linha."
)

# Botão para Gerar Planilha
if st.button("Gerar Planilha"):
    if produto and po and numeros_serie_raw.strip():
        # Tratamento dos números de série
        numeros_serie = [ns.strip() for ns in numeros_serie_raw.splitlines() if ns.strip()]

        if numeros_serie:
            try:
                # Geração da Planilha
                arquivo_gerado = gerar_planilha(produto, po, numeros_serie)

                # Botão de Download
                with open(arquivo_gerado, "rb") as f:
                    st.download_button(
                        label="Baixar Planilha",
                        data=f,
                        file_name=arquivo_gerado,
                        mime="text/csv"
                    )
                st.success("Planilha gerada com sucesso!")
            finally:
                # Limpeza do Arquivo
                deletar_arquivo_se_existe(arquivo_gerado)
        else:
            st.error("Nenhum número de série válido foi encontrado.")
    else:
        st.error("Por favor, preencha todos os campos corretamente.")
