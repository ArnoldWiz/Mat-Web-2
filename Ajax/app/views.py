from django.http import JsonResponse
from django.shortcuts import render
from .models import Municipality, State

# Create your views here.

def index(request):
    states = State.objects.all().order_by('name')
    context = {'states': states}
    return render(request, 'app/index.html', context)


def load_municipalities(request):
    state_id = request.GET.get('state_id') 
    municipalities = Municipality.objects.filter(state_id=state_id).order_by('name').values('id', 'name')
    return JsonResponse(list(municipalities), safe=False)