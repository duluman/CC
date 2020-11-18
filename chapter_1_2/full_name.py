

first_name = "Cristian"
last_name = "Duluman"

full_name = f"{first_name} {last_name}"  # f-strings

print(full_name)

message = f"Hello, {full_name}"

print(message)

full_name_v2 = "{} {} v2".format(first_name, last_name)

print(full_name_v2)


full_name_v3 = "{a} {b} v3".format(a=first_name, b=last_name)

print(full_name_v3)


number = 23

print(f"My favorite number is: {number}")
