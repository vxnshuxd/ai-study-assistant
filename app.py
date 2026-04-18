import re

# Function to summarize text
def summarize(text):
    sentences = text.split('.')
    summary = '.'.join(sentences[:2])   # first 2 sentences
    return summary

# Function to generate questions
def generate_questions(text):
    sentences = text.split('.')
    questions = []

    for s in sentences:
        s = s.strip()
        words = s.split()

        if len(words) < 4:
            continue

        # If sentence contains "is/are"
        if " is " in s:
            parts = s.split(" is ")
            questions.append(f"What is {parts[0]}?")
        
        elif " are " in s:
            parts = s.split(" are ")
            questions.append(f"What are {parts[0]}?")
        
        else:
            questions.append(f"Explain: {s}")

    return questions[:5]
def generate_answers(text):
    sentences = text.split('.')
    answers = []

    for s in sentences:
        s = s.strip()
        if len(s) > 10:
            answers.append(s.strip().capitalize())

    return answers[:5]

# Main program
text = input("Enter your study text:\n")

summary = summarize(text)
questions = generate_questions(text)
answers = generate_answers(text)

print("\n===== SUMMARY =====")
print(summary)

print("\n===== QUESTIONS & ANSWERS =====")

for i in range(min(len(questions), len(answers))):
    print(f"\nQ{i+1}: {questions[i]}")
    print(f"A{i+1}: {answers[i]}")