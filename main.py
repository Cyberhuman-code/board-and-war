import random
def attackActive():
    if plr1[int(percNum)][3] > 0:
        if plr1[int(percNum)][0] == "Eye":
            for f in range(random.randrange(1, 5)):
                if plr2[int(attackNum)][3] > 0:
                    plr2[int(attackNum)][3] -= plr1[int(percNum)][4] * plr1[int(percNum)][5]
                    plr1[len(plr1)-1] += plr1[int(percNum)][3]
                    if plr2[int(attackNum)][3] > 0:
                        if plr2[int(attackNum)][3] <= 0:
                            plr1[len(plr1)-1] += plr2[int(attackNum)][4]
                            plr1[int(percNum)][5] += 0.5
                        print(f"Tower {plr2[int(attackNum)][0]} Now have {plr2[int(attackNum)][3]} HP")
                    else:
                        print(f"Tower {plr2[int(attackNum)][0]} already died")
                else:
                    print(f"Tower {plr2[int(attackNum)][0]} already died")
        elif plr1[int(percNum)][0] == "Tank":
            for f in range(random.randrange(1, 2)):
                plr2[int(attackNum)][3] -= random.randrange(plr1[int(percNum)][4] - 50, plr1[int(percNum)][4] + 50) * plr1[int(percNum)][5]
                plr1[len(plr1)-1] += plr1[int(percNum)][3]
                if plr2[int(attackNum)][3] > 0:
                    if plr2[int(attackNum)][3] <= 0:
                        plr1[len(plr1)-1] += plr2[int(attackNum)][4]
                        plr1[int(percNum)][5] += 0.5
                    print(f"Tower {plr2[int(attackNum)][0]} Now have {plr2[int(attackNum)][3]} HP")
                else:
                    print(f"Tower {plr2[int(attackNum)][0]} already died")
        elif plr1[int(percNum)][0] == "Arrowman":
            if plr2[int(attackNum)][3] > 0:
                plr2[int(attackNum)][3] -= plr1[int(percNum)][4] * plr1[int(percNum)][5]
                plr1[int(percNum)][3] += random.randrange(5, 20)
                plr1[len(plr1)-1] += plr1[int(percNum)][3]
                if plr2[int(attackNum)][3] > 0:
                    if plr2[int(attackNum)][3] <= 0:
                        plr1[len(plr1)-1] += plr2[int(attackNum)][4]
                        plr1[int(percNum)][5] += 0.5
                print(f"Tower {plr2[int(attackNum)][0]} Now have {plr2[int(attackNum)][3]} HP")
            else:
                print(f"Tower {plr2[int(attackNum)][0]} already died")
        elif plr1[int(percNum)][0] == "Gladiator":
            if plr2[int(attackNum)][3] > 0:
                plr2[int(attackNum)][3] -= random.randrange(plr1[int(percNum)][4] - 10, plr1[int(percNum)][4] + 10) * plr1[int(percNum)][5]
                plr1[len(plr1)-1] += plr1[int(percNum)][3]
                if plr2[int(attackNum)][3] > 0:
                    if plr2[int(attackNum)][3] <= 0:
                        plr1[len(plr1)-1] += plr2[int(attackNum)][4]
                        plr1[int(percNum)][5] += 0.5
                    print(f"Tower {plr2[int(attackNum)][0]} Now have {plr2[int(attackNum)][3]} HP")
                else:
                    print(f"Tower {plr2[int(attackNum)][0]} already died")
            else:
                print(f"Tower {plr2[int(attackNum)][0]} already died")
        elif plr1[int(percNum)][0] == "Rocketman":
            if plr2[int(attackNum)][3] > 0:
                plr2[int(attackNum)][3] -= plr1[int(percNum)][4] * plr1[int(percNum)][5]
                for f in range(random.randrange(1, 2)):
                    streep.append([random.randrange(1, 10), random.randrange(1, 10)])
                plr1[len(plr1)-1] += plr1[int(percNum)][3]
                if plr2[int(attackNum)][3] > 0:
                    if plr2[int(attackNum)][3] <= 0:
                        plr1[len(plr1)-1] += plr2[int(attackNum)][4]
                        plr1[int(percNum)][5] += 0.5
                print(f"Tower {plr2[int(attackNum)][0]} Now have {plr2[int(attackNum)][3]} HP")
            else:
                print(f"Tower {plr2[int(attackNum)][0]} already died")
        elif plr1[int(percNum)][0] == "Guard":
            if plr2[int(attackNum)][3] > 0:
                plr2[int(attackNum)][3] -= random.randrange(plr1[int(percNum)][4], plr1[int(percNum)][4]+30) * plr1[int(percNum)][5]
                streep.append([random.randrange(1, 10), random.randrange(1, 10)])
                plr1[len(plr1)-1] += plr1[int(percNum)][3]
                if plr2[int(attackNum)][3] > 0:
                    if plr2[int(attackNum)][3] <= 0:
                        plr1[len(plr1)-1] += plr2[int(attackNum)][4]
                        plr1[int(percNum)][5] += 0.5
                print(f"Tower {plr2[int(attackNum)][0]} Now have {plr2[int(attackNum)][3]} HP")
            else:
                print(f"Tower {plr2[int(attackNum)][0]} already died")
        elif plr1[int(percNum)][0] == "Turrel":
            for f in range(random.randrange(2, 4)):
                if plr2[int(attackNum)][3] > 0:
                    plr2[int(attackNum)][7] = False
                    plr2[int(attackNum)][3] -= plr1[int(percNum)][4] * plr1[int(percNum)][5]
                    plr1[len(plr1)-1] += plr1[int(percNum)][3]
                    if plr2[int(attackNum)][3] > 0:
                        if plr2[int(attackNum)][3] <= 0:
                            plr1[len(plr1)-1] += plr2[int(attackNum)][4]
                            plr1[int(percNum)][5] += 0.5
                        print(f"Tower {plr2[int(attackNum)][0]} Now have {plr2[int(attackNum)][3]} HP")
                    else:
                        print(f"Tower {plr2[int(attackNum)][0]} already died")
                else:
                    print(f"Tower {plr2[int(attackNum)][0]} already died")
        elif plr1[int(percNum)][0] == "Gun":
            if plr2[int(attackNum)][3] > 0:
                plr2[int(attackNum)][3] -= random.randrange(plr1[int(percNum)][4], plr1[int(percNum)][4]+30) * plr1[int(percNum)][5]
                plr1[len(plr1)-1] += plr1[int(percNum)][3]
                plr1[int(percNum)][4] += 5
                if plr2[int(attackNum)][3] > 0:
                    if plr2[int(attackNum)][3] <= 0:
                        plr1[int(percNum)][4] += 5
                        plr1[len(plr1)-1] += plr2[int(attackNum)][4]
                        plr1[int(percNum)][5] += 0.5
                print(f"Tower {plr2[int(attackNum)][0]} Now have {plr2[int(attackNum)][3]} HP")
            else:
                print(f"Tower {plr2[int(attackNum)][0]} already died")
        elif plr1[int(percNum)][0] == "SwordMan":
            if plr2[int(attackNum)][3] > 0:
                plr2[int(attackNum)][3] -= random.randrange(plr1[int(percNum)][4], plr1[int(percNum)][4]+30) * plr1[int(percNum)][5]
                plr2[int(attackNum)][7] = False
                plr1[len(plr1)-1] += plr1[int(percNum)][3]
                plr1[int(percNum)][4] += 5
                if plr2[int(attackNum)][3] > 0:
                    if plr2[int(attackNum)][3] <= 0:
                        plr1[int(percNum)][4] += 5
                        plr1[len(plr1)-1] += plr2[int(attackNum)][4]
                        plr1[int(percNum)][5] += 0.5
                print(f"Tower {plr2[int(attackNum)][0]} Now have {plr2[int(attackNum)][3]} HP")
            else:
                print(f"Tower {plr2[int(attackNum)][0]} already died")
    else:
        print(f"Your Tower {plr1[int(percNum)][0]} already died!")
