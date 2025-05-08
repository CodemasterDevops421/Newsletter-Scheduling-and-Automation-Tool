from django.shortcuts import render, redirect
from .models import Newsletter
from django.utils.timezone import now
from django import forms

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['subject', 'body', 'recipient_list', 'scheduled_time']

def create_newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = NewsletterForm()
    return render(request, 'newsletter/create.html', {'form': form})

def dashboard(request):
    newsletters = Newsletter.objects.all().order_by('-scheduled_time')
    return render(request, 'newsletter/dashboard.html', {'newsletters': newsletters})
