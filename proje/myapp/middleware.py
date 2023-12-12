from .models import *

def myapp_middleware(get_response):

    def middleware(request):
        request.categories =Product.objects.all()

        response =get_response

        return response(request)
    
    return middleware