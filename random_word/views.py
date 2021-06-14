from django.shortcuts import render, redirect
# Create your views here.
from django.utils.crypto import get_random_string
import random
# Create your views here.
def index(request):
    request.session['contador'] = 0
    return redirect('/random_word')

def random_word(request):

    request.session['contador'] += 1
    context = {
        'generador' : get_random_string(length=14),
        'num_random':(random.randint(1,1000))
    }
    return render(request, 'index.html', context)