from django.http import HttpResponse
from django.shortcuts import render
import sys

personality = None
# Create your views here.
def index(request):
    question_list = []
    if request.method == 'POST':
        with open('personality_app/pyke/facts.kfb', 'w') as f:
            age = request.POST['age']
            f.write(f"age({age})\n")

            if request.POST['gender'] == 'Female':
                gender = 1
            else:
                gender = 0

            f.write(f"gender({gender})\n")
            for i in range(1, 21):
                if i <= 4:
                    f.write(f"openness_{i}({request.POST[f'question{i}']})\n")
                elif i <= 8:
                    f.write(f"neuroticism_{i-4}({request.POST[f'question{i}']})\n")
                elif i <= 12:
                    f.write(f"conscientiousness_{i-8}({request.POST[f'question{i}']})\n")
                elif i <= 16:
                    f.write(f"agreeableness_{i-12}({request.POST[f'question{i}']})\n")
                else:
                    f.write(f"extraversion_{i-16}({request.POST[f'question{i}']})\n")
        global personalities
        personalities = test_questions()
        return render(request, 'feedback.html', context={
            'personality': personalities[-1].title(),
        }
                      )


    question_list = [
        "I'm good at coming up with new ideas. rate yourself from 1 to 8",
        "I'm curious about how things work. rate yourself from 1 to 8",
        "I appreciate being around diverse groups of people. rate yourself from 1 to 8",
        "I would prefer to have a theoretical discussion rather than making small talk. rate yourself from 1 to 8",
        "I am relaxed most of the time. rate yourself from 1 to 8",
        "I panic easily. rate yourself from 1 to 8",
        "I dislike myself. rate yourself from 1 to 8",
        "I remain calm under pressure. rate yourself from 1 to 8",
        "I complete tasks successfully. rate yourself from 1 to 8",
        "I often forget to put things back in their proper place. rate yourself from 1 to 8",
        "I tell the truth. rate yourself from 1 to 8",
        "I keep my promises. rate yourself from 1 to 8",
        "I believe that I am better than others. rate yourself from 1 to 8",
        "I treat all people equally. rate yourself from 1 to 8",
        "I am easy to satisfy. rate yourself from 1 to 8",
        "I trust what people say. rate yourself from 1 to 8",
        "I avoid contacts with others. rate yourself from 1 to 7",
        "I don't talk a lot. rate yourself from 1 to 7",
        "I don't mind being the center of attention. rate yourself from 1 to 7",
        "I make friends easily. rate yourself from 1 to 7",
    ]
    return render(request, 'index.html', context={'questions': question_list, 'personality':None})


def test_questions():
    sys.path.append('personality_app/pyke')
    import driver
    return driver.bc_test()

def feedback(request):
    return render(request, 'feedback.html', context={'personality': personality})
