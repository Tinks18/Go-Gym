from django.shortcuts import render, redirect, get_object_or_404
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Gymslot
from .forms import SlotForm


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
