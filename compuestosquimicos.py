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
percent_composition = water.percent_composition()
print("Composición porcentual del agua:")
for element, percentage in percent_composition.items():
    print(f" - {element}: {percentage:.2f}%")

# 4. Estequiometría (balancear una ecuación)
from chemlib import Reaction

reaction = Reaction({"H2": 2, "O2": 1}, {"H2O": 2})
print("Balance de la reacción:", reaction.is_balanced())  # Debe devolver True
print("Ecuación balanceada:", reaction.formula)
