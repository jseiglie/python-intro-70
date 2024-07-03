
# int -5 5 100 float 1.5 
# kjahsdjkhasjkd 
# array en python es lista [1,2,3] 
# tuple (1,2,3) no se pueden modificar valores
# set {1,2,3} no pueden repetirse valores
# obj de js se llaman diccionarios

arr = [1,2,3]

print(arr[0])
arr[0]=58
arr.append('pepe')
arr.remove(58)
#print(arr)


#for el in arr:
#    print('loop ', el)

range(10) # 0-9
range(1,5) # 1-4
range(1,10,2) # 1 3 5 7 9

# myRange = range(1,10,2)
# print(list(myRange))

# for x in myRange:
#     print(x)

# list = [1,2,3,4,5,6,78,8,9]

# for item in range(len(list)):
#     print(f"elemento en indice {item}: {list[item]}")
    

#boolean -> True False

#operadores logicos
# > < ==  <= >=  and or not

# arra = [1,2,3, 'pepe']

# x=10
# y=5

# resultado = (x<5) or (y>1) 
# print(resultado)

# bol = True
# print( not bol)


def sayHi(name):
    return 'Hi ' + name

print(sayHi('Pepe'))

def sum(a,b):
    return a+b

print(sum(5,5))

#const sum = (a,b) => a+b
suma = lambda x,y : x+y
print(suma(2,2)) 


arra = [1,2,3]

#map(funcion, iterable)
#arra.map(el => el*2)
#const multi = (el) => el*2
# arra.map(multi)
def multi(num):
    return num*2

print(
    list(map( lambda x: x*2 , arra))
)

print(
    list(map(multi , arra))
)

if (1>2):
    print('esto que cosa es?')
elif (1<2):
    print('eso esta mejor')
else: 
    print('otra cosa')