dict_shopping ={"warzywniak": ["cebula", "pomidory","zmieniaki"], "apteka":["witamina c", "nurofen"]}
print("Lista zakupów")
suma = 0
for i in dict_shopping:
    print(f"Idę do {i.capitalize()} i kupuję tam: {dict_shopping[i]}")
    suma += len(dict_shopping[i])
print(f"W sumie kupuje {suma} rzeczy")