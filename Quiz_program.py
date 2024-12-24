
questions = ("What gas do plants absorb?",
             "Which element is in DNA?",
             "Who discovered gravity?",
             "What is Earth's liquid core?",
             "What is the study of stars?")

options = (("A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"),
           ("A. Helium", "B. Carbon", "C. Oxygen", "D. Iron"),
           ("A. Einstein", "B. Newton", "C. Galileo", "D. Tesla"),
           ("A. Magma", "B. Water", "C. Iron", "D. Lead"),
           ("A. Biology", "B. Astronomy", "C. Geology", "D. Physics"))

correct_answers = ("C", "B", "B", "A", "B")
user_answers = []
question_number = 0
correct, incorrect = 0, 0

for question in questions:
    print("----------------------------")
    print(question)
    for option in options[question_number]:
        print(option)

    user_answer = input("Enter (A, B, C, D): ").upper()
    user_answers.append(user_answer)

    if user_answer == correct_answers[question_number]:
        print("Correct!")
        correct += 1
    else:
        print("Incorrect!")
        incorrect += 1    
    question_number += 1

print(f"Correct: {correct}")
print(f"Incorrect: {incorrect}")