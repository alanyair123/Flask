nums = ["Uno", "Dos", "Tres", "Cuatro", "Cinco"]
colors = ["Rojo", "Azul", "Verde", "Amarillo", "Rosa", "Morado", "Naranja", "Blanco", "Negro", "Gris"]
ips = ["127.0.0.1", "192.168.0.1", "10.0.0.1"]
device_names = ["Router", "Switch", "Firewall"]

"""
for ip in ips:
    for device in device_names:
        if ip == "192.168.0.1" and device == "Router":
            print(f"IP: {ip}, Device: {device}")
"""

dispo = ["Router", "192.168.0.1", ["P1", "192.168.0.2"]]
# dispo.append(["P1", "192.169.0.2"])
print(dispo[2][1])

di_1 ={"D1": "Datos":"Datos"}
print(di_1.get("D2"))
