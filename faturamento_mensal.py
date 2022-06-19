SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
OUTROS = 19849.53

TOTAL = SP + RJ + MG + ES + OUTROS
PER_SP = SP / TOTAL * 100
PER_RJ = RJ / TOTAL * 100
PER_MG = MG / TOTAL * 100
PER_ES = ES / TOTAL * 100
PER_OUTROS = OUTROS / TOTAL * 100

print(f'SP representou {PER_SP:.2f}% do valor total mensal')
print(f'RJ representou {PER_RJ:.2f}% do valor total mensal')
print(f'MG representou {PER_MG:.2f}% do valor total mensal')
print(f'ES representou {PER_ES:.2f}% do valor total mensal')
print(f'Outros estados representaram {PER_OUTROS:.2f}% do valor total mensal')
