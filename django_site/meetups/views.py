from django.shortcuts import render
from .models import Meetup
from .forms import Registrationform


# Create your views here.
def index(request):
    meetups = Meetup.objects.all()
    return render(request, 'meetups/index.html', {
        
        'meetups': meetups
    })

def meetup_detail(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        registration_form = Registrationform()
        return render(request, 'meetups/meetup_details.html', {
            'meetup_found':True,
            'meetup': selected_meetup,
            'form': registration_form,
        })
    except Exception as exc:
        return render(request, 'meetups/meetup_details.html', {
            'meetup_found': False
        })


    # 1:31 fra https://www.youtube.com/watch?v=t7DrJqcUviA&list=RDCMUCSJbGtTlrDami-tDGPUV9-w&index=6