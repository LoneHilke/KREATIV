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
        'show_meetups': False,
        'meetups': meetups
    })