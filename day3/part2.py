import re

with open("data.txt") as f:
    my_input = f.read()

pattern = r"(mul\((\d{1,3}),(\d{1,3})\))|(don\'t\(\))|(do\(\))"
matches = re.finditer(pattern, my_input)

result = 0
enabled = True

for match in matches:
    if match.group(4):
        enabled = False
        continue
    elif match.group(5):
        enabled = True
        continue
    if enabled:
        result += int(match.group(2)) * int(match.group(3))
    print(match, enabled)

print(result)