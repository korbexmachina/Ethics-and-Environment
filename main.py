from scenario import scenario

money = 50
environment = 50

scenarios = []

scenario0 = scenario("Oh no! Those pesky environmental regulations are really harshing our company’s mellow. What should we do? (The Lawyer)", 
                     "Keep company manufacturing in regulated country (no change in environmental impact, - profit)",
                     "Move company manufacturing to less regulated country(-- environmental impact, ++ profit)",
                     0, -1, -2, 2)

print(f"Money: {money}\nEnvironmental impact: {environment}")
print(scenario0.__str__())

while True:
    choice = input("Choose an option:")
    if choice == "1":
        money = scenario0.option1_picked(environment, money)[0]
        environment = scenario0.option2_picked(environment)[1]
        break
    elif choice == "2":
        money = scenario0.option2_picked(environment, money)[0]
        environment = scenario0.option2_picked(environment)[1]
        break
    else:
        print("Invalid choice, please make a valid selection: ", end="")

print(f"Money: {money}\nEnvironmental impact: {environment}")
