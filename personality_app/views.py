from django.http import HttpResponse
from django.shortcuts import render
import sys

personality = None
definitions = {
    'dependable': "A dependable person is someone who gives reliable service and is loyal and stable.",
    'lively': "Being lively is being happy or confident, but being able to express it.",
    'extraverted': "Extroverts enjoy spending time with others. They are typically outgoing and love to work on teams. When brainstorming they love to collaborate and talk out loud.",
    'serious': "Serious personalities have a strong work ethic that allows them to push through challenges in order to reach their goals.",
    'responsible': "Responsible people are truthful and sincere. They may not always say what the other person wants to hear, but they will always tell the truth as they see it",
}
benefits = {
    'dependable': [
        "The dependable person is someone you can count on in the workplace, at home, or even in the greater management field of governance and politics.",
        "Being dependable means that you do what you say you will, when you say you will. You can be trusted to complete any task, and you will do it well.",
        "A dependable person builds trust by holding him/herself accountable, and if they lead others, holding their team members accountable as well. Dependable people are also responsive.",
    ],
    'lively': [
        "If you are lively, people want to be around you, since they are drawn to your happiness and confidence.",
        "In a study, people who were lively displayed increased brain activity in a region thought to suppress pain and were more likely to have their pain eased by a placebo instead of actual pain-reducing drugs.",
        "Being lively can really attract people to you and make you a happier and healthier person.",
    ],
    'extraverted': [
        "You are wired for enthusiasm. Research has found that extroverts are more likely to associate pleasurable feelings with their current environment, according to one analysis of neurological differences between introverts and extroverts.",
        "You are more likely to be a leader. Research has found that most leaders self-identify as extroverts. And it’s no surprise. You are great in groups, large rooms and often have no problem building rapport with anyone.",
        "You’re anti-boring. Extroverts are great at pulling out the best from people — conversation, energy and confidence. You are also more likely to have lots of interesting adventures, fun activities and socializing in your calendar which gives you lots to talk about.",
    ],
    'serious': [
        "You are able to maintain your focus on a task, even when the going gets tough.",
        "Serious personalities have a strong work ethic that allows them to push through challenges in order to reach their goals.",
        "They can quickly assess a situation or problem and come up with practical solutions to address it effectively.",
    ],
    'responsible': [
        "Responsibility is important because it makes you more productive. Without responsibility, you are more likely to shirk your duties or even miss deadlines.",
        "Many people associate responsibility with hardship and discomfort, but this is not always the case. Responsibility can increase your self-esteem.",
        "One of the key benefits of responsibility is that it helps build strong relationships. When you are responsible, you become a more reliable and trustworthy person.",
    ]
}
challenges = {
    'dependable': [
        "You Become a Pushover and Support the Slackers",
        "You Never Hear Praise",
        "You Attract the Wrong Kind of People",
    ],
    'lively': [
        "Lively people find it hard to say no, even in detrimental situations.",
        "Highly lively people tend to be people-pleasers, often sacrificing their own interests and needs in the interest of helping, supporting, or caring for others.",

    ],
    'extraverted': [
        "Often unable to make analytical, emotionless judgements.",
        "May lack independence and gumption.",
        "May value too highly the validation of others.",
        "May occasionally come across as harsh and aggressive or controlling and arrogant.",
    ],
    'serious': [
        "At first glance, someone with a Serious personality type might seem like they have it all together.",
        "They tend to be dependable and responsible, and are known for being reliable and pragmatic.",
        "But despite their many strengths, those with a Serious personality can also face a number of -unique challenges.",
    ],
    'responsible': [
        "People who shoulder responsibility tend to be overly-relied on by other people.",
        "Shouldering responsibility tends to be stressful and require quick split-second decisions.",
    ],
}


# Create your views here.
def index(request):
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
                    f.write(f"neuroticism_{i - 4}({request.POST[f'question{i}']})\n")
                elif i <= 12:
                    f.write(f"conscientiousness_{i - 8}({request.POST[f'question{i}']})\n")
                elif i <= 16:
                    f.write(f"agreeableness_{i - 12}({request.POST[f'question{i}']})\n")
                else:
                    f.write(f"extraversion_{i - 16}({request.POST[f'question{i}']})\n")

        personalities = test_questions()
        print(personalities)
        return render(request, 'feedback.html', context={
            'personality': personalities[-1].title(),
            'benefits': benefits[personalities[-1]],
            'challenges': challenges[personalities[-1]],
            'definition': definitions[personalities[-1]],
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
    return render(request, 'index.html', context={'questions': question_list})


def test_questions():
    sys.path.append('personality_app/pyke')
    import driver
    return driver.bc_test()
