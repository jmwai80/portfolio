from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponseRedirect, reverse
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'john/index.html',{})

def gallery(request):
    return render (request, 'john/gallery.html',{})

def resume(request):
    return render(request, 'john/resume.html', {})

def portfolio(request):
    return render(request, 'john/portfolio.html', {})
def about(request):
    return render(request, 'john/about.html', {})

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['jmwai@conncoll.edu'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, 'john/thanks.html',{})
    return render(request, "john/email.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')
