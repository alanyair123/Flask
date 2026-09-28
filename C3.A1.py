nums = ["Uno", "Dos", "Tres", "Cuatro", "Cinco", "Seis", "Siete", "Ocho", "Nueve", "Diez"]
colors = ["Rojo", "Azul", "Verde", "Amarillo", "Rosa", "Morado", "Naranja", "Blanco", "Negro", "Gris"]
#print(nums)
#colors.append('viloeta')
#colors.extend('viloeta')
#colors.insert(0,'viloeta')
#colors.clear()
#colors.append('viloeta')
#print(colors.pop())
#colors.sort(reverse=True)
#colors.sort(reverse=False)
#colors_1=colors.copy()
#print(colors_1)
nums.reverse()
#print(colors)
nuevaLista = []
for num in nums:
    sal = [num,colors[nums.index(num)]]
    nuevaLista.append(sal)
print(nuevaLista)






     


