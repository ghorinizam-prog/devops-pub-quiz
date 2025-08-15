# Welcome message for the quiz
print("Welcome to the Pub Quiz!")

# List of questions, options, and answers
quiz_questions = [
    {
        "question": "What is the capital of England?",
        "options": ["A) London", "B) Paris", "C) Berlin", "D) Madrid"],
        "answer": "A"
    },
    {
        "question": "What is 20 / 4?",
        "options": ["A) 3", "B) 4", "C) 5", "D) 22"],
        "answer": "C"
    },
    
    {
        "question": "What is the colour of Apple?",
        "options": ["A) Green", "B) Black", "C) Blue", "D) Marron"],
        "answer": "A"
    },

    {
        "question": "What is 2 + 3?",
        "options": ["A) 5", "B) 6", "C) 7", "D) 8"],
        "answer": "A"
    },

    {
        "question": "What is 9-2?",
        "options": ["A) 5", "B) 6", "C) 7", "D) 8"],
        "answer": "C"
    },
]

# Loop through each question
for question in quiz_questions:
    # Display the question and options
    print(question["question"])
    for option in question["options"]:
        print(option)
    
    # Get the user's answer
    user_answer = input("Your answer (A, B, C, D): ").strip().upper() # Ensuring the input is uppercase for comparison
    
    # Check if the answer is correct
    if user_answer == question["answer"]:
        print("Correct!")
    else:
        print(f"Wrong! The correct answer was {question['answer']}.")


# Initialize the score
score = 0

# Loop through each question
for question in quiz_questions:
    # Display the question and options
    print("\n" + question["question"])
    for option in question["options"]:
        print(option)
    
    # Get the user's answer
    user_answer = input("Your answer (A, B, C, D): ").strip().upper() # Ensuring the input is uppercase for comparison
    
    # Check if the answer is correct
    if user_answer == question["answer"]:
        print("Correct!")
        score += 1  # Increment the score for a correct answer
    else:
        print(f"Wrong! The correct answer was {question['answer']}.")


# Goodbye message
print("\nThanks for playing the Pub Quiz!")
# Display the final score
print(f"Your final score is: {score}/{len(quiz_questions)}")