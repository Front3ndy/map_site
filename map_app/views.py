from django.shortcuts import render, redirect
from .forms import ContactFrom
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.views.generic.base import View

from .models import ObjectsData


class DetailView(View):

    def get(self, request, pk):
        dost = ObjectsData.objects.get(id=pk)
        return render(request, 'map_app/review.html', {'dost': dost})

def homepage(request):
    dosts = ObjectsData.objects.all()
    nine_dosts = ObjectsData.objects.all()[:9]
    return render(request, 'map_app/index.html', {'dosts_list': dosts, 'some': nine_dosts})

def contact(request):
    if request.method == 'POST':
        form = ContactFrom(request.POST)
        if form.is_valid():
            subject = "Пробное сообщение"
            body = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message,
                          'admin@example.com',
                          ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
            return redirect("home")
    form = ContactFrom()
    return render(request, "map_app/form.html", {'form': form})
