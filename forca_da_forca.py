import random
from os import system
import time

palavras = {
    'Amendoim':{
        'dica': 'Alimento'
      },
    'Esfirra':{
        'dica': 'Alimento'
    },
    'Xicara':{
        'dica': 'Objeto'
    },
    'Heterossexual':{
        'dica': 'Aquele que gosta do oposto'
    },
    'Magenta':{
        'dica': 'Cor'
    },
    'Paralelepipedo':{
        'dica': 'Forma Geometrica'
    },
    'Pneumonia':{
        'dica': 'Doença'
    },
    'Submarino':{
        'dica': 'Meio de Transporte'
    },
    'Otorrinolaringologista':{
        'dica': 'Profissao'
    },
    'Reporter':{
        'dica': 'Profissao'
    },
    'Basquete':{
        'dica': 'Esporte'
    },
    'Eloquencia':{
        'dica': 'Capacidade de Argumentacao'
    },
    'Asterisco':{
        'dica': 'Caractere Especial'
    },
    'Umbigo':{
        'dica': 'Parte do Corpo'
    },
    'Chuveiro':{
        'dica': 'Eletrodomestico'
    },
    'Coelho':{
        'dica': 'Animal'
    },
    'Coracao':{
        'dica': 'Parte do Corpo'
    },
    'Unha':{
        'dica': 'Parte do Corpo'
    },
    'Excecao':{
        'dica': 'Fora da Regra'
    }, 
    'Capricornio':{
        'dica': 'Signo'
    },
    'Determinada':{
        'dica': 'Qualidade'
    },
    'Sincera':{
        'dica': 'Qualidade'
    },
    'Extrovertido':{
        'dica': 'Qualidade'
    },
    'Pacoca':{
        'dica': 'Alimento'
    },
    'Baco':{
        'dica': 'Parte do Corpo'
    },
    'Esfincter':{
        'dica': 'Parte do Corpo'
    },
    'Juiz':{
        'dica': 'Profissao'
    },
    'Cineasta':{
        'dica': 'Profissao'
    },
    'Biologo':{
        'dica': 'Profissao'
    },
    'Geladeira':{
        'dica': 'Eletrodomestico'
    },
    'Caqui':{
        'dica': 'Alimento'
    },
    'Kiwi':{
        'dica': 'Alimento'
    },
    'Moqueca':{
        'dica': 'Alimento'
    },
    'Cachecol':{
        'dica': 'Vestuario'
    },
    'Meia':{
        'dica': 'Vestuario'
    },
    'Coturno':{
        'dica': 'Calcado'
    },
    'Sandalia':{
        'dica': 'Calcado'
    }
}
lista = []
def listaPalavras(): 
  global lista
  for palavra in palavras:
    lista.append(palavra)

  return lista

def dicaPalavra(palavraCorreta):
  global palavras
  dica = ''
  for palavra in palavras:
    if (palavra == palavraCorreta):
      dica = palavras[palavraCorreta]['dica']
      dica = dica.upper()
  return dica

def palavraAleatoria():
  palavra = random.choice(listaPalavras())
  return palavra

def addEspaco(palavra):
  palavraFormat = ''
  for letra in palavra:
    palavraFormat += letra + ' '
  return palavraFormat

