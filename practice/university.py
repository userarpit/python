from typing import List

universities = [
    ["California Institute of Technology", 2175, 37704],
    ["Harvard", 19627, 39849],
    ["MIT", 10566, 40732],
    ["Priceton", 7802, 37000],
    ["Rice", 5879, 35551],
    ["Stanford", 19535, 40569],
    ["Yale", 11701, 40500],
]


def enrollment_stats(universities):
    total_student = []
    total_tuition = []
    for u in universities:
        total_student.append(u[1])
        total_tuition.append(u[2])

    return (total_student, total_tuition)


def mean(mean_list: List[float]) -> float:
    """Calculate the mean of a list of numbers.

    Args:
        mean_list: A list of numbers.

    Returns:
        The mean of the list of numbers.
    """
    return sum(mean_list) / len(mean_list)


def median(median_list):
    median_list.sort()
    if len(median_list) % 2 == 1:
        center_index = int(len(median_list) / 2)
        return median_list[center_index]
    else:
        # list has even number of elements, 8
        # get middle 2
        left_center_index = (len(median_list) / 2) - 1
        right_center_index = len(median_list) / 2

        return mean(median_list[left_center_index],
                    median_list[right_center_index])


total_student, total_tuition = enrollment_stats(universities)

print("*" * 50)
print(f"Total students: {sum(total_student):,}")
print(f"Total tuition: $ {sum(total_tuition):,}")

print(f"\nStudent mean: {mean(total_student):,.2f}")
print(f"Student median: {median(total_student):,}")

print(f"\nTuition mean: $ {mean(total_tuition):,.2f}")
print(f"Tuition median: $ {median(total_tuition):,}")

print("*" * 50)
