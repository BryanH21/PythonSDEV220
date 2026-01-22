# Name: Bryan 
# Module 2 Lab 

DEANS_LIST: float = 3.5
DEANS_LIST_MSG: str = "You made the Dean's list"
HONOR_ROLL: float = 3.25
HONOR_ROLL_MSG: str = "You made the Honor Roll"
SENTINEL: str = 'ZZZ'
INPUT_PROMPT: str = 'Enter the first name ("ZZZ" to quit): '
INPUT_PROMPT2: str = 'Enter the GPA: '

first_name: str = ''
gpa: float = 0.0

while True:
    first_name = input(INPUT_PROMPT)
    if first_name.upper() != SENTINEL:
        gpa = float(input(INPUT_PROMPT2))
        if gpa >= DEANS_LIST:
            print(DEANS_LIST_MSG)
        elif gpa >= HONOR_ROLL:
            print(HONOR_ROLL_MSG)
    else:
        break