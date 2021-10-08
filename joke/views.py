from .models import *
from django.shortcuts import render


# Create your views here.
def home(request, joke_num):
    jokes = Joke.objects.all()
    next = max(list(map(lambda x: x.id, list(jokes))))
    print(next)
    return render(request, 'index.html',
                  {'url': str(joke_num + 1 if next > joke_num else ''),'previous_url':str(joke_num-1 if joke_num>1 else ''), 'joke': Joke.objects.get(id=joke_num).joke})
