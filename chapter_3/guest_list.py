

guests = ["Tonny Robbins", "Robin Sharma", "Paulo Coelho"]

message = f"Dear {guests[0]}, you are most cordially invited to be our guest at the dinner party we have arranged"

print(message)

message = f"Sir {guests[1]}, it will be great having you among us! We are going to arrange a dinner party at our sweet home"

print(message)

message = f"{guests[2]}, we invite you to share dinner with us"

print(message)

guests[0] = "Dan Puric"

for guest in guests:
    print(f"Dear, {guest} you are invited tonight to the dinner.")

guests.insert(0, "Tudor Gheorghe")  # add one new guest to the beginning of your list
guests.insert(2, "Thierry Henry")  # add one new guest to the middle of your list.
guests.append("Bob Proctor")  ## add one new guest to the end of your list.

print(guests)