print("HEstos ceelos me hacen daño me enloqueceeeeeeeeen")
print("jamas aprenderé a vivir sin tii")
#Atentamente: Vicente
""" Canción = Estos celos jsjs"""
#String= "Helloo"
#tipo numero= 2 (int)
#tipo numero= 2.2 (float)
#listas = []
#tuplas=()
#diccionarios={ "user" : "henry", "email", "hola@gmail.com"}
#Booleano= True/False

word= "python"




# esto es un comentario en Python
print('hello world')

""" esto es un
comentario de multiples lineas
"""

"""  Tipos de datos en Python """


# Tipo de dato String: 'hola mundo'  str()
# Tipo de dato Numeral (int o float):    10, 10.5  int()  float()
# Tipo de dato array o listas:  ['python', 'javascript']  list()
# Tipo de dato Booleano: True / False  bool()
# Tipo de dato Diccionario:  {'usuario': 'henry', 'email': 'hola@dojopy.com}  dict()
# Tipo de dato conjunto o set:  {'c++', 'java'} set()
# Tipo de dato Tupla o tuple:  ('pablo', 'rosa')  tuple()



""" Tipo de dato Sring """
mystack_favorito = "python python"

print(type(mystack_favorito))

print(dir(mystack_favorito))

print(mystack_favorito.upper())
print(mystack_favorito.lower())
print(mystack_favorito.replace('py', '00') )
print(mystack_favorito.find('xyz'))
print(mystack_favorito.isnumeric())

conversion_string = str(12)

print(type(conversion_string))
"""Arrays """
lista=["python","js",100]
print(f" la lista posee {len(lista)}")
print(list("Mathias-Dev"))
data_json = open('/home/henry/dojopy/bootcamp-lunes-miercoles/bootcamp-python/data.json').read()_# data_json.close()


with open('/home/henry/dojopy/bootcamp-lunes-miercoles/bootcamp-python/data.json') as file:
    data_json = file.read()

product = json.loads(data_json)