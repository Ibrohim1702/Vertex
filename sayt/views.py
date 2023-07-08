from django.shortcuts import render

from sayt.models import Contact


# Create your views here.


def index(requests):
    ctx = {}
    if requests.POST:
        name =requests.POST.get('name')
        email =requests.POST.get('email')
        message =requests.POST.get('message')
        Contact.objects.create(
            name=name, email=email, message=message
        )
        ctx = {
            "contact": index
        }


    return render(requests, "index.html", ctx)