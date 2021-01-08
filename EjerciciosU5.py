import Metodos

path = "codigo.java"

try:
    archivo = open (path, 'r', encoding = 'UTF-8')

except:
    print ("El archivo que intentas abrir no existe")
    quit ()

texto = ""

for linea in archivo:
    texto += linea

print ("\n------------------------------------------------Codigo inicia------------------------------------------------------------\n", texto, "\n", "---------------------------------------------Fin codigo----------------------------------------------------------------------")
print("\n                                       Resultados del anáisis")

print("\nSentencia de asignación. ",Metodos.Sentencias_Asignacion(texto),
      "\nOperaciones aritméticas básicas. ", Metodos.Operaciones_Aritmetricas(texto),
      "\nExpresiones booleanas básicas. ", Metodos.Expresiones_Booleanas(texto),
      "\nFormulas más complejas ", Metodos.Formulas_Complejas(texto),
      "\nEl encabezado de estructura de control", Metodos.Estructuras_Control(texto))

