

### Medidor de Palavras por Texto ####

'''Breve descrição do projeto:
Crie um programa em Python que analisa um texto que for passado dentro do próprio terminal, contando a frequência de cada palavra no texto. Após realizar a contagem de cada 
palavra, o programa deve exibir qual palavra e quantas vezes aquela palavra apareceu no texto. Todo o programa deve funcionar a partir do terminal'''


# 1. Permitir inserir um bloco de texto:
# ○ Permitir que o usuário insira um bloco de texto no terminal

texto = input('Digite o texto: ')
# texto = '''testando o programa para ver se esse programa funciona direto após os testes. Os testes serão realizados para garantir a funcionalidade do programa'''

# Separa o testo em uma lista de palavras
texto_lista = texto.split()

# Cria um dicionário vazio
contagem = {}

# Contagem de frequencia:
for palavra in texto_lista:
    if palavra in contagem:
        contagem[palavra] += 1
    
    else:
        contagem[palavra] = 1


# 2. Contagem de Frequência de Palavras:
# Contar a frequência de cada palavra no texto, ignorando a diferenciação entre maiúsculas e minúsculas.

# Exibe a Contagem de frequencia:
print(f'Contagem de frequencia:')
for chave, frequencia in contagem.items():
    print(f'{chave}: {frequencia}')
print('############')

# ordena a lista resultante
contagem_ordenada = sorted(contagem.items(), key=lambda palavra: palavra[1], reverse=True)

# seleciona as 5 palavras mais frequentes
top_palavras = contagem_ordenada[:5]


# 3. Exibir as palavras mais frequentes
# Exibir as palavras mais frequentes no texto, em ordem crescente

# exibe as palavras mais frequentes
print(f'\nPalavras mais frequentes:')
for chave in top_palavras:
        print(chave[0])
print('############')

