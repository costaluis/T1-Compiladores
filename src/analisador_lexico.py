import sys
import string
import json

if(len(sys.argv) > 2):
    print("Numero de argumentos invalido!")
    sys.exit(1)

try:
    f = open(sys.argv[1], "r")
except:
    print("Nao foi possivel abrir o arquivo!")
    sys.exit(2)

texto = f.read()

f.close()

tabela_simb_reservados = {
    'program' : 'simb_program',
    'var' : 'simb_var',
    'integer' : 'simb_tipo',
    'real' : 'simb_tipo',
    'begin' : 'simb_begin',
    'while' : 'simb_while',
    'do' : 'simb_do',
    'end' : 'simb_end',
    'if' : 'simb_if',
    'else' : 'simb_else',
    'write' : 'simb_write',
    'read' : 'simb_read',
    'for' : 'simb_for',
    'procedure' : 'simb_procedure'
}

cadeia = ''

estados_finais = {
    'q0' : funcq0,
    'q2' : funcq2,
    'q4' : funcq4,
    'q5' : funcq5,
    'q7' : funcq7,
    'q8' : funcq8,
    'q9' : funcq9,
    'q10' : funcq10,
    'q12' : funcq12,
    'q13' : funcq13,
    'q14' : funcq14,
    'q16' : funcq16,
    'q19' : funcq19,
    'q21' : funcq21,
    'q22' : funcq22,
    'q23' : funcq23,
    'q24' : funcq24,
    'q25' : funcq25,
    'q26' : funcq26,
    'q27' : funcq27,
    'q28' : funcq28,
    'q29' : funcq29,
    'q30' : funcq30
    }

automato = {
    'q0' : {' ' : 'q0',
            '\t' : 'q0',
            '\n' : 'q0',
            ':' : 'q3',
            '<' : 'q6',
            '=' : 'q10',
            '>' : 'q11',
            '{' : 'q20',
            ';' : 'q14',
            '(' : 'q22',
            ')' : 'q23',
            '+' : 'q24',
            '-' : 'q25',
            '*' : 'q27',
            '/' : 'q28',
            '.' : 'q26'
            },
    'q1' : {},
    'q3' : {'=' : 'q4'},
    'q6' : {'=' : 'q7'},
    'q6' : {'>' : 'q8'},
    'q11' : {'=' : 'q12'}, 
    'q20' : {'}' : 'q21'},
    'q15' : {'.' : 'q17'},
    'q17' : {},
    'q18' : {}
}
for letter in string.ascii_letters:
    automato['q0'][letter] = 'q1'
    automato['q1'][letter] = 'q1'

for digit in string.digits:
    automato['q0'][digit] = 'q15'
    automato['q1'][digit] = 'q1'
    automato['q15'][digit] = 'q15'
    automato['q17'][digit] = 'q18'
    automato['q18'][digit] = 'q18'

tabela_outros = {
    'q0' : 'q29',
    'q1' : 'q2',
    'q3' : 'q5',
    'q6' : 'q9',
    'q11' : 'q13',
    'q15' : 'q16',
    'q17' : 'q30',
    'q18' : 'q19',
    'q20' : 'q20'
}

index = 0
estado = 'q0'
output = ''

while(True):
    estado = 'q0'
    while(True):
        c = texto[index]
        if(c not in automato[estado].keys()):
            estado = tabela_outros[estado]
        else:
            cadeia += c
            estado = automato[estado][c]
            if(estado in estados_finais.keys()):
                func_output, index = estados_finais[estado](cadeia, index)
                output += func_output
                break
            index += 1


            



print(json.dumps(automato, indent=4))
