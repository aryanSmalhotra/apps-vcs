from typing import ItemsView


items = {'candy':0.99,'milk':4.15,'chips':1.99}
a=input("what item's price you want to see")
if a == items['candy']:
    print(items["0.99"])
elif a == items["milk"]:
    print(items["4.15"])
elif a == items['chips']:
    print(items["1.99"])
else:
    print()