def attack():
    if plr1[int(percNum)][7] == True and plr1[int(percNum)][3] > 0 and plr1[int(percNum)][10] == False:
        for i in range(3):
            if plr1[int(percNum)][1] - plr2[int(attackNum)][1] == i+1 or plr2[int(attackNum)][1] - plr1[int(percNum)][1] == i+1 and plr1[int(percNum)][2] == plr1[int(percNum)][2]:
                attackActive()
            elif plr1[int(percNum)][2] - plr2[int(attackNum)][2] == i+1 or plr2[int(attackNum)][2] - plr1[int(percNum)][2] == i+1 and plr1[int(percNum)][1] == plr1[int(percNum)][1]:
                attackActive()
    else:
        print("Now tower can't attack")
def step():
    global canStep
    canStep = True
    if 10 > int(tohodNumX) > 0 and 10 > int(tohodNumY) > 0:
        if plr1[int(hodNum)][3] > 0:
            for s in range(len(plr2)-1):
                if plr2[s][1] == int(tohodNumX) and plr2[s][2] == int(tohodNumY):
                    canStep = False
                    print(f"On cage X {tohodNumX}, Y {tohodNumY} is located other tower")
                if plr1[s][1] == int(tohodNumX) and plr1[s][2] == int(tohodNumY):
                    canStep = False
                    print(f"On cage X {tohodNumX}, Y {tohodNumY} is located other tower")
            if not plr1[int(hodNum)][7]:
                canStep = False
                print(f"Tower {plr1[int(hodNum)][0]} is not purchased!")
            if plr1[int(hodNum)][10]:
                canStep = False
                print(f"Tower {plr1[int(hodNum)][0]} is stun!")
            if canStep:
                for m in range(plr1[int(hodNum)][9]):
                    f = plr1[int(hodNum)][9]-m
                    if f == plr1[int(hodNum)][1]-int(tohodNumX) == 1 or f == int(tohodNumX)-plr1[int(hodNum)][1] and plr1[int(hodNum)][2] == int(tohodNumY):
                        for v in range(len(streep)):
                            if int(tohodNumX) == streep[v][0] and int(tohodNumY) == streep[v][1]:
                                plr1[int(hodNum)][3] -= 40
                                print(f"Tower {plr1[int(hodNum)][0]} step in trap! Now tower have {plr1[int(hodNum)][3]} HP")
                        plr1[int(hodNum)][1] = int(tohodNumX)
                        print(f"Now {plr1[int(hodNum)][0]} on {plr1[int(hodNum)][1]} X, {plr1[int(hodNum)][2]} Y")
                    elif f == plr1[int(hodNum)][2]-int(tohodNumY) or int(tohodNumY)-plr1[int(hodNum)][2] == f and plr1[int(hodNum)][1] == int(tohodNumX):
                        for v in range(len(streep)):
                            if int(tohodNumX) == streep[v][0] and int(tohodNumY) == streep[v][1]:
                                plr1[int(hodNum)][3] -= 40
                                print(f"Tower {plr1[int(hodNum)][0]} step in trap! Now tower have {plr1[int(hodNum)][3]} HP")
                        plr1[int(hodNum)][2] = int(tohodNumY)
                        print(f"Now {plr1[int(hodNum)][0]} on {plr1[int(hodNum)][1]} X, {plr1[int(hodNum)][2]} Y")
