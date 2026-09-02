import csv

# criação da estrutura para representar um discente -  Classe Discente
class Discente:
    def __init__(self, matricula, nome, ano, periodo, tipo, status, nivel, curso, modalidade, unidade, unidade_gestora):
        # mapeamento de cada coluna do CSV para os atributos do objeto
        self.matricula = matricula
        self.nome = nome
        self.ano = ano
        self.periodo = periodo
        self.tipo = tipo
        self.status = status
        self.nivel = nivel
        self.curso = curso
        self.modalidade = modalidade
        self.unidade = unidade
        self.unidade_gestora = unidade_gestora

# leitura dos dados e mapeamento para a classe discente
def mapear_dados_csv(nome_arquivo):
    # aqui abrimos o arquivo de forma tradicional para leitura de nomes que contenham acentos e pontuações
    arquivo = open(nome_arquivo, 'r', encoding='utf-8')
    linhas = arquivo.readlines()
    arquivo.close()
    
    # verificação do cabeçalho: o índice 0 no modelo de linhas e colunas sempre guardara, aqui, a primeira linha (cabeçalho)
    cabecalho = linhas[0].strip()
    print("Cabeçalho verificado no CSV:", cabecalho)
    
    # estrutura da linha -  PARTE 2: criação de lista, mas sem a função implementada.
    lista_de_objetos = []
    
    # o laço for inicia a leitura no índice 1 para ignorar o cabeçalho lido acima, então percorremos os nomes
    for i in range(1, len(linhas)):
        # limpa as quebras de linha e remove aspas duplas dos textos, tornando mais facil a extração de dados
        linha_limpa = linhas[i].strip().replace('"', '')
        
        # esse if evita erro caso o arquivo tenha uma linha em branco no final
        if linha_limpa != "":
            # quebra a string em uma lista de colunas separadas por vírgula, assim como no arquivo csv
            colunas = linha_limpa.split(',')
            
            # instancia a classe mapeando as strings extraídas para o formato de objeto esperado
            aluno_mapeado = Discente(
                colunas[0], colunas[1], colunas[2], colunas[3], 
                colunas[4], colunas[5], colunas[6], colunas[7], 
                colunas[8], colunas[9], colunas[10]
            )
            
            lista_de_objetos.append(aluno_mapeado)
            
    # retorna os dados mapeados para que a Parte 2 (funcao que percorre os nomes) e 3(funcao de impressao) assumam o controle
    return lista_de_objetos

######################################################################
## implementando a função de impressão das informações de um discente:
######################################################################
def imprimir_discente(aluno):
    print(f"Matrícula        : {aluno.matricula}")
    print(f"Nome            : {aluno.nome}")
    print(f"Ano/Período     : {aluno.ano}.{aluno.periodo}")
    print(f"Tipo/Status     : {aluno.tipo} - {aluno.status}")
    print(f"Nível de Ensino : {aluno.nivel}")
    print(f"Curso           : {aluno.curso} ({aluno.modalidade})")
    print(f"Unidade         : {aluno.unidade}")
    print(f"Unidade Gestora : {aluno.unidade_gestora}")
    print("----------------------------------------\n")

# atualização da função de leitura do discente de acordo com a nova formatação e criação de função própria:
def ler_discente(lista_de_objetos):
    for aluno in lista_de_objetos:
	    imprimir_discente(aluno)

## área de testes ##
# aqui estamos chamando a função e passando o nome real do arquivo para verificar se está tudo ok
#nome_do_csv = "dis-csv-discentes-de-graduacao-de-2026.csv"
#lista_pronta = mapear_dados_csv(nome_do_csv)
# testes
#print(f"Total de alunos carregados na memória: {len(lista_pronta)}")
#ler_discente(lista_pronta)

#função para percorrer a lista de alunos e escrever no arquivo .txt
def arquivo_txt(lista_de_objetos, nome_arquivo):
     with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
          for aluno in lista_de_objetos:
               arquivo.write(f"Matrícula: {aluno.matricula}\n")
               arquivo.write(f"Nome: {aluno.nome}\n")
               arquivo.write(f"Ano/Período: {aluno.ano}.{aluno.periodo}\n")
               arquivo.write(f"Tipo/Status: {aluno.tipo} - {aluno.status}\n")
               arquivo.write(f"Nível de Ensino: {aluno.nivel}\n")
               arquivo.write(f"Curso: {aluno.curso}\n")
               arquivo.write(f"Unidade: {aluno.unidade}\n")
               arquivo.write(f"Unidade Gestora: {aluno.unidade_gestora}\n")
               arquivo.write(f"----------------------------------------------\n\n")

     print(f"Dados salvos com sucesso em: {nome_arquivo}")

#função main para ler .csv, criar lista de discentes e salvra no .txt 
def main():
     nome_do_csv = "dis-csv-discentes-de-graduacao-de-2026.csv"
     nome_do_txt = "discentes_2026.txt"
     lista_de_objetos = mapear_dados_csv(nome_do_csv)
     print(f"Total de alunos carregados na memória: {len(lista_de_objetos)}")
     arquivo_txt(lista_de_objetos, nome_do_txt)

if __name__ == "__main__":
     main()

