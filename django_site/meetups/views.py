from django.shortcuts import render, redirect
from .models import Meetup
from .forms import RegistrationForm


# Create your views here.
def index(request):
    meetups = Meetup.objects.all()
    return render(request, 'meetups/index.html', {
        
        'meetups': meetups
    })

def meetup_detail(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
            
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                participant = registration_form.save()
                selected_meetup.participants.add(participant)
                return redirect('confirm-registration')
        
        return render(request, 'meetups/meetup_details.html', {
                'meetup_found':True,
                'meetup': selected_meetup,
                'form': registration_form,
            })

    except Exception as exc:
        return render(request, 'meetups/meetup_details.html', {
            'meetup_found': False
        })

def confirm_registration(request):
    return render(request, 'meetups/registration-success.html')


    # fra https://www.youtube.com/watch?v=t7DrJqcUviA&list=RDCMUCSJbGtTlrDami-tDGPUV9-w&index=6