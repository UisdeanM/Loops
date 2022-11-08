#machine accepts 25, 10, 5
#coke costs 50c



cost = 50



while cost > 0:
    coin = int(input("Insert coin: "))
    if coin in [5, 10, 25]:
        cost -= coin
    print("Amount due :", cost)

change_owed = abs(cost)

print("Change owed: ", change_owed)


