import os
import shutil

pasta_para_limpar = "."

tipos_arquivos = {
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
    "Instaladores": [".exe", ".msi"],
    "Compactados": [".zip", ".rar"]
}

print("Iniciando a limpeza da pasta...")

for arquivo in os.listdir(pasta_para_limpar):
    nome, extensao = os.path.splitext(arquivo)
    extensao = extensao.lower()

    # 4. Verificando em qual categoria o arquivo se encaixa
    for pasta_destino, extensoes_permitidas in tipos_arquivos.items():
        if extensao in extensoes_permitidas:

            # Cria a pasta se ela não existir
            if not os.path.exists(pasta_destino):
                os.makedirs(pasta_destino)

            # Move o arquivo para lá
            print(f"Movendo: {arquivo} -> {pasta_destino}")
            shutil.move(arquivo, os.path.join(pasta_destino, arquivo))

print("Tudo organizado!")
