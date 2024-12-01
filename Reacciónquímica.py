from chemlib import Compound, Reaction

# Crear compuestos
N2O5 = Compound("N2O5")
H2O = Compound("H2O")
HNO3 = Compound("HNO3")

# Crear una reacción usando los compuestos
reaction = Reaction([N2O5, H2O], [HNO3])

# Mostrar si la reacción está balanceada inicialmente
print("¿La reacción está balanceada?", reaction.is_balanced)

# Balancear la reacción
reaction.balance()

# Mostrar la fórmula balanceada
print("\nFórmula balanceada:")
print(reaction.formula)
