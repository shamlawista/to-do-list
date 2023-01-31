import json

with open("JSON_ex.json", 'r') as file:
    content = file.read()

data = json.loads(content)
score = 0
for question in data:
    print(question["question_text"])
    for index, choices in enumerate(question["alternatives"]):
        print(index+1, '-', choices)
    user_choice = input("Enter the correct answer: ")
    question["user_choice"] = user_choice
    if question["user_choice"] == question["correct_answer"]:
        score = score+1

print(score, "/", len(data))

for question in data:
    user_ans = int(question["user_choice"])
    correct_ans= int(question["correct_answer"])
    print("your answer to", question["question_text"], "was", question["alternatives"][user_ans-1])
    print("correct answer is: ", question["alternatives"][correct_ans-1])
