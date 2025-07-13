from random_word import RandomWords


def draw_shape(count):
    match count:
        case 0:
            print("-------")
        case 1:
            print("-------")
            print("   0   ")
        case 2:
            print("-------")
            print("   0   ")
            print("   |   ")
        case 3:
            print("-------")
            print(r" \ 0   ")
            print("   |   ")
        case 4:
            print("-------")
            print(r" \ 0 / ")
            print("   |   ")
        case 5:
            print("-------")
            print(r" \ 0 / ")
            print("   |   ")
            print(" /     ")
        case 6:
            print("-------")
            print(r" \ 0 / ")
            print("   |   ")
            print(r" /   \ ")
        case 7:
            print("-------")
            print(r" \ 0 /  |")
            print("   |   ")
            print(r" /   \ ")
        case 8:
            print("-------")
            print(r" \ 0 / _|")
            print("   |   ")
            print(r" /   \ ")
        case 9:
            print("-------")
            print("  0_|")
            print(r" /|\  ")
            print(r" / \ ")


# Return a single random word
random_word = RandomWords().get_random_word()
print(random_word)
name = input("Enter your name - ")
print(f"Welcome {name}")
print("------------------")
print("Try to guess in less than 10 attempts")
guess_word = "_" * len(random_word)
print(f"Guess the word (of length {len(random_word)}): ", guess_word)

guess_word = list(guess_word)
count = 0
while count < 10:
    letter = input()
    if len(letter) > 1:
        print("Please enter the data of length 1")
        continue
    if not (96 < ord(letter) <= 122) and not (64 < ord(letter) <= 90):
        print("Please enter the letter from the alphabet [a-z]")
        continue

    letter = letter.lower()
    if letter in random_word:
        all_occurrence_of_letter = [
            i
            for i in range(len(random_word))
            if random_word.startswith(letter, i)
        ]

        # print(all_occurrence_of_letter)

        for index in all_occurrence_of_letter:
            guess_word[index] = letter
            print(
                f"Guess the word of length {len(random_word)}) :",
                "".join(guess_word),
            )
        if "_" not in guess_word:
            print("you win")
            break
    else:
        if count == 9:
            print("you loose, you let a kind man die.")

        print(f"{9 - count} turns are left")
        draw_shape(count)
        count += 1
