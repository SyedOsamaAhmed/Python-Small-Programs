
quiz = {
    "question1": {
        "question": "What is the capital of Pakistan?",
        "answer": "Islamabad"
    },
    "question2": {
        "question": "What is the capital of Bangladesh?",
        "answer": "Dhaka"
    },
    "question3": {
        "question": "What is the capital of United States?",
        "answer": "New York"
    },
    "question4": {
        "question": "What is the capital of India?",
        "answer": "Delhi"
    },
    "question5": {
        "question": "What is the capital of Italy?",
        "answer": "Viena"
    },

}
score = 0
answer = ''

for key, value in quiz.items():
    print(value["question"])
    answer = input("Answer:")

    if (answer.lower() == value["answer"].lower()):
        print("Correct!")
        score += 1
        print(f"Your score is: {str(score)}\n")
    else:
        print("Wrong!")
        if score == 0:
            pass
        else:
            score -= 1
        print(f"Your score is: {str(score)}\n")

print(f"Your got {score} out of 5 questions correct")
print(f"Your got {score/5*100}%")
