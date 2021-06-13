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
    sys.exit(1)

texto = f.read()
index = 0

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

estados_finais = {'q2' : funcq2}

estados_finais['q2'](index)

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
    

print(json.dumps(automato, indent=4))
