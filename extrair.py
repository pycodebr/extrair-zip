from zipfile import ZipFile

# Caminho do seu arquivo .zip #
filePath = 'myfile.zip'

# Abre o arquivo em modo de leitura para extrair #
with ZipFile(filePath, 'r') as zip:
    zip.printdir()

    # Extrai os arquivos #
    zip.extractall()