def forca(erros):

  if (erros == 0):
    print('     ________')
    print('     |/     | ')
    print('     |')
    print('     |')
    print('     |')
    print('     |')
    print('     |')
  elif (erros == 1):
    print('     ________')
    print('     |/     |')
    print('     |      O')
    print('     |')
    print('     |')
    print('     |')
    print('     |')
  elif (erros == 2):
    print('     ________')
    print('     |/     |')
    print('     |      O')
    print('     |      |')
    print('     |')
    print('     |')
    print('     |')
  elif (erros == 3):
    print('     ________')
    print('     |/     |')
    print('     |      O')
    print('     |      |')
    print('     |      |')
    print('     |')
    print('     |')
  elif (erros == 4):
    print('     ________')
    print('     |/     |')
    print('     |      O')
    print('     |      |>')
    print('     |      |')
    print('     |')
    print('     |')
    print('     |')
  elif (erros == 5):
    print('     ________')
    print('     |/     |')
    print('     |      O')
    print('     |     <|>')
    print('     |      |')
    print('     | ')
    print('     | ')
  elif (erros == 6):
    print('     ________')
    print('     |/     |')
    print('     |      O')
    print('     |     <|>')
    print('     |      |')
    print('     |       \ ')
    print('     | ')
  elif (erros == 7):
    print('------------------- GAME OVER -------------------')
    print('     ________')
    print('     |/     |')
    print('     |     x.x')
    print('     |     <|>')
    print('     |      |')
    print('     |     / \ ')
    print('     | ')

def removePalavra(palavraCorreta): 
  palavraCorreta = palavraCorreta.capitalize()
  
  if palavraCorreta in palavras:
    palavras.pop(palavraCorreta)

def iniciaJogo():
  jogando = True

  while(jogando):
    dica = ''
    erros = 0
    palavraCorreta = palavraAleatoria()
    dica = dicaPalavra(palavraCorreta)
    tracos = '_'*len(palavraCorreta)
    letras = '' 
    tentativa = ''
    
    while (erros < 7):
      system('clear')
      if (len(palavras) == 0):
        print('--------------------------------------')
        print('\t\tO jogo foi zerado!')
        print('--------------------------------------')
        print('\n\nVocê jogou com todas as palavras disponíveis.')
        print('Se desejar reiniciar o jogo, inicie-o novamente.')
        exit()
      else:
        #estrutura da interface
        print('\n\t\t\t\tJOGO DA FORCA\n\n')
        print('\tDICA: '+dica+'\n')
        forca(erros)
        print('\t\t\t\t'+addEspaco(tracos))
        print('\nLETRAS: '+addEspaco(letras))

        tracos = tracos.upper()
        palavraCorreta = palavraCorreta.upper()
        if(tracos != palavraCorreta or erros < 7):
          tentativa = input('\nTente uma letra: ')
          tentativa = tentativa.upper() 
          n = letras.count(tentativa)

          if (n > 0):
            print('\nVocê já tentou essa letra!')
            time.sleep(1) 
          elif (len(tentativa) > 1):
            print('\nVocê adicionou mais de uma letra!')
            time.sleep(1) 
          elif (not 'A' <= tentativa <= 'Z'):
            print('Digite apenas letras!')
            time.sleep(1) 
          else:
            letras += tentativa
            if (palavraCorreta.count(tentativa) > 0):
              for i in range(len(palavraCorreta)):
                if (tentativa == palavraCorreta[i]):
                  tracos = tracos[:i] + palavraCorreta[i] + tracos[i+1:]
            else:
              erros+=1

        if (erros == 7):
          system('clear')
          print('\n\t\t\t\tJOGO DA FORCA\n\n')
          print('\tDICA: '+dica+'\n')
          forca(erros)
          print('\nFORCA!!\nVocê esgotou todas as tentativas!')
          print('\nA palavra era: " '+palavraCorreta+' ".')
          break
        elif (palavraCorreta == tracos):
          system('clear')
          print('\n\t\t\t\tJOGO DA FORCA\n\n')
          print('\tDICA: '+dica+'\n')
          forca(erros)
          print('\t\t\t\t'+addEspaco(tracos))
          print('\nLETRAS: '+addEspaco(letras))
          print('\nParabéns! Você acertou a palavra!')
          break

    novoJogo = input('\nDeseja jogar novamente? (S/N) ')
    if (novoJogo == 'S' or novoJogo == 's'):
      jogando = True
      removePalavra(palavraCorreta)
    else:
      jogando = False
      system('clear')
      print('--------------------------------------')
      print('\t\t\tJogo Finalizado!')
      print('--------------------------------------')

iniciaJogo()