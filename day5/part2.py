with open("data.txt") as f:
    rules_str, updates_str = f.read().split("\n\n")

rules_str, updates_str = rules_str.splitlines(), updates_str.splitlines()

rules = [list(map(int, item.split("|"))) for item in rules_str]
updates = [list(map(int, item.split(","))) for item in updates_str]

# Logic


def sort_update(update):
    print(update)
    while not check_update(update):
        for rule in rules:
            if all(item in update for item in rule):
                index1, index2 = update.index(rule[0]), update.index(rule[1])
                if index1 > index2:
                    update[index1], update[index2] = rule[1], rule[0]
    return update

def check_update(update):
    return not any(
        rule[0] in update and rule[1] in update and update.index(rule[0]) > update.index(rule[1])
        for rule in rules
    )

result = sum(
    update[len(update) // 2]
    for update in updates
    if check_update(update)
)

result2 = sum(
    sort_update(update)[len(update) // 2]
    for update in updates
    if not check_update(update)
)

print(result2)
