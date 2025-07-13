Days = set(["Mon", 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'])


def printdays():
    for d in Days:
        print(d)
    print()


Days.add("Sun")
printdays()

Days.discard("Tue")
printdays()

DaysA = set(["Mon", "Tue", "Wed"])
DaysB = set(["Wed", "Thu", "Fri", "Sat", "Sun"])
AllDays = DaysA | DaysB
print(AllDays)
AllDays = DaysA & DaysB
print(AllDays)

AllDays = DaysA - DaysB
print(AllDays)

DaysA = set(["Mon", "Tue", "Wed"])
DaysB = set(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
subset = DaysA <= DaysB
superset = DaysA <= DaysB

print(subset)
print(superset)
