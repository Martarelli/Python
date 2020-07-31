def GeraDicionário():
    """
    Carrega o arquivo com a lista de palavras e com isso
    gera um dicionário, que é uma lista contendo todas as
    palavras, e a devolve
    """
    arquivo = open('PALAVRAS.txt', 'r')

    dicionário = []

    print('Carregando palavras para o Dicionário')

    for palavra in arquivo:
        separado = palavra.split('\n')
        print(separado[0])
        dicionário.append(separado[0])

    return dicionário


def RecebeFrase():
    """
    Das letras que recebemos temos que garantir nenhuma tenha
    acento ou ç
    """
    while True:
        frase = input('Digite a frase usando * para os caracteres desconhecidos\n')
        ok = True
        for char in frase:
            if not 'a' <= char <= 'z' and not 'A' <= char <= 'Z' and char != '*' and char != ' ':
                ok = false
                break
        if ok:
            return frase
        else:
            print('Digite letras sem acento e sem ç!')


def ProcuraPalavra(dicionário, palavra):
    """
    Procura as possíveis palavras para substituir
    a palavra passada, e as devolve numa lista
    """
    palavra = palavra.upper()

    if palavra [0] != '*':
        for i in range(len(dicionário)):
            if i % 100 == 0:
                print('Procurando letra no dicionário')
            if dicionário[i][0] == palavra[0]:
                break

        for j in range(i, len(dicionário)):
            if j % 100:
                print('Procurando letra no dicionário')
            if dicionário[j][0] != palavra[0]:
                break
        return SeparaPorTamanho(dicionário[i:j], palavra)
    else:
        return SeparaPorTamanho(dicionário, palavra)

def SeparaPorTamanho(dicionário, palavra):
    """
    Separa as possíveis candidatas a palavras substitutas
    por tamanho
    """
    tamanho = len(palavra)

    candidatos = []

    for word in dicionário:
        if tamanho == len(word):
            eh_candidata = True
            for i in range(tamanho):
                if palavra[i] != '*' and palavra[i] != word[i]:
                    eh_candidata = False
                    break
            if eh_candidata:
                print('Adicionando palavra candidata')
                candidatos.append(word)

    return candidatos

def GeraFrasesPossíveis(candidatas_totais):
    """
    A partir da matriz com todas as palavras candidatas
    essa função vai gerar todas as possíveis frases
    """

    aux = open('auxiliar.py', 'w')
    aux.write('def funcao_auxiliar(candidatas_totais):\n')
    aux.write('\tarquivo = open("FRASE.txt", "w")\n')

    aux.write('\tfrase = []\n')
    aux.write('\tfor i in range(len(candidatas_totais)):\n')
    aux.write('\t\tfrase.append("")\n')

    for i in range(len(candidatas_totais)):
        linha = '\t'*(i+1)
        linha += 'for a%i in range(len(candidatas_totais[%i])):\n'%(i,i)
        aux.write(linha)
        linha = '\t'*(i+2) + 'frase[%i]= candidatas_totais[%i][a%i]\n'%(i,i,i)
        aux.write(linha)

    aux.write('\t'*(i+2) + 'frase_s = ""\n')
    aux.write('\t'*(i+2) + 'for palavra in frase:\n')
    aux.write('\t'*(i+3)+ 'frase_s += palavra\n')
    aux.write('\t'*(i+3)+ 'frase_s += " "\n')
    aux.write('\t'*(i+2) + 'arquivo.write(frase_s + "\\n")\n')

    aux.write('\tarquivo.close()')

    aux.close()

    print("Gerando Lista de Palavras Candidatas...")
    
    from auxiliar import funcao_auxiliar

    funcao_auxiliar(candidatas_totais)     

def main():
    """
    Função principal do programa
    """
    dicionário = GeraDicionário()
    frase = RecebeFrase().split()

    candidatas_totais = []

    for palavra in frase:
        candidatas_totais.append(ProcuraPalavra(dicionário, palavra))

    GeraFrasesPossíveis(candidatas_totais)

    print('Operações Encerradas')



main()

    
