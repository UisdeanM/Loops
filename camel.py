camelcase = input("camelCase:  ")
print("snake_case = : ", end="")
for _ in camelcase:
    if _.islower():
        print(_, end="")
    else:
        print("_" + _.lower(), end="")
print("")