from django.shortcuts import render

# Create your views here.
def index(request):
    meetups = [
        {'title': 'Runde perler',
         'location': 'fiskesnørre',
          'slug': 'runde_perler'},
        {'title': 'Rørperler',
         'location': 'elastiksnor',
          'slug': 'rorperler'},
    ]
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups
    })

def meetup_detail(request, meetup_slug):
    
    selected_meetup= {
        'title': 'runde perler',
        'description': 'sjov med perler'
    }
    return render(request, 'meetups/meetup_details.html', {
        'meetup_title': selected_meetup['title'],
        'meetup_description': selected_meetup['description']
    })


    # 1:31 fra https://www.youtube.com/watch?v=t7DrJqcUviA&list=RDCMUCSJbGtTlrDami-tDGPUV9-w&index=6