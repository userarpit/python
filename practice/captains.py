captains_dict = {}

captains_dict["Enterprise"] = "Picard"
captains_dict["Voyager"] = "Janeway"
captains_dict["Defiant"] = "Sisko"

if "Enterprise" in captains_dict:
    pass
else:
    captains_dict["Enterprise"] = "Unknown"

if "Discovery" in captains_dict:
    pass
else:
    captains_dict["Discovery"] = "Unknown"

print(captains_dict)

for ship, captain_name in captains_dict.items():
    print(f"The {ship} is captained by {captain_name}")

del captains_dict['Discovery']

print(captains_dict)

key_value_pair = (("Enterprise","Picard"),("Voyager","Janeway"),("Defiant","Sisko"))

captains_dict = dict(key_value_pair)
print(captains_dict)
