import os

def deletar_arquivo_se_existe(caminho_arquivo):
    """Deleta o arquivo se ele existir."""
    if os.path.exists(caminho_arquivo):
        os.remove(caminho_arquivo)
