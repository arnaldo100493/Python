# Hola Mundo

print("Hola, Python!")

'''
Este
es
un
comentario.
'''

'''(variable) my_string: Literal['Aquí cambia el valor de la cadena de texto']'''

my_string = "Esto es una cadena de texto."
my_string = "Aquí cambia el valor de la cadena de texto."
print(type(my_string))
print(my_string)

my_string = 6 #Tipado dinmámico
print(type(my_string))
print(my_string)

my_other_string: str = "Esto es otra cadena de texto."
#my_other_string = 10 #Se cambiaría el tipo igualmente

my_int = 7
my_int = my_int + 4
print(my_int)
print(my_int - 1)
print(my_int)

my_float = 6.5
print(type(my_float))
print(my_float)

print(my_int + my_float)
#print(my_int + my_float + my_other_string) #Error

my_bool = True
my_bool = False
print(type(my_bool))
print(my_bool)

print("El valor de mi entero es " + str(my_int) + " y el de mi bool " + str(my_bool))
print(f"El valor de mi entero es {my_int} y el de mi bool {my_bool}")

my_list = [my_other_string, my_int, my_float, my_bool]
print(type(my_list))
my_list.append(my_bool)
print(my_list)
print(my_list[0])
#print(my_list[4]) #Error

my_dict = {"string": my_other_string, "string": my_int, "string": my_float, "string":  my_bool, "mouredev": "Brais Moure"}
print(type(my_dict))
print(my_dict)
print(my_dict["mouredev"])

my_set = {my_other_string, my_int, my_float, my_bool, my_bool, my_bool}
print(type(my_set))
print(my_set)

my_tuple = (my_other_string, my_int, my_float, my_bool, my_bool, my_bool)
print(type(my_tuple))
print(my_tuple)

if my_int == 11 or my_bool == True:
   print("El valor es 11.")
elif my_int == 12:
   print("El valor es 12.")   
else:
   print("El valoe no es 11 ni 12.")

for my_item in my_list:
   print(my_item)

for my_item in range(10):
   print(my_item)

for my_item in my_dict:
   print(my_item)                  

for my_item in my_set:
   print(my_item)

for my_item in my_tuple:
   print(my_item)     

def my_function():
    print("Esto es una función")

#my_function()

for my_item in range(10):
    my_function()

def my_function_with_return(param):
    return 10 + param

my_return = my_function_with_return(5)
print(my_return)

class MyClass:
   
   my_name = ""

   def __init__(self, my_name):
      self.my_name = my_name

   def print_name(self):
       print(self.my_name)   


my_class = MyClass("Brais")
my_class.print_name()
my_class.my_name = "Mouredev"
print(type(my_class))
print(my_class.my_name) 





