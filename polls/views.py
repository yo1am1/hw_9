from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import PhoneForm
from .models import Number
from .tasks import sending


def add_number(request):
    if request.method == "POST":
        form = PhoneForm(request.POST)
        if form.is_valid():
            form.save()
            num_clean = Number.objects.values("number").last().get("number")

            sending.delay(num_clean)

            return HttpResponseRedirect(reverse("send_message"))
    else:
        form = PhoneForm()
    return render(request, "main.html", {"form": form})


def message(request):
    return render(request, "answer.html")
