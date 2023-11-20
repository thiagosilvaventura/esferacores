import sympy as sp

# Definindo os símbolos
r, k, n = sp.symbols('r k n')

# Área inicial de cada faixa (situação inicial)
A0 = (1/7) * 4 * sp.pi * r**2

# Fator de escala para a situação com distorção
Ad = (k/7) * 4 * sp.pi * r**2

# Área de cada faixa na situação com mais faixas
Am = (1/n) * 4 * sp.pi * r**2

# Relação para k na situação com distorção
k_relation = sp.solve(Ad / A0 - 1, k)

# Relação para n na situação com mais faixas
n_relation = sp.solve(Am / A0 - 1, n)

# Exibindo as relações
print("Relação para k na situação com distorção:")
print(k_relation)

print("\nRelação para n na situação com mais faixas:")
print(n_relation)
