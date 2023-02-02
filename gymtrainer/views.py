from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event
from .models import Gymslot


# from django.views.generic import TemplateView


# class HomeView(TemplateView):
#     """
#     View to render homepage
#     """
#     template_name = 'home/index.html'

# Create your views here.

def get_schedule(request):
    slots = Gymslot.objects.all()
    context = {
        'slots': slots
    }
    return render(request, 'gymtrainer/get_schedule.html', context)


def add_slot(request):
    if request.method == 'POST':
        firstname = request.POST.get('fslot_name')
        lastname = request.POST.get('lslot_name')
        submit = 'submit' in request.POST
        Gymslot.objects.create(firstname=firstname, lastname=lastname, submit=submit)

        return redirect('get_schedule')
 
    return render(request, 'gymtrainer/add_slot.html')


# def all_events(request):
#     events_list = Events.objects.all()
#     return render(request, 'gymtrainer/events_list.html',
#     {'events_list': events_list})
