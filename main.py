import time
import random
def attackActive():
    if plr1[int(percNum)][0] == "Turrel":
        for f in range(random.randrange(1, 5)):
            if plr2[int(attackNum)][3] > 0:
                plr2[int(attackNum)][3] -= plr1[int(percNum)][4] * plr1[int(percNum)][5]
                plr1[len(plr1)-1] += plr1[int(percNum)][3]
                if plr2[int(attackNum)][3] > 0:
                    if plr2[int(attackNum)][3] <= 0:
                        plr1[len(plr1) - 1] += plr2[int(attackNum)][4]
                        plr1[int(percNum)][5] += 0.5
                    print(f"Tower {plr2[int(attackNum)][0]} Now have {plr2[int(attackNum)][3]} HP")
                else:
                    print(f"Tower {plr2[int(attackNum)][0]} already died")
            else:
                print(f"Tower {plr2[int(attackNum)][0]} already died")
    elif plr1[int(percNum)][0] == "Arrowman":
        for f in range(random.randrange(1, 2)):
            plr2[int(attackNum)][3] -= random.randrange(plr1[int(percNum)][4]-50, plr1[int(percNum)][4]+50) * plr1[int(percNum)][5]
            if plr2[int(attackNum)][3] > 0:
                if plr2[int(attackNum)][3] <= 0:
                    plr1[int(percNum)][5] += 0.5
                print(f"Tower {plr2[int(attackNum)][0]} Now have {plr2[int(attackNum)][3]} HP")
            else:
                print(f"Tower {plr2[int(attackNum)][0]} already died")
    elif plr1[int(percNum)][0] == "Dragon":
            if plr2[int(attackNum)][3] > 0:
                plr2[int(attackNum)][3] -= plr1[int(percNum)][4] * plr1[int(percNum)][5]
                plr1[int(percNum)][3] += random.randrange(5, 15)
                if plr2[int(attackNum)][3] <= 0:
                    plr1[int(percNum)][3] += random.randrange(20, 40)
                    plr1[int(percNum)][5] += 0.5
                print(f"Tower {plr2[int(attackNum)][0]} Now have {plr2[int(attackNum)][3]} HP")
            else:
                print(f"Tower {plr2[int(attackNum)][0]} already died")
    elif plr1[int(percNum)][0] == "Gladiator":
        if plr2[int(attackNum)][3] > 0:
            plr2[int(attackNum)][3] -= random.randrange(plr1[int(percNum)][4], plr1[int(percNum)][4]+10) * plr1[int(percNum)][5]
            if plr2[int(attackNum)][3] > 0:
                if plr2[int(attackNum)][3] <= 0:
                    plr1[int(percNum)][5] += 0.5
                print(f"Tower {plr2[int(attackNum)][0]} Now have {plr2[int(attackNum)][3]} HP")
            else:
                print(f"Tower {plr2[int(attackNum)][0]} already died")
        else:
            print(f"Tower {plr2[int(attackNum)][0]} already died")
def attack():
    if plr1[int(percNum)][7] == True and plr1[int(percNum)][3] > 0:
        for i in range(3):
            if plr1[int(percNum)][1] - plr2[int(attackNum)][1] == i+1 or plr2[int(attackNum)][1] - plr1[int(percNum)][1] == i+1 and plr1[int(percNum)][2] == plr1[int(percNum)][2]:
                attackActive()
            elif plr1[int(percNum)][2] - plr2[int(attackNum)][2] == i+1 or plr2[int(attackNum)][2] - plr1[int(percNum)][2] == i+1 and plr1[int(percNum)][1] == plr1[int(percNum)][1]:
                attackActive()

def step():
    global canStep
    canStep = True
    if 10 > int(tohodNumX) > 0 and 10 > int(tohodNumY) > 0:
        if plr1[int(hodNum)][3] > 0:
            for s in range(len(plr2) - 1):
                if plr2[s][1] == int(tohodNumX) and plr2[s][2] == int(tohodNumY):
                    canStep = False
                if plr1[s][1] == int(tohodNumX) and plr1[s][2] == int(tohodNumY):
                    canStep = False
            if canStep:
                for f in range(2):
                    if plr1[int(hodNum)][1]-int(tohodNumX) == 1 or int(tohodNumX)-plr1[int(hodNum)][1] and plr1[int(hodNum)][2] == int(tohodNumY):
                        plr1[int(hodNum)][1] = int(tohodNumX)
                        print(f"Now {plr1[int(hodNum)][0]} on {plr1[int(hodNum)][1]} X, {plr1[int(hodNum)][2]} Y")
                    elif plr1[int(hodNum)][2]-int(tohodNumY) == 1 or int(tohodNumY)-plr1[int(hodNum)][2] and plr1[int(hodNum)][1] == int(tohodNumX):
                        plr1[int(hodNum)][2] = int(tohodNumY)
                        print(f"Now {plr1[int(hodNum)][0]} on {plr1[int(hodNum)][1]} X, {plr1[int(hodNum)][2]} Y")
            else:
                print(f"On cage X {tohodNumX}, Y {tohodNumY} is located other tower")
