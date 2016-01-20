from django.shortcuts import render_to_response


# Create your views here.

def home(request):

    content = {
        'questionId': 1,
        'questionTitle': 'titleOne',
        'questionText': 'Lorem ipsum dolor sit amet'
    }
    return render_to_response('index.html', content)
