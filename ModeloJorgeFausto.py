# import RaulArispe
import json


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
# mystack_favorito = "python python"

# print(type(mystack_favorito))

# print(dir(mystack_favorito))

# print(mystack_favorito.upper())
# print(mystack_favorito.lower())
# print(mystack_favorito.replace('py', '00') )
# print(mystack_favorito.find('xyz'))
# print(mystack_favorito.isnumeric())

# conversion_string = str(12)

# print(type(conversion_string))





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
mystack_favorito = ''

# print(type(mystack_favorito))

# print(dir(mystack_favorito))

# print(mystack_favorito.upper())
# print(mystack_favorito.lower())
# print(mystack_favorito.replace('py', '00') )
# print(mystack_favorito.find('xyz'))
# print(mystack_favorito.isnumeric())

# conversion_string = str(12)

# print(type(conversion_string))


""" TIPO DE DATO ARRAY O LISTA """

lista_tareas = ['aprender python', 'aprender javascript', 100 ]

# print('mi lista tiene: ', len(lista_tareas), 'elemnetos')
# print(f'mi lista tiene {len(lista_tareas)} elementos')

# print(type(lista_tareas))

# print(dir(lista_tareas))

# lista_tareas.append('aprender React Native')

# print(lista_tareas)

# lista_tareas.insert(1, 'aprender Django')

# print(lista_tareas)

# print(lista_tareas[0:2])

# lista_tareas.remove('aprender javascript')

# print(lista_tareas)

# tareas_hermano = ['pintar', 'ir al cole']

# lista_tareas.extend(tareas_hermano)

# print(lista_tareas)


# lista_tareas = []

# lista_tareas.clear()

# print(lista_tareas)

# print(list('henry'))


""" TIPO DE DATOS BOOLEANOS """

# is_active = True

# print(is_active)
# print(type(is_active))
# print(bool(lista_tareas))

# print(is_active + 1)

""" TIPO DE DATO DICT """

perfil_user = {
    'nombre': 'henry',
    'email': 'henry@gmail.com',
    'age': 24,
    'lista_stack': [
        'python', 'react'
    ]
}

# print(perfil_user['nombres']
# print(perfil_user['dni'])

print(perfil_user.get('emailss', 'soporte@dojopy.com'))

print(dir(perfil_user))

print(perfil_user.keys())

print(perfil_user.values())

perfil_user['nombre'] = 'Alan'
print(perfil_user)

del perfil_user['email']

print(perfil_user)

# perfil_user = {}
# perfil_user.clear()

print(perfil_user.items())


# data_json = open('/home/henry/dojopy/bootcamp-lunes-miercoles/bootcamp-python/data.json').read()
# data_json.close()


# with open('/home/henry/dojopy/bootcamp-lunes-miercoles/bootcamp-python/data.json') as file:
#     data_json = file.read()


# data_product = json.loads(data_json)


# print('data del JSON')
# print(data_product)
# print(data_product[0].get('producto'))
# print(data_product[1].get('precio'))


""" TIPO DE DATO SET O CONJUNTOS """

mis_lenguajes_favoritos = {'python', 'javascript', 'flutter', 'python'}

print(mis_lenguajes_favoritos)
print(type(mis_lenguajes_favoritos))
print(dir(mis_lenguajes_favoritos))
print(len(mis_lenguajes_favoritos))

mis_lenguajes_favoritos.add('reactJS')
print(mis_lenguajes_favoritos)
mis_lenguajes_favoritos.remove('flutter')
print(mis_lenguajes_favoritos)


