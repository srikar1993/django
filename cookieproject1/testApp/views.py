from django.shortcuts import render

# Create your views here.

def cookie_view(request):
    count = int(request.COOKIES.get('count', 0))
    new_count = count + 1
    response = render(request, 'testApp/cookie.html', {'count': new_count})
    response.set_cookie('count', new_count, max_age=60)
    return response