#/usr/bin/python3
'''
Gerador de arquivos de teste para questão 3
'''
import random

FIRST_NAME_MALES = ['ALBERTO', 'BERNARDO', 'CARLOS', 'DIEGO', 'EDUARDO',
'FLÁVIO', 'GUSTAVO', 'HENRIQUE', 'IGOR', 'JOÃO', 'KAIO', 'LUIZ', 'MARCOS',
'NORBERTO', 'OTÁVIO', 'PAULO', 'QUINCAS', 'RAFAEL', 'SAMUEL', 'TIAGO',
'ULISSES', 'VITOR', 'WILLIAM', 'XAVIER', 'YAGO', 'ZEUS']

FIRST_NAME_FEMALES = ['ALANA', 'BÁRBARA', 'CAMILA', 'DANIELE', 'EMÍLIA',
'FERNANDA', 'GABRIELLY', 'HELENA', 'ISABELE', 'JULIA', 'KELLY', 'LILIAN',
'MARIA', 'NICOLE', 'OLGA', 'PRISCILA', 'QUITÉRIA', 'RENATA', 'SAMARA',
'TALITA', 'URSULA', 'VANESSA', 'WILMA', 'XAYENE', 'YASMIM', 'ZULMIRA']

LAST_NAMES = ['ALMEIDA', 'BARBOSA', 'CABRAL', 'DINIZ', 'ESTEVES', 'FIGUEIREDO',
'GALVÃO', 'HORA', 'IBERS', 'JARDIM', 'KYLE', 'LACERDA', 'MACEDO', 'NOBREGA',
'OLIVEIRA', 'PAIVA', 'QUEIROZ', 'RIBEIRO', 'SACRAMENTO', 'TAVARES', 'UCHOA',
'VIEIRA', 'WILLIAMS', 'XAVIER', 'YNH', 'ZIL']

MONTHLY_DAYS = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31,
    11: 30, 12: 31
}
MONTHLY_NAMES = {
    1: 'JANEIRO', 2: 'FEVEREIRO', 3: 'MARÇO', 4: 'ABRIL', 5: 'MAIO', 6: 'JUNHO',
    7: 'JULHO', 8: 'AGOSTO', 9: 'SETEMBRO', 10: 'OUTUBRO', 11: 'NOVEMBRO',
    12: 'DEZEMBRO'
}

def generate_name(gender = ''):
    if gender.startswith('f') or gender.startswith('F'):
        gender_list = FIRST_NAME_FEMALES
    elif gender.startswith('m') or gender.startswith('M'):
        gender_list = FIRST_NAME_MALES
    else:
        gender_list = random.choice([FIRST_NAME_FEMALES, FIRST_NAME_MALES])
    return random.choice(gender_list)+' '+random.choice(LAST_NAMES)

def generate_birthday():
    month = random.randint(1, 12)
    month_name = MONTHLY_NAMES[month]
    day = random.randint(1, MONTHLY_DAYS[month] + 1)
    return f"{day} DE {month_name}"

def generate_file(qtd, file_name = 'pessoas.txt'):
    with open(file_name, 'w') as arquivo:
        pessoas = list()
        for i in range(qtd):
            pessoas.append(', '.join([generate_name(), generate_birthday()]))
        arquivo.write('\n'.join(pessoas))
        arquivo.close()

if __name__ == '__main__':
    quantidade = int(input("Quantidade de pessoas: "))
    generate_file(quantidade)