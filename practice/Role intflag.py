from enum import IntFlag, Flag


class Role(IntFlag):
    OWNER = 8
    POWER_USER = 4
    USER = 2
    SUPERVISOR = 1
    ADMIN = OWNER | POWER_USER | USER | SUPERVISOR


print(Role.ADMIN.value)
print(Role.OWNER in Role.ADMIN)
print(Role.SUPERVISOR + 10)
