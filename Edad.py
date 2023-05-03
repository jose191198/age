
#1.-El doble de mi edad tiene 24 años, ¿cuántos años tengo? (x=?)

x = 24/2
print(x)

#2.- A un tercio de la edad de mi hermana le disminuyo 15 años para
#  tener la misma edad que yo. Yo tengo 6 años. 
# ¿Qué edad tiene ella? (Escribir la ecuación correspondiente, 
# despejar y calcular la nueva variable "y" de manera manual)

mi_edad2 = 6
suma_hermana = mi_edad2 + 15
y = suma_hermana * 3
print(y)

#3.-Determina quién es más grande (variables "x" y "y") utilizando if y else.

if x > y:
    print(f'Sujeto 1 es mayor que sujeto 2 con {x} años')
else:
    print(f'Sujeto 2 es mayor que sujeto 1 con {y} años')