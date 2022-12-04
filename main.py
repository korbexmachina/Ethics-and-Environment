from scenario import Scenario

# Creating all of the scenario objects

scenario0 = Scenario(
    "Oh no! Those pesky environmental regulations are really harshing our company's mellow. What should we do?", 
    "Keep company manufacturing in regulated country",
    "Move company manufacturing to less regulated country",
    0, -1, -2, 2,
    "ʕ•ᴥ•ʔ (The Lawyer)"
)

scenario1 = Scenario(
    "Last year we pulled in record earnings. Should we expand our operations or keep them as is?",
    "It is our manifest destiny to expand to the stars and beyond!",
    "It is too risky our current position is stable",
    -2, 3, 0, 0,
    "><((((⌐ಠ> (The Secretary)"
)

scenario2 = Scenario(
    "There's been a new innovation in manufacturing technology that can really increase our production,\noh slight issue though it might have some environmental consequences.",
    "Go for it",
    "No it is too dangerous",
    -3, 2, 1, 0,
    "><((((⌐ಠ> (The Secretary)"
)

scenario3 = Scenario(
    "Our factories in the Eastern District are producing extreme levels of toxic pollutants into the air,\nso much so that people are getting sick, and even dying!\nIt's unlikely that this sort of pollution will be traced back to us though… ",
    "Make some changes to the factories, better safe than sorry...",
    "Ehhhhh whats the worst that could happen...?",
    2, -2, -1, -2,
    "ʕ•ᴥ•ʔ (The Lawyer)"
)

scenario4 = Scenario(
    "Woah! The government is trying to pass a law that would make your current equipment obsolete.\nIf you donate to my campaign, I might just be able to rally some of my party members to oppose it.",
    "Sure, sounds like a fair deal!",
    "No dice, pal.",
    0, -2, 1, -2,
    "@_'-' (The Lawmaker)"
)

scenario5 = Scenario(
    "I have a great idea! Since we are based near an ocean why don't we start investing in wind turbines to help power our factories,\nsure it'll cost a bit of money to build but we'll get much more back eventually.",
    "Great idea!",
    "This isn't some sort of fantasyland of course that won't work",
    1, 1, -1, -1,
    "><((((⌐ಠ> (The Secretary)"
)

scenario6 = Scenario(
    "Hey there, Big Executive! I was wondering if you wanted to become a donor for our Environmental Non-Profit.\nIf you donate, you'd get your brand name all over our event banners and maybe even a shiny plaque in our headquarters.\nYou'd like that wouldn't you?",
    "Brand publicity AND a shiny plaque? I'm in! Oh, also the environment…yeah that's important.",
    "Get out of here you dirty my office floor",
    2, 1, -1, -1,
    "(^ • ε • ^) (The Non-Profit Representative)"
)

scenario7 = Scenario(
    "My coworkers and I can barely pay our living expenses. Can we pretty please have a raise?",
    "Sure you guys work hard enough",
    "Stop being lazy and get back to work",
    -1, 0, 0, 0,
    "υ´• ﻌ •`υ (The Factory Worker)"
)

scenario8 = Scenario(
    "Waste from one of our new factories is starting to build up, what should we do with it?",
    "Dump it into the ocean. It's big enough to hold it all.",
    "Fund waste management research",
    -99, -2, 0, 0, # -99 forces the blame the consumers ending
    "ʕ•ᴥ•ʔ (The Lawyer)"
)

# Initializing variables
money = 10
environment = 10
scenarios = [scenario0, scenario1, scenario2, scenario3, scenario4, scenario5, scenario6, scenario7, scenario8]

print("Welcome to the team, Big Executive! Your job is to improve the corporation. Good luck!\nType 1 or 2 to select an option when prompted\nPress Enter to continue:")
input()
print("\n" * 100)
# The actual game loop
for i in scenarios:
    print(f"Money: {money}\nEnvironmentalism: {environment}")
    print(i.__str__())
    while True:
        choice = input("Choose an option:")
        if choice == "1":
            money = i.option1_picked(environment, money)[1]
            environment = i.option1_picked(environment, money)[0]
            print("\n" * 100)
            break
        elif choice == "2":
            money = i.option2_picked(environment, money)[1]
            environment = i.option2_picked(environment, money)[0]
            print("\n" * 100)
            break
        else:
            print("Invalid choice, please make a valid selection: ", end="") # Prompt for a valid choice, and run through the loop again

#Endings
print(f"Money: {money}\nEnvironmental impact: {environment}")
if environment < -10:
    print("Our company is being blamed for environmental degradation, we need somebody to blame. Who better than those average joe consumers!\nShame on them for ruining the environment.")
elif environment >= 10 and money >= 10:
    print("Wow! We at Corporation Co. are astonished at your ability to both turn a profit and make our operations more sustainable.\nWe didn't know that was possible. Keep up the good work!")
elif environment <= 10 and money < 10:
    print("Your decisions have cost us financially and the board believes someone more amenable to our goals deserves your position.")
elif environment < 10 and money < 10:
    print("Your decisions have cost us financially and the board believes someone more amenable to our goals deserves your position.\nWe now have to file for bankruptcy and deal with an innumerable amount of federal and state lawsuits.")
elif environment > 10 and money < 10:
    print("You were so busy worrying about the “environment” and being “sustainable” that you ran Corporation Co. into the ground,\nthanks to you millions of people are unemployed!")
elif environment >= 10 and money > 10:
    print("You did your job well. We made a profit.")
else:
    print("You were perfectly mediocre.")