def health():
    if plr1[int(healthNum)][7]:
        if plr1[int(healthNum)][3] > 0:
            plr1[int(healthNum)][3] += 75
            print(f"Now {plr1[int(healthNum)][0]} Tower have {plr1[int(healthNum)][3]} HP")
        else:
            print("This tower already died!")
    else:
        print("Tower is not purchased")
plrs = [[["Eye", 1, 1, 200, 60, 1, 30, False, 50, 2, False],["Tank", 2, 1, 105, 20, 1, 15, True, 0, 2, False],["SwordMan", 3, 1, 105, 20, 1, 20, True, 0, 2, False],["Arrowman", 4, 1, 90, 45, 1, 15, True, 0, 2, False], ["Gladiator", 5, 1, 100, 40, 1, 10, True, 0, 2, False], ["Gun", 6, 1, 100, 50, 1, 1, False, 250, 3, False], ["Turrel", 7, 1, 120, 70, 1, 1, False, 450, 2, False], ["Guard", 8, 1, 110, 30, 1, 1, False, 600, 3, False], ["Rocketman", 9, 1, 125, 75, 1, 1, False, 150, 4, False], ["Rocketman", 10, 1, 125, 75, 1, 1, False, 150, 4, False], 0], [["Eye", 1, 10, 200, 60, 1, 30, False, 50, 2, False],["Tank", 2, 10, 105, 20, 5, 15, True, 0, 2, False],["SwordMan", 3, 10, 105, 20, 1, 20, True, 0, 2, False],["Arrowman", 4, 10, 90, 45, 1, 15, True, 0, 2, False], ["Gladiator", 5, 10, 100, 50, 1, 10, True, 0, 2, False], ["Gun", 6, 10, 100, 50, 1, 1, False, 250, 3, False], ["Turrel", 7, 10, 120, 70, 1, 1, False, 450, 2, False], ["Guard", 8, 10, 110, 30, 1, 1, False, 600, 3, False], ["Rocketman", 9, 10, 125, 75, 1, 1, False, 150, 4, False], ["Rocketman", 10, 10, 125, 75, 1, 1, False, 150, 4, False], 0]]
stepNum = 1
plr1 = plrs[0]
plr2 = plrs[1]

