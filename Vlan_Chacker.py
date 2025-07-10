#Vlan_Checker.py

vlan = int(input("ingrese el numero de la vlan"))

if 1 <= vlan <= 1005:
    print("la vlan esta en el rango NORMAL")
elif 1006 <= vlan <= 4094:
    print("la vlan esta en rl rango EXTENDIDO")
else:
    print ("La vlan ingresada no es valida(FUERA DE RANGO)")
    