with open("data.txt") as f:
    rules_str, updates_str = f.read().split("\n\n")

rules_str, updates_str = rules_str.splitlines(), updates_str.splitlines()

rules = [list(map(int, item.split("|"))) for item in rules_str]
updates = [list(map(int, item.split(","))) for item in updates_str]

# Logic


def check_update(update):
    return not any(
        rule[0] in update and rule[1] in update and not update.index(rule[0]) < update.index(rule[1])
        for rule in rules
    )
    # return sum(
    #     False
    #     for rule in rules
    #     if rule[0] in update and rule[1] in update
    #     if not update.index(rule[0]) < update.index(rule[1])
    # )
    # for rule in rules:
    #     if rule[0] in update and rule[1] in update:
    #         if not update.index(rule[0]) < update.index(rule[1]):
    #             return False
    # return True

result = sum(
    update[len(update) // 2]
    for update in updates
    if check_update(update)
)

print(check_update(updates[3]))
print(result)
