str1 = "14, 625, 498.002"

def replace(str1):
    mapped = str1.maketrans(",.",".,")
    str1 = str1.translate(mapped)
    return str1.replace(". ",".")

if __name__ == "__main__":
    print(replace(str1))