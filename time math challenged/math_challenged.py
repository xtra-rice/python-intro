import random
import time

print("You have 10 questions to answer.")
input("Press enter to start! \n--------------------------------------")

operators = ["+", "-", "*"]
max_questions = 0
user_score = 0

start_time = time.time()
while max_questions < 10:
    x = random.randint(1, 9)
    y = random.randint(1, 9)
    operator = random.choice(operators)

    question = (f"{x} {operator} {y}")
    user_answer = input((question) + " = ")
    correct_answer = eval(question)

    max_questions += 1

    if user_answer.isdigit() and int(user_answer) == correct_answer:
        user_score += 1


end_time = time.time()
elapsed_time = round(end_time - start_time, 2)
print(f"Nice work! You finished in {elapsed_time} seconds! Score: {user_score} / {max_questions} ")
