import numpy as np

def enrollment_stats(univ):
    student_enrollment_values = [e[1] for e in univ]
    annual_tuition_fees = [a[2] for a in univ]
    return (student_enrollment_values, annual_tuition_fees)


def mean(mylist):
    return np.mean(mylist)


def median(mylist):
    return np.median(mylist)


universities = [
    ["California Institute of Technology", 2175, 37704],
    ["Harvard", 19627, 39849],
    ["Massachusetts Institute of Technology", 10566, 40732],
    ["Princeton", 7802, 37000],
    ["Rice", 5879, 35551],
    ["Stanford", 19535, 40569],
    ["Yale", 11701, 40500],
]
student_tuition_list = enrollment_stats(universities)

print("******" * 6)
print(f"Total students: {sum(student_tuition_list[0]):,}")
print(f"Total tution: $ {sum(student_tuition_list[1]):,}", end="\n")

print(f"Student mean: {mean(student_tuition_list[0]):,.2f}")
print(f"Student median: {median(student_tuition_list[0]):,.0f}", end="\n")

print(f"Tuition mean: $ {mean(student_tuition_list[1]):,.2f}")
print(f"Tuition median: $ {median(student_tuition_list[1]):,.0f}")
print("******" * 6)
