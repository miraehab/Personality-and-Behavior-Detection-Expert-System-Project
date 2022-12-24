from django.shortcuts import render
import contextlib
import sys
sys.path.append("D:\\New folder\\personality_test\\mainapp")
from pyke import knowledge_engine
from pyke import krb_traceback

engine = None
# Create your views here.
def index(request):
    if request.method == 'POST':
        print(request.POST['age'])
        with open('mainapp/facts.kfb', 'w') as f:
            age = request.POST['age']
            f.write(f"age({age})\n")
            gender =  None#request.POST['gender']=='Female'
            if request.POST['gender'] == 'Female': gender = 1
            else: gender = 0
            f.write(f"gender({gender})\n")
            for i in range(1,2+1):
                print(f"openness_{i}({request.POST[f'question{i}']})")
                f.write(f"openness_{i}({request.POST[f'question{i}']})\n")
            print(sys.path)
            initialize_engine()
            test_questions()

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
    return render(request, 'index.html', context={'questions':question_list})



def initialize_engine():
    global engine
    engine = knowledge_engine.engine(__file__)


def test_questions():
    engine.reset()  # Allows us to run tests multiple times.

    engine.activate('rules')

    print("doing proof")

    try:
        with engine.prove_goal('rules.what_is_the_personality($personality)') as gen:  # you will need to edit this line
            print("sss")
            for vars, plan in gen:
                print("You Personality is: %s" % (vars['personality']))  # you will need to edit this line

    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

    print()
    print("done")