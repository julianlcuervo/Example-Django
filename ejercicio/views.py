from django.http import HttpResponse

from datetime import datetime
import json 

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('oh hi, la hora es {now}'.format(now = now))


def num(request):
    """debugger"""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    """import pdb; pdb.set_trace()"""
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message':'Integers sorted successfully'
    }
    return HttpResponse(json.dumps(data), content_type='application/json')


def say_hi(request,name,age):
    if age < 12:
        message = 'lo siento {}, no pudes estar aqui'.format(name)
    else:
        message = 'Hola bienvenido {}'.format(name)
    return HttpResponse(message)