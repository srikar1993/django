from django.http import HttpResponse

class ExecutionFlowMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # Pre processing of request
        print('This line is printed at pre-processing of request...')
        # Forwarding the request to next level
        response = self.get_response(request)
        # Post processing of request
        print('This line is printed at post-processing of request...')
        return response

class AppMaintainanceMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        return HttpResponse('<h1>Application Under Maintainance...</h1><h1>Please Try Again After Some Time</h1>')

class ErrorMessageMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def process_exception(self, request, exception):
        mymsg = '''
        <h1>Please check the input you have provided...</h1><hr>
        '''
        exceptioninfo = f'''
        <h1>Raised Exception: {exception.__class__.__name__}</h1>
        <h1>Exception Message: {exception}</h1>
        '''
        return HttpResponse(mymsg + exceptioninfo)

class FirstMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # Pre processing of request
        print('This line is printed by First Middleware at pre-processing of request...')
        # Forwarding the request to next level
        response = self.get_response(request)
        # Post processing of request
        print('This line is printed by First Middleware at post-processing of request...')
        return response

class SecondMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # Pre processing of request
        print('This line is printed by Second Middleware at pre-processing of request...')
        # Forwarding the request to next level
        response = self.get_response(request)
        # Post processing of request
        print('This line is printed by Second Middleware at post-processing of request...')
        return response

class ThirdMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # Pre processing of request
        print('This line is printed by Third Middleware at pre-processing of request...')
        # Forwarding the request to next level
        response = self.get_response(request)
        # Post processing of request
        print('This line is printed by Third Middleware at post-processing of request...')
        return response

