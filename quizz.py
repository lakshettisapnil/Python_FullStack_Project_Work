
quiz = [
    {
        "question": "What is the correct file extension for Python?",
        "options": {
            "a": ".pt",
            "b": ".python",
            "c": ".py",
            "d": ".pyt"
        },
        "answer": "c"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": {
            "a": "function",
            "b": "def",
            "c": "fun",
            "d": "define"
        },
        "answer": "b"
    },
    {
        "question": "What is the output of print(type(10))?",
        "options": {
            "a": "<class 'float'>",
            "b": "<class 'int'>",
            "c": "<class 'str'>",
            "d": "<class 'bool'>"
        },
        "answer": "b"
    }
]
score = 0
for q in quiz:
    print("\n" + q["question"])
    
for op,val in q["options"]:
        print(op,val)
    
''' user_answer = input("Enter your answer (a/b/c/d): ").lower()
    
    if user_answer == q["answer"]:
        print("Correct")
        score += 1
    else:
        print("Wrong")
print("\nYour final score:", score, "/", len(quiz))'''
