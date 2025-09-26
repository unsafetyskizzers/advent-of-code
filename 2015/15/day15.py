file = open("2015/15/input.txt", "r")
input = file.readlines()
file.close()

ingredients = {}
for line in input:
    command = line.split()
    ingredients[command[0].strip(":")] = {}
    for i in range(1, len(command), 2):
        ingredients[command[0].strip(":")][command[i]] = int(command[i+1].strip(","))

highest_score = 0
best_cookie = []

for sugar_amt in range(0, 101):
    for sprinkles_amt in range(0, 101 - sugar_amt):
        for candy_amt in range(0, 101 - sugar_amt - sprinkles_amt):
            choco_amt = 100 - sugar_amt - sprinkles_amt - candy_amt
            amounts = [sugar_amt, sprinkles_amt, candy_amt, choco_amt]
            curr_cookie_score = 1
            calorie_count = 0
            for component in list(ingredients["Sugar"].keys()):
                if component != "calories":
                    component_score = 0
                    for i in range(4):
                        component_score += ingredients[list(ingredients.keys())[i]][component] * amounts[i]
                    if component_score < 0: component_score = 0
                    curr_cookie_score *= component_score
            if curr_cookie_score > highest_score:
                for i in range(4):
                    calorie_count += ingredients[list(ingredients.keys())[i]]["calories"] * amounts[i]
                if calorie_count == 500:
                    highest_score = curr_cookie_score
                    best_cookie = [sugar_amt, sprinkles_amt, candy_amt, choco_amt]

print(highest_score, best_cookie)
                