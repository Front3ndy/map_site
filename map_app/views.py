from django.shortcuts import render, redirect
from .forms import ContactFrom
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def homepage(request):
    return render(request, 'map_app/index.html')

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
