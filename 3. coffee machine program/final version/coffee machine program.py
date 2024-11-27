MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

moneyresource = 0
resources =  {**resources, "money": 0}

while 1<2:
    print("What would you like? (espresso/latte/cappuccino): ")
    userchoice = input()
    if userchoice == "report":
        print("Here are the current resources: ")
        print(resources)
    
    elif userchoice == "off":
        break
    
    elif userchoice == "espresso":
        # if MENU.get("expresso").get("ingredient").get("water") <= resources.get("water") and MENU.get("expresso").get("ingredient").get("coffee") <= resources.get("coffee"):
        if MENU['espresso']['ingredients']['water'] <= resources['water'] and MENU['espresso']['ingredients']['coffee'] <= resources['coffee']:
            print("thank you! We have sufficient resources to make espresso! Please insert money!")
            while 1<2:
                moneyinput = input()
                moneyinput = float(moneyinput)
                if moneyinput == MENU["espresso"]["cost"]:
                    moneyresource =+ moneyinput
                    resources.update({'water': resources.get("water") - 50, 'coffee': resources.get("coffee") - 18, "money": resources.get("money") + moneyresource})
                    print("Thank you! Your transaction is now complete!")
                    print("Here is your espresso. Enjoy!")
                    print("  ")
                    break
                
                elif moneyinput > MENU['espresso']['cost']:
                    change = moneyinput - MENU['espresso']['cost']
                    change = round(change,2)
                    moneyresource =+ MENU['espresso']['cost']
                    resources.update({'water': resources.get("water") - 50, 'coffee': resources.get("coffee") - 18, "money": resources.get("money") + moneyresource})
                    print ("Thank you! Your transaction is now complete! Here is " + str(change) + " dollars in change.")
                    print("Here is your espresso. Enjoy!")
                    print("  ")
                    break
                
                else:
                    print("Sorry! Insufficient money! Would you like to try again? Only type yes or no.")
                    moneyinputreentry = input()
                    if moneyinputreentry ==  "yes":
                        print("Press any button to try again!")
                        print("  ")
                    else:
                        print("Sorry that's not enough money. Money refunded.")
                        break
                        
        else:
            print("Sorry! We've run out of resources, so we cannot serve you espresso!")

    elif userchoice == "latte":
        # if MENU.get('latte').get('ingredient').get('water') <= resources.get('water') and MENU.get('latte').get('ingredient').get('milk') <= resources.get('milk') and MENU.get('latte').get('ingredient').get('coffee') <= resources.get('coffee'):
        if MENU['latte']['ingredients']['water'] <= resources['water'] and MENU['latte']['ingredients']['milk'] <= resources['milk'] and MENU['latte']['ingredients']['coffee'] <= resources['coffee']:
            print("thank you! We have sufficient resources to make latte! Please insert money!")
            while 1<2:
                moneyinput = input()
                moneyinput = float(moneyinput)
                if moneyinput == MENU["latte"]["cost"]:
                    moneyresource =+ moneyinput
                    resources.update({'water': resources.get("water") - 200, 'milk': resources.get("milk") - 150, 'coffee': resources.get("coffee") - 24, "money": resources.get("money") + moneyresource})
                    print("Thank you! Your transaction is now complete!")
                    print("Here is your latte. Enjoy!")
                    print("  ")
                    break

                elif moneyinput > MENU.get("latte").get("cost"):
                    change = moneyinput - MENU.get("latte").get("cost")
                    change = round(change,2)
                    moneyresource =+ MENU.get("latte").get("cost")
                    resources.update({'water': resources.get("water") - 200, 'milk': resources.get("milk") - 150, 'coffee': resources.get("coffee") - 24, "money": resources.get("money") + moneyresource})
                    print ("Thank you! Your transaction is now complete! Here is " + str(change) + " dollars in change.")
                    print("Here is your latte. Enjoy!")
                    print("  ")
                    break

                else:
                    print("Sorry! Insufficient money! Would you like to try again? Only type yes or no.")
                    moneyinputreentry = input()
                    if moneyinputreentry ==  "yes":
                        print("Press any button to try again!")
                        print("  ")
                    else:
                        print("Sorry that's not enough money. Money refunded.")
                        break
        else:
            print("Sorry! We've run out of resources, so we cannot serve you latte!")
        
    elif userchoice == "cappuccino":
        # if MENU.get("cappuccino").get("ingredient").get("water") <= resources.get("water") and MENU.get("cappuccino").get("ingredient").get("milk") <= resources.get("milk") and MENU.get("cappuccino").get("ingredient").get("coffee") <= resources.get("coffee"):
        if MENU['cappuccino']['ingredients']['water'] <= resources['water'] and MENU['cappuccino']['ingredients']['milk'] <= resources['milk'] and MENU['cappuccino']['ingredients']['coffee'] <= resources['coffee']:
            print("thank you! We have sufficient resources to make cappuccino! Please insert money!")
            while 1<2:
                moneyinput = input()
                moneyinput = float(moneyinput)
                if moneyinput == MENU['cappuccino']['cost']:
                    moneyresource =+ moneyinput
                    resources.update({'water': resources.get("water") - 250, 'milk': resources.get("milk") - 100, 'coffee': resources.get("coffee") - 24, "money": resources.get("money") + moneyresource})
                    print("Thank you! Your transaction is now complete!")
                    print("Here is your cappucino. Enjoy!")
                    print("  ")
                    break

                elif moneyinput > MENU.get("cappuccino").get("cost"):
                    change = moneyinput - MENU.get("cappuccino").get("cost")
                    change = round(change,2)
                    moneyresource =+ MENU.get("cappuccino").get("cost")
                    resources.update({'water': resources.get("water") - 250, 'milk': resources.get("milk") - 100, 'coffee': resources.get("coffee") - 24, "money": resources.get("money") + moneyresource})
                    print ("Thank you! Your transaction is now complete! Here is " + str(change) + " dollars in change.")
                    print("Here is your cappuccino. Enjoy!")
                    print("  ")
                    break

                else:
                    print("Sorry! Insufficient money! Would you like to try again? Only type yes or no.")
                    moneyinputreentry = input()
                    if moneyinputreentry ==  "yes":
                        print("Press any button to try again!")
                        print("  ")
                    else:
                        print("Sorry that's not enough money. Money refunded.")
                        break
        else:
            print("Sorry! We've run out of resources, so we cannot serve you cappuccino!")

    else:
        print("there's no such command built within our system. Please try again!")

exit()