def health():
    if plr1[int(healthNum)][3] > 0:
        plr1[int(healthNum)][3] += 75
        print(f"Now {plr1[int(healthNum)][0]} Tower have {plr1[int(healthNum)][3]} HP")
    else:
        print("This tower already died!")

def upgrade():
    if plr1[len(plr1)-1] >= plr1[upgrNum][3]*2:
        plr1[len(plr1)-1] -= plr1[upgrNum][3]
        plr1[upgrNum][3] += plr1[upgrNum][3]/2
        plr1[upgrNum][7] += 0.5

# Tower: [0] Name, [1] X, [2] Y, [3] Health, [4] Attack, [5] MultiplyAttack [6] Reload [7] Can Attack
# Player: [5] Cash
plr1 = [["Dragon", 1, 1, 200, 60, 1, 30, True, 0],["Turrel", 2, 1, 105, 20, 1, 15, True, 0],["Turrel", 3, 1, 105, 20, 1, 20, True, 0],["Arrowman", 4, 1, 90, 45, 1, 15, True, 0], ["Gladiator", 5, 1, 100, 50, 1, 10, True, 0], ["Engineer", 6, 1, 200, 70, 1, 1, False, 250], 0]
plr2 = [["Dragon", 1, 5, 200, 60, 1, 30, True, 0],["Turrel", 2, 5, 105, 20, 5, 15, True, 0],["Turrel", 3, 5, 105, 20, 1, 20, True, 0],["Arrowman", 4, 5, 90, 45, 1, 15, True, 0], ["Gladiator", 5, 5, 100, 50, 1, 10, True, 0], ["Engineer", 6, 5, 200, 70, 1, 1, False, 250], 0]
def towers():
    print("Your Towers:\n")
    for s in range(len(plr1)-2):
        if plr1[s][0] != "Engineer":
            print(f"{plr1[s][0]} - {s}, Have {plr1[s][3]} HP")
        else:
            if not plr1[s][7]:
                print(f"[Buy 700$] {plr1[s][0]} - {s}, Have {plr1[s][3]} HP")
            else:
                print(f"{plr1[s][0]} - {s}, Have {plr1[s][3]} HP")
    print("\nTowers:\n")
    for s in range(len(plr1)-2):
        print(f"{plr2[s][0]} - {s}, Have {plr2[s][3]} HP")

def buy_tower():
    if plr1[len(plr1)-1] >= plr1[buynum][8]:
        plr1[len(plr1) - 1] -= plr1[buynum][8]
        plr1[buynum][7] = True
        print(f"Tower {plr1[buynum][0]} is successfully purchased!")
    else:
        print(f"You have < {plr1[buynum][8]}$")

def statistic():
    print("\nYour Towers statistic")
    for s in range(5):
        if plr1[s][3] > 0:
            if plr1[s][0] != "Engineer":
                print(f"{plr1[s][0]} Tower - Number: {s}, HP: {plr1[s][3]}, Damage: {plr1[s][4]}, Reload Time: {plr1[s][6]}")
            else:
                if not plr1[s][7]:
                    print(f"[Buy 700$] {plr1[s][0]} Tower - Number: {s}, HP: {plr1[s][3]}, Damage: {plr1[s][4]}, Reload Time: {plr1[s][6]}")
                else:
                    print(f"{plr1[s][0]} Tower - Number: {s}, HP: {plr1[s][3]}, Damage: {plr1[s][4]}, Reload Time: {plr1[s][6]}")
        else:
            print(f"{plr1[s][0]} Tower already died!")

    print(f"You have {plr1[len(plr1)-1]} cash")

while True:
    skip = input("Attack/Walk/Health/Upgrade/Statistic/Buy Tower >>> ")
    if skip == "Attack":
        towers()
        percNum = input("\nYour attack tower >>> ")
        attackNum = input("On attack tower >>> ")
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
    elif skip == "Upgrade":
        towers()
        upgrNum = input("\nUpgrade Tower >>> ")
        upgrade()
    elif skip == "Statistic":
        statistic()
    elif skip == "Buy Tower":
        towers()
        buynum = input("\nTower Buy >>> ")
        buy_tower()
    else:
        print("Step is not found!")
