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

def funcq0(cadeia, index):
    return '', index

def funcq2(cadeia, index):
    if(cadeia in tabela_simb_reservados):
        return cadeia + ', ' + tabela_simb_reservados[cadeia] + '\n', index-1
    else:
        return cadeia + ', id\n', index-1

def funcq4(cadeia, index):
    return ':=, simb_atrib\n', index

def funcq5(cadeia, index):
    return ':, simb_dp\n', index-1

def funcq7(cadeia, index):
    return '<=, simb_menor_igual\n', index

def funcq8(cadeia, index):
    return '<>, simb_dif\n', index

def funcq9(cadeia, index):
    return '<, simb_menor\n', index-1

def funcq10(cadeia, index):
    return '=, simb_igual\n', index

def funcq12(cadeia, index):
    return '>=, simb_maior_igual\n'

def funcq13(cadeia, index):
    return '>, simb_maior\n', index-1

def funcq14(cadeia, index):
    return ';, simb_pv\n', index

def funcq16(cadeia, index):
    return cadeia + ', num_int\n', index-1

def funcq19(cadeia, index):
    return cadeia + ', num_real\n', index-1

def funcq21(cadeia, index):
    return cadeia + ', comentario\n', index

def funcq22(cadeia, index):
    return '(, simb_apar\n', index

def funcq23(cadeia, index):
    return '), simb_fpar\n', index

def funcq24(cadeia, index):
    return '+, simb_mais\n', index

def funcq25(cadeia, index):
    return '-, simb_menos\n', index

def funcq26(cadeia, index):
    return '., simb_p\n', index

def funcq27(cadeia, index):
    return '*, simb_mult\n', index

def funcq28(cadeia, index):
    return '/, simb_div\n', index

def funcq29(cadeia, index):
    return cadeia + ', erro("caractere nao permitido")\n', index

def funcq30(cadeia, index):
    return cadeia + ', erro("numero real mal formado")\n', index

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

estados_erro = ['q29', 'q30']
estado_inicial = 'q0'
estado_comentario = 'q20'

index = 0
output = ''
cadeia = ''
estado = ''

try:
    while(True):
        cadeia = ''
        estado = estado_inicial
        while(True):
            c = texto[index]
            index += 1
            if(c not in automato[estado].keys()):
                estado = tabela_outros[estado]
                if(estado in estados_finais.keys()):
                    if(estado in estados_erro):   
                        cadeia += c
                    func_output, index = estados_finais[estado](cadeia, index)
                    output += func_output
                    break
            else:
                cadeia += c
                estado = automato[estado][c]
                if(estado in estados_finais.keys()):
                    func_output, index = estados_finais[estado](cadeia, index)
                    output += func_output
                    break
except IndexError:
    if(estado == estado_comentario):
        output += cadeia + ', erro("comentario nao finalizado")\n'
    elif(estado != estado_inicial):
        func_output, index = estados_finais[tabela_outros[estado]](cadeia, index)
        output += func_output
print(output)

#print(json.dumps(automato, indent=4))
