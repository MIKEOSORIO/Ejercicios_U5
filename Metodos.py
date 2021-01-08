import re

def Sentencias_Asignacion(codigo):

    patron = re.compile('[A-Za-z]\w*[ ]*[=][ ]*\w+[.]?\w*')
    resultado = re.findall(patron, codigo)
    return resultado

def Operaciones_Aritmetricas(codigo):

    patron2 = re.compile('[A-Za-z0-9-_]+\s*[=]+\s*[A-Za-z0-9-_|0-9.0-9]+\s*[\+,\-,\*,\/,\%,\^]+\s*[A-Za-z0-9-_|0-9.0-9]+')
    resultado2 = re.findall(patron2, codigo)
    return resultado2

def Expresiones_Booleanas(codigo):

    patron3 = re.compile('[A-Za-z]\w*[ ]*[<>!=][=][ ]*[A-Za-z0-9]|[A-Za-z]\w*[ ]*[<>][ ]*[A-Za-z0-9]')
    resultado3 = re.findall(patron3, codigo)
    return resultado3

def Formulas_Complejas(codigo):

    patron4 = re.compile('[A-Za-z0-9]+\s*=+\s*[A-Za-z0-9]+\s*[|<|>|!|<=|>=|\+|\-\*\/]\s*[(]+\s*[A-Za-z0-9]+\s*[|<|>|!|<=|>=|\+|\-\*\/]+\s*[A-Za-z0-9]+\s*[)]')
    resultado4 = re.findall(patron4, codigo)
    return resultado4

def Estructuras_Control(codigo):

    patron5 = re.compile('if[ ]*\(.+\)|while[ ]*\(.+\)|for[ ]*\(.+\)|else if[ ]*\(.+\)|switch[ ]*\(.+\)')
    resultado5 = re.findall(patron5, codigo)
    return resultado5

