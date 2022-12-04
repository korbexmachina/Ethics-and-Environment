from scenario import Scenario

money = 10
environment = 10

scenarios = []

scenario0 = Scenario(
    "Oh no! Those pesky environmental regulations are really harshing our company's mellow. What should we do? (The Lawyer)", 
    "Keep company manufacturing in regulated country (no change in environmental impact, - profit)",
    "Move company manufacturing to less regulated country(-- environmental impact, ++ profit)",
    0, -1, -2, 2
)

scenario1 = Scenario(
    "Last year we pulled in record earnings. Should we expand our operations or keep them as is?",
    "It is our manifest destiny to expand to the stars and beyond! (+ + + profit, - - environment)",
    "It is too risky our current position is stable (no change in profit, no change in environment)",
    -2, 3, 0, 0
)

scenario2 = Scenario(
    "There's been a new innovation in manufacturing technology that can really increase our production, oh slight issue though it might have some environmental consequences.",
    "Go for it(+ + profit, - - - environment)",
    "No it is too dangerous(no change in profit, + environment)",
    -3, 2, 1, 0
)

scenario3 = Scenario(
    "Our factories in the Eastern District are producing extreme levels of toxic pollutants into the air, so much so that people are getting sick, and even dying! It's unlikely that this sort of pollution will be traced back to us though… ",
    "Make some changes to the factories, better safe than sorry…(- - profit, + + environment)",
    "Ehhhhh whats the worst that could happen..? (- - profit, - environment)",
    2, -2, -1, -2
)

scenario4 = Scenario(
    "Woah! The government is trying to pass a law that would make your current equipment obsolete. If you donate to my campaign, I might just be able to rally some of my party members to oppose it.",
    "Sure, sounds like a fair deal! (no change in profit, - - environment)",
    "No dice, pal. (- - profit, + environment)",
    0, -2, 1, -2
)

scenario5 = Scenario(
    "I have a great idea! Since we are based near an ocean why don't we start investing in wind turbines to help power our factories, sure it'll cost a bit of money to build but we'll get much more back eventually.",
    "Great idea! (+ profit, + environment)",
    "This isn't some sort of fantasyland of course that won't work(- profit, - environment)",
    1, 1, -1, -1
)

scenario6 = Scenario(
    "Hey there, Big Executive! I was wondering if you wanted to become a donor for our Environmental Non-Profit. If you donate, you’d get your brand name all over our event banners and maybe even a shiny plaque in our headquarters. You’d like that wouldn’t you?",
    "Brand publicity AND a shiny plaque? I'm in! Oh, also the environment…yeah that's important. (+ profit, ++ environment)",
    "Get out of here you dirty my office floor (- profit, - environment)",
    2, 1, -1, -1
)

scenario7 = Scenario(
    "My coworkers and I can barely pay our living expenses. Can we pretty please have a raise?",
    "Sure you guys work hard enough (-profit, no change in environment)",
    "Stop being lazy and get back to work (no change in profit, no change in environment)",
    -1, 0, 0, 0
)

scenario8 = Scenario(
    "Waste from one of our new factories is starting to build up, what should we do with it?",
    "Dump it into the ocean. It's big enough to hold it all.",
    "Fund waste management research",
    0, 0, 1, -2
)

scenarios = [scenario0, scenario1, scenario2, scenario3, scenario4, scenario5, scenario6, scenario7, scenario8]

'''
22
    choice = input("Choose an option:")
    if choice == "1":
        money = scenario0.option1_picked(environment, money)[0]
        environment = scenario0.option1_picked(environment, money)[1]
        break
    elif choice == "2":
        money = scenario0.option2_picked(environment, money)[0]
        environment = scenario0.option2_picked(environment, money)[1]
        break
    else:
        print("Invalid choice, please make a valid selection: ", end="")

print(f"Money: {money}\nEnvironmental impact: {environment}")
'''

for i in scenarios:
    print(f"Money: {money}\nEnvironmental impact: {environment}")
    print(i.__str__())
    while True:
        choice = input("Choose an option:")
        if choice == "1":
            money = i.option1_picked(environment, money)[0]
            environment = i.option1_picked(environment, money)[1]
            print("\n" * 100)
            break
        elif choice == "2":
            money = i.option2_picked(environment, money)[0]
            environment = i.option2_picked(environment, money)[1]
            print("\n" * 100)
            break
        else:
            print("Invalid choice, please make a valid selection: ", end="")
