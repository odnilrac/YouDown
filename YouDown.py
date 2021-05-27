#
# YouDown.py    Script para fazer downloads de áudio e vídeo do YouTube com base
#               na biblioteca pytube (https://pypi.org/project/pytube/), versão
#               10.8.2 ou superior. ATENÇÃO: Versão 10.8.1 apresenta erro 404!
#
#               Versão 1.0 - 26-05-2021 | odnilrac
#

from pathlib import Path
from pytube import YouTube
from tqdm import tqdm
import os, sys

# Limpar a tela com base no SO
os.system('cls' if os.name == 'nt' else 'clear')

# Salvar o diretório atual do script
diretorio = Path().absolute()

# Receber link do YouTube
link = input('Informe o link do video no YouTube ou tecle <ENTER> para sair: ')
link = (link.replace(' ',''))
if (link == ''): sys.exit(0)

# Aceitar apenas endereço do YouTube
formato1 = 'https://www.youtube.com/watch?v='   # Ex: https://www.youtube.com/watch?v=ilw-qmqZ5zY
formato2 = 'https://youtu.be/'                  # Ex: https://youtu.be/ilw-qmqZ5zY
if formato1 not in link:
    if formato2 not in link:
        print ('ERRO: O link informado não é válido!')
        sys.exit(0)

# Variáveis de tratamento com o endereço estando OK
path = diretorio
yurl = YouTube(link)

# Opções de download do YouTube
print('\n1- Download do vídeo no formato MP4')
print('2- Download do áudio no formato MP3')
opcao = int(input('Opção? '))

# Rotinas para o download de áudio ou vídeo do YouTube
if opcao == 1:
    print('\nBaixando o vídeo... aguarde!')
    for i in tqdm(range(100)):
        arq = yurl.streams.filter(file_extension='mp4').first().download(path)
    print('\nDownload concluído!')
elif opcao == 2:
    print('\nATENÇÃO: Caso exista um vídeo com o mesmo nome, ele será removido!!!')
    conf = input('Continuar execução? (S/N) ')
    if conf == 'S' or conf == 's':
        print('\nBaixando o áudio do vídeo... aguarde!')
        for i in tqdm(range(100)):
            arq = yurl.streams.filter(only_audio=True).first().download(path)
        print('\nDownload concluído!')
        base, ext = os.path.splitext(arq)
        novoarq = base + '.mp3'
        if os.path.isfile(novoarq):
            os.remove(arq)
            sys.exit(0)
        else:
            os.rename(arq, novoarq)
    elif conf == 'N' or conf == 'n':
        print('\nProcessamento cancelado!')
        sys.exit(0)
    else:
        print('\nERRO: Opção inválida, encerrando!')
        sys.exit(0)
else:
    print('\nERRO: Opção inválida!')
    sys.exit(0)
