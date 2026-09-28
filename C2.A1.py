week = ['Lunes', 'Martes', 'Miercoles', 'jueves', 'Viernes', 'sabado', 'Domingo']
out = []
for indx, day in enumerate(week):
    if day in ['sabado', 'Domingo']:
        out.append(day)

print(out)