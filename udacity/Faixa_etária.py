# -*- coding: cp1252 -*-

def funcao1():
    print "esta funcao n�o faz nada"

def funcao2(x):
    if type(x) == str:
        print "x � uma string", x
    elif type(x) == int:
        print "x � um n�mero inteiro",x
    elif type(x) == float:
        print "x � um n�mero float",x
    else:
        print "ah, tou com pregui�a, me mostre o tipo de x a�, v�, na moral, v�", type(x)

def funcao3(par):
    variavel = "bli"
    return par == variavel

def faixa_etaria(idade):
    if 18 <= idade < 60:
        return "adulto"
    elif idade <= 10:
        return "crian�a"
    elif idade >= 60:
        return "idoso"
    elif 10<idade<18:
        return "adolescente"

#funcao1()
#funcao2("mauricio")
#funcao1()
#funcao2(3)
#funcao2(5.0)
#funcao2([])
#resp1 = funcao3("bli")
#print "O resultado da primeira compara��o �", resp1
#resp2 = funcao3("bla")

mauricio = 33
igor = 5
braulio = 80
andre = 16

print "Mauricio � ",faixa_etaria(mauricio)
print "Igor � "    ,faixa_etaria(igor)
print "Br�ulio �"  ,faixa_etaria(braulio)
print "Andr� �"    ,faixa_etaria(andre)
