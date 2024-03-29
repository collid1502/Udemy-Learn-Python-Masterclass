#####################################################################
####               Building a Multiple Choice Quiz               ####
#####################################################################

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompts = [
    "What colour are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What colour are bananas?\n(a) Teal\n(b) Magneta\n(c) Yellow\n\n",
    "What colour are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_prompts[0], "a") ,
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

# now create a function to run test

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score = score + 1 ;

    print("You got " + str(score) + "/" + str(len(questions)) + " Correct")

run_test(questions)
