#Compuestos químicos
#Formación de un compuesto
#Masa molar
#Composición porcentual en masa
#Estequiometría

from chemlib import Compound

# 1. Formación de un compuesto
water = Compound("H2O")
print("Fórmula del compuesto:", water.formula)

# 2. Masa molar
print("Masa molar del agua (H2O):", water.molar_mass(), "g/mol")

# 3. Composición porcentual en masa
from chemlib import Compound

# Crear un compuesto químico
compound = Compound("H2O")  

# Obtener los elementos del compuesto
elements = compound.occurences.keys() 

# Calcular y mostrar la composición porcentual en masa de cada elemento
print(f"Composición porcentual en masa de {compound.formula}:")
for element in elements:
    percentage = compound.percentage_by_mass(element)
    print(f"{element}: {percentage:.2f}%")

# 4. Estequiometría 
from chemlib import Compound

# Crear un compuesto químico
compound = Compound("H2O")  

# Cantidad inicial en gramos
cantidad_gramos = 5  

# Calcular cantidades estequiométricas
resultados = compound.get_amounts(grams=cantidad_gramos)

# Mostrar los resultados
print(f"Resultados estequiométricos para {compound.formula}:")
print(f"Gramos: {resultados['grams']:.2f} g")
print(f"Moles: {resultados['moles']:.4f} mol")
print(f"Moléculas: {resultados['molecules']:.2e} moléculas")
