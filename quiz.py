#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "Who is the author of A Little Life the novel?\n(a) Hanya Yanagihara\n(b) Kazuo Ishiguro\n(c) Ian McEwan",
    "Choose the correct synopsis for this novel.\n(a) It follows the mental anguish and moral dilemmas of Rodion Raskolnikov, an impoverished ex-student in Saint Petersburg who plans to kill an unscrupulous pawnbroker for her money.\n(b) The novel follows the lives of four friends in New York City from college through to middle-age.\n(c) The novel covers a year of the author's pursuit of what she wants to obtain from life: happiness.",
    "Who is the main protagonist in the story?\n(a) Michael\n(b) Jude\n(c) Ron"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "b")
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + '/' + str(len(questions)) + " correct")

run_quiz(questions)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




