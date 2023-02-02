from django.shortcuts import render, redirect, get_object_or_404
import calendar
from calendar import HTMLCalendar
from datetime import datetime
# from .models import Event
from .models import Gymslot
from .forms import SlotForm



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
        form = SlotForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('get_schedule')
    form = SlotForm()
    context = {
        'form': form
        }        
    return render(request, 'gymtrainer/add_slot.html', context)

    # if request.method == 'POST':
    #     firstname = request.POST.get('fslot_name')
    #     lastname = request.POST.get('lslot_name')
    #     submit = 'submit' in request.POST
    #     Gymslot.objects.create(firstname=firstname, lastname=lastname, submit=submit)

    #     return redirect('get_schedule')
 
    # return render(request, 'gymtrainer/add_slot.html')


def edit_slot(request, slot_id):
    slot = get_object_or_404(Gymslot, id=slot_id)
    if request.method == 'POST':
        form = SlotForm(request.POST, instance=slot)
        if form.is_valid():
            form.save()
            return redirect('get_schedule')
    form = SlotForm(instance=slot)
    context = {
        'form': form
    }
    return render(request, 'gymtrainer/edit_slot.html', context)


def delete_item(request, slot_id):
    slot = get_object_or_404(Gymslot, id=slot_id)
    slot.delete()
    return redirect('get_schedule')


def all_events(request):
    events_list = Events.objects.all()
    return render(request, 'gymtrainer/events_list.html',
    {'events_list': events_list})
