
# SOLAR SYSTEM QUIZ COMPETITION
# Python Capstone Project

questions = [
    {
        "question": "How many planets are there in our Solar System?",
        "options": ["A. 7", "B. 8", "C. 9", "D. 10"],
        "answer": "B"
    },
    {
        "question": "Which planet is closest to the Sun?",
        "options": ["A. Earth", "B. Mars", "C. Mercury", "D. Venus"],
        "answer": "C"
    },
    {
        "question": "Which is the largest planet in our Solar System?",
        "options": ["A. Earth", "B. Jupiter", "C. Saturn", "D. Neptune"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Mars", "B. Venus", "C. Jupiter", "D. Mercury"],
        "answer": "A"
    },
    {
        "question": "Which planet is famous for its beautiful rings?",
        "options": ["A. Earth", "B. Mars", "C. Saturn", "D. Venus"],
        "answer": "C"
    },
    {
        "question": "Which planet do we live on?",
        "options": ["A. Mars", "B. Earth", "C. Venus", "D. Jupiter"],
        "answer": "B"
    },
    {
        "question": "What is the Sun?",
        "options": ["A. Planet", "B. Moon", "C. Star", "D. Asteroid"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Morning Star?",
        "options": ["A. Venus", "B. Mars", "C. Saturn", "D. Neptune"],
        "answer": "A"
    },
    {
        "question": "Which planet is farthest from the Sun?",
        "options": ["A. Earth", "B. Jupiter", "C. Uranus", "D. Neptune"],
        "answer": "D"
    },
    {
        "question": "What is the natural satellite of Earth?",
        "options": ["A. Sun", "B. Moon", "C. Mars", "D. Venus"],
        "answer": "B"
    }
]


# Display quiz instructions
def show_instructions():
    print("\n========== QUIZ INSTRUCTIONS ==========")
    print("1. There are 10 questions.")
    print("2. Each correct answer gives 1 mark.")
    print("3. There is no negative marking.")
    print("4. Enter A, B, C or D as your answer.")
    print("5. Your final score will be displayed.")
    print("=======================================")


# Calculate result
def calculate_result(score):
    percentage = (score / len(questions)) * 100

    if percentage >= 80:
        remark = "Excellent Performance!"
    elif percentage >= 60:
        remark = "Good Performance!"
    elif percentage >= 40:
        remark = "Average Performance!"
    else:
        remark = "Keep Practicing!"

    return percentage, remark


# Save participant result
def save_result(name, score, percentage):
    file = open("quiz_results.txt", "a")

    file.write(
        name + " | " + str(score) + "/10 | "
        + str(round(percentage, 2)) + "%\n"
    )

    file.close()


# Start quiz
def start_quiz():

    name = input("\nEnter participant name: ").strip()

    if name == "" or "|" in name:
        print("Please enter a valid name.")
        return

    score = 0
    correct = 0
    incorrect = 0

    print("\nWelcome", name, "!")
    print("Welcome to the Solar System Quiz!\n")

    for i in range(len(questions)):

        print("\n---------------------------------------")
        print("Question", i + 1, ":", questions[i]["question"])

        for option in questions[i]["options"]:
            print(option)

        while True:
            answer = input("Enter your answer (A/B/C/D): ").strip().upper()

            if answer in ["A", "B", "C", "D"]:
                break
            else:
                print("Invalid choice! Enter A, B, C or D.")

        if answer == questions[i]["answer"]:
            print("Correct Answer!")
            score += 1
            correct += 1

        else:
            print("Wrong Answer!")
            print("Correct answer:", questions[i]["answer"])
            incorrect += 1

    # Display final result
    percentage, remark = calculate_result(score)

    print("\n=======================================")
    print("             QUIZ RESULT")
    print("=======================================")
    print("Participant Name:", name)
    print("Total Questions:", len(questions))
    print("Correct Answers:", correct)
    print("Incorrect Answers:", incorrect)
    print("Final Score:", score, "/", len(questions))
    print("Percentage:", round(percentage, 2), "%")
    print("Performance:", remark)
    print("=======================================")

    save_result(name, score, percentage)

    print("Your result has been saved successfully!")


# View previous results
def view_results():

    print("\n========== PREVIOUS RESULTS ==========")

    try:
        file = open("quiz_results.txt", "r")
        records = file.readlines()
        file.close()

        if len(records) == 0:
            print("No results available.")

        else:
            for record in records:
                print(record.strip())

    except FileNotFoundError:
        print("No quiz results found yet.")


# Main menu
def main():

    while True:

        print("\n")
        print("=======================================")
        print("       SOLAR SYSTEM QUIZ COMPETITION")
        print("=======================================")
        print("1. Start Quiz")
        print("2. Quiz Instructions")
        print("3. View Previous Results")
        print("4. Exit")
        print("=======================================")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            start_quiz()

        elif choice == "2":
            show_instructions()

        elif choice == "3":
            view_results()

        elif choice == "4":
            print("\nThank you for participating!")
            print("Exiting Solar System Quiz.")
            break

        else:
            print("Invalid choice! Please try again.")


# Run the program
main()
