# contact/views.py
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Optional: Send email
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})