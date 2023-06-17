
from django.contrib import messages

def infor(request):
    message = messages.info(request, 'Commnent deleted!')
    return message

