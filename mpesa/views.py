from django.shortcuts import render

# Create your views here.


def index(request):
    data = {
        'id': 1,
        'name': 'John',
        'phonenumber': '12345678'

    }
    return render(request, 'index.html', {'data': data})
