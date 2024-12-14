with open("data.txt") as f:
    rules_str, updates_str = f.read().split("\n\n")

rules_str, updates_str = rules_str.splitlines(), updates_str.splitlines()

rules = [list(map(int, item.split("|"))) for item in rules_str]
updates = [list(map(int, item.split(","))) for item in updates_str]

def check_update(update):

    return False

def check_updates(updates):
    for update in updates:
        check_update(update)


print(rules, updates)
