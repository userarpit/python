file = "techcrunch - Copy.csv"

lines = (line for line in open(file, mode="r"))
# col = nex

list_line = (s.rstrip().split(",") for s in lines)

col = next(list_line)
print(col)

company_dicts = (dict(zip(col, data)) for data in list_line)

# funding = (
#     int(company_dict["raisedAmt"])
#     for company_dict in company_dicts
#     if company_dict["round"] == "a"
# )

# total_series_a = sum(funding)
# print(f"Total series A fundraising: ${total_series_a:,}")

# for a in company_dicts:
#     print(a)

company_round_a_dict = (
    {company_dict["company"]: company_dict["raisedAmt"]}
    for company_dict in company_dicts
    if company_dict["round"] == "a"
)

# for a in company_round_a_dict:
#     for k, v in a.items():
#         print(k)

average_round_a_dict = {}

for company_a in company_round_a_dict:
    for key, value in company_a.items():

        if key not in average_round_a_dict:
            average_round_a_dict[key] = [0, 0]

        average_round_a_dict[key][0] = average_round_a_dict[key][0] + int(value)
        average_round_a_dict[key][1] = average_round_a_dict[key][1] + 1


# print(average_round_a_dict["Earth Class Mail"])

for key, value in average_round_a_dict.items():
    print(
        f"Average amount raised for the company {key} - {float(value[0] / value[1]):.2f} "
    )
