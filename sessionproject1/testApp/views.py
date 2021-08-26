from django.shortcuts import render

# Create your views here.

def count_view(request):
    count = int(request.session.get('count', 0))
    new_count = count + 1
    request.session['count'] = new_count
    request.session.set_expiry(30)
    response = render(request, 'testApp/count.html', {'count': new_count})
    return response