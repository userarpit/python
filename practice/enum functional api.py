from enum import Enum

# @unique
HTTPStatusCode = Enum(
    value="HTTPStatusCode",
    names=[("OK",200),
         ("CREATED", 201),
         ("BAD_REQUEST", 400),
         ("NOT_FOUND", 404),
         ("SERVER_ERROR", 200),
        ],
)

print(list(HTTPStatusCode.__members__.items()))