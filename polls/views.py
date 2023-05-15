from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import PhoneForm
from .tasks import sending


def add_number(request):
    sending.delay()
    if request.method == "POST":
        form = PhoneForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("sms"))
    else:
        form = PhoneForm()
    return render(request, "main.html", {"form": form})


def message(request):
    return render(request, "answer.html")
