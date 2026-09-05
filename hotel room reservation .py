# hotel room reservations :
name = input("Enter customer name: ")

single_rooms = 5
double_rooms = 3

print("Single rooms available:", single_rooms)
print("Double rooms available:", double_rooms)

room = input("Enter room type (single/double): ")
days = int(input("Enter number of days: "))

if room == "single":
    if single_rooms > 0:
        price = 1500
        single_rooms -= 1
        print("Room available")
    else:
        price = 0
        print("Single room not available")

elif room == "double":
    if double_rooms > 0:
        price = 2500
        double_rooms -= 1
        print("Room available")
    else:
        price = 0
        print("Double room not available")

else:
    price = 0
    print("Invalid room type")

if price > 0:
    total = price * days

    print("Customer:", name)
    print("Room:", room)
    print("Days:", days)
    print("Total bill:", total)
    print("Booking confirmed")
    print("Remaining single rooms:", single_rooms)
    print("Remaining double rooms:", double_rooms)

