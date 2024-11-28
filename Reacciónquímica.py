# 1. Formación de una reacción química
reaction = Reaction({"CH4": 1, "O2": 2}, {"CO2": 1, "H2O": 2})

# Verificar si la ecuación está balanceada
print("La ecuación está balanceada:", reaction.is_balanced())

# Mostrar la ecuación balanceada
print("Ecuación balanceada:", reaction.formula)
