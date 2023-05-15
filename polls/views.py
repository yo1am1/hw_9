from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import PhoneForm
from .tasks import sending

from django.shortcuts import render

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