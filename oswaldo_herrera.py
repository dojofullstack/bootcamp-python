# import Dilva

import  json


# esto es un comentario en python
print("hello world");

""" esto es un comentario de multiples entrelineas"""

"""tipos de datos en python:"""

# tipo de dato string: 'hola mundo' str()
#tipo de dato numeral (int o float): 10 10.5
#tipo de dato array o listas:['python','javascript']
#tipo de dato booleano: true o false
#tipo de dato diccionario: {'usuario': 'henry', 'email': 'hola@dojopy.com'}
#tipo de dato conjunto o set: {'c++','java'}
#tipo de dato tupla o tuple: ('pablo', 'rosa')


"""tipo de dato String"""

mystack_favorito = 'python'

print(type(mystack_favorito))
print(dir(mystack_favorito))

print(mystack_favorito.upper())
print(mystack_favorito.lower())
print(mystack_favorito.replace('py', '00'))
print(mystack_favorito.find('py'))
print(mystack_favorito.isnumeric())

str()

conversion_string = str(12)

print(type(conversion_string))





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


# """ TIPO DE DATO ARRAY O LISTA """

# lista_tareas = ['aprender python' , 'aprender javascript',100]

# print('mi lista tiene: ',len(lista_tareas) ,'elementos')
# print(f'mi lista tiene {len(lista_tareas)} elementos ')

# print(type(lista_tareas))
# print(dir(lista_tareas))

# lista_tareas.append('aprender React Native')

# print(lista_tareas)

# lista_tareas.insert('aprender Django')

# mi_nombre="oswaldo"
# print(list('oswaldo'))

# """ TIPOS DE DATOS BOOLEANOS """

# is_active = True

# print(is_active)
# print(type(is_active))
# print(bool(list_tareas))

# print(is_active + 1)

""" tipo de dato dict """

perfil_user = {
    'nombre' : 'henry',
    'email' : 'henry@gmail.com',
    'age' : 24,
    'lista_stack': [
        'python' , 'react'
    ]
}

# print(perfil_user['nombre'])
# print(perfil_user['email'])

print(perfil_user.get('emails', 'soporte@gmail.com'))

print(dir(perfil_user))

print(perfil_user.keys())

print(perfil_user.values())

perfil_user['nombre'] = 'Alan'
print(perfil_user)

del perfil_user['email']

print(perfil_user)

# data_json = open('/direccion').read()

# data_product =json.loads(data_json)
# print(data_product)