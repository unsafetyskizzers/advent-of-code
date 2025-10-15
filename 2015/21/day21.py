boss_base = {"hp": 104, "damage": 8, "armor": 1}
player_base = {"hp": 100, "damage": 0, "armor": 0}
inventory = [0, 0, 0]

shop_weapons = [
    {"cost": 0, "damage": 0, "armor": 0},
    {"cost": 8, "damage": 4, "armor": 0},
    {"cost": 10, "damage": 5, "armor": 0},
    {"cost": 25, "damage": 6, "armor": 0},
    {"cost": 40, "damage": 7, "armor": 0},
    {"cost": 74, "damage": 8, "armor": 0}
]

shop_armors = [
    {"cost": 0, "damage": 0, "armor": 0},
    {"cost": 13, "damage": 0, "armor": 1},
    {"cost": 31, "damage": 0, "armor": 2},
    {"cost": 53, "damage": 0, "armor": 3},
    {"cost": 75, "damage": 0, "armor": 4},
    {"cost": 102, "damage": 0, "armor": 5},
]

shop_rings = [
    {"cost": 0, "damage": 0, "armor": 0},
    {"cost": 20, "damage": 0, "armor": 1},
    {"cost": 25, "damage": 1, "armor": 0},
    {"cost": 40, "damage": 0, "armor": 2},
    {"cost": 50, "damage": 2, "armor": 0},
    {"cost": 80, "damage": 0, "armor": 3},
    {"cost": 100, "damage": 3, "armor": 0},
]

shops = [shop_weapons, shop_armors, shop_rings]

def cheapest_upgrade(inv):
    cheapest_upgrade = [0, 0, 0]
    cheapest_upgrade_cost = 999999
    for i in range(len(inv)):
        if shops[i][inv[i]+1]["cost"] - shops[i][inv[i]]["cost"] < cheapest_upgrade_cost:
            cheapest_upgrade = [0, 0, 0]
            cheapest_upgrade[i] = 1
            cheapest_upgrade_cost = shops[i][inv[i]+1]["cost"] - shops[i][inv[i]]["cost"]
    for i in range(3):
        inv[i] += cheapest_upgrade[i]
    print("Bought", cheapest_upgrade, "with", cheapest_upgrade_cost, "more gold")
    return inv

def highest_ratio(inv):
    h_ratio = 0

def simulate_battle():
    player_boosted = {"hp": 100, "damage": 0, "armor": 0}
    boss_sim = {"hp": 104, "damage": 8, "armor": 1}
    turn = 1
    for i in range(len(inventory)):
        player_boosted["damage"] += shops[i][inventory[i]]["damage"]
        player_boosted["armor"] += shops[i][inventory[i]]["armor"]
    while player_boosted["hp"] > 0 and boss_sim["hp"] > 0:
        boss_sim["hp"] -= max(player_boosted["damage"] - boss_base["armor"], 1)
        player_boosted["hp"] -= max(boss_base["damage"] - player_boosted["armor"], 1)
        print("Turn", turn, "Boss HP:", boss_sim["hp"], "Player HP:", player_boosted["hp"])
        turn += 1
    if player_boosted["hp"] > 0: print("Player wins")
    else: print("Boss wins")
    return player_boosted["hp"] > 0

while True:
    inventory = cheapest_upgrade(inventory)
    if simulate_battle():
        break

inventory_cost = 0
for i in range(len(inventory)):
    inventory_cost += shops[i][inventory[i]]["cost"]

print("Inventory cost:", inventory_cost, "Inventory:", inventory)
# this answer is wrong! TODO check for highest stat point to gold ratio instead of cheapest upgrade in new algorithm