streep = []
for b in range(random.randrange(2, 5)):
    streep.append([random.randrange(1, 10), random.randrange(1, 10)])
def towers():
    print("Your Towers:\n")
    for s in range(len(plr1)-1):
        if plr1[s][7]:
            print(f"{plr1[s][0]} - {s}, Have {plr1[s][3]} HP, Stun: {plr1[s][10]}")
        else:
            print(f"[Buy {plr1[s][8]}$] {plr1[s][0]} - {s}, Have {plr1[s][3]} HP, Stun: {plr1[s][10]}")
    print("\nPlayer 2 Towers:\n")
    for s in range(len(plr1)-1):
        if plr1[s][7]:
            print(f"{plr1[s][0]} - {s}, Have {plr1[s][3]} HP, Stun: {plr1[s][10]}")
        else:
            print(f"[Buy {plr1[s][8]}$] {plr1[s][0]} - {s}, Have {plr1[s][3]} HP, Stun: {plr1[s][10]}")

def buy_tower():
    if plr1[len(plr1)-1] >= plr1[int(buynum)][8]:
        if not plr1[int(buynum)][7]:
            plr1[len(plr1) - 1] -= plr1[int(buynum)][8]
            plr1[int(buynum)][7] = True
            print(f"Tower {plr1[int(buynum)][0]} is successfully purchased!")
        else:
            print("Tower already purchased!")
    else:
        print(f"You have < {plr1[int(buynum)][8]}$")
def buy_towers_print():
    for s in range(len(plr1)-2):
        if not plr1[s][7]:
            print(f"[Buy {plr1[s][8]}$] {plr1[s][0]} Tower - Number: {s}, HP: {plr1[s][3]}, Damage: {plr1[s][4]}, Reload Time: {plr1[s][6]}, Stun: {plr1[s][10]}")
def statistic():
    print("\nYour Towers statistic")
    for s in range(len(plr1)-1):
        if plr1[s][3] > 0:
            if plr1[s][7]:
                print(f"{plr1[s][0]} Tower - Number: {s}, HP: {plr1[s][3]}, Damage: {plr1[s][4]}, Reload Time: {plr1[s][6]}, Stun: {plr1[s][10]}")
            else:
                print(f"[Buy {plr1[s][8]}$] {plr1[s][0]} Tower - Number: {s}, HP: {plr1[s][3]}, Damage: {plr1[s][4]}, Reload Time: {plr1[s][6]}, Stun: {plr1[s][10]}")
        else:
            print(f"{plr1[s][0]} Tower already died!")
    print(f"You have {plr1[len(plr1)-1]}$ cash")
while True:
    skip = input("Attack/Walk/Health/Statistic/Buy Tower >>> ")
    if stepNum == 1:
        stepNum = 2
        plr1 = plrs[0]
        plr2 = plrs[1]
    else:
        stepNum = 1
        plr1 = plrs[1]
        plr2 = plrs[0]
    if skip is not None:
        if skip == "Attack":
            towers()
            percNum = input("\nYour tower >>> ")
            attackNum = input("Player 2 attack tower >>> ")
            attack()
        elif skip == "Walk":
            towers()
            hodNum = input("\nWalk Tower >>> ")
            tohodNumX = input("Walk to X >>> ")
            tohodNumY = input("Walk to Y >>> ")
            step()
        elif skip == "Health":
            towers()
            healthNum = input("\nHealth Tower >>> ")
            health()
        elif skip == "Statistic":
            statistic()
        elif skip == "Buy Tower":
            buy_towers_print()
            buynum = input("\nTower Buy >>> ")
            buy_tower()
        else:
            print("Step is not found!")
    for n in range(len(plr1) - 2):
        if plr1[n][10]:
            plr1[n][10] = False
        if plr2[n][10]:
            plr2[n][10] = False