from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from .models import Contact

# Create your views here.
def contactview(request):
    name = ""
    email = ""
    message = ""
    recipient_mail = 'champ.wikrom@gmail.com'

    form= ContactForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get("name")
        email = form.cleaned_data.get("email")
        message = form.cleaned_data.get("message")
        subject = f'{name} has send your a message'

        Contacter = Contact(name=name, email=email, message=message)
        Contacter.save()

        message = f'{name} with the email {email} sent the following message:\n\n{message}'
        send_mail(subject, message, 'wikorm.champ@gmail.com', [recipient_mail])

        context = {'form': form}
        return render(request, 'resume/index.html', context)
    else:
        context = {'form': form}
        return render(request, 'resume/index.html', context)