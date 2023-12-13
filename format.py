import re

name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.groups(2) + " " + matches.groups(1)

print(f"Hello, {name}!")

# # #

# if matches:
#     last, first = matches.groups()
#     name = f"{first} {last}"

# print(f"Hello, {name}!")

# # #

# if "," in name:
#     last, first = name.split(", ")
#     name = f"{first} {last}"

# print(f"Hello, {name}!")
