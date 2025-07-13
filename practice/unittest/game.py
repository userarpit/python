def rock_paper_scissors(input):
    if input < 0 or input > 2:
        raise ValueError("choice must be 0, 1, or 2")

    choices = ["rock", "paper", "scissors"]
    return choices[input]
