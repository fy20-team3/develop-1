import os
from django.http import HttpResponse


def healthcheck(request):
    hostname = os.uname()[1]
    return HttpResponse("Hello, from {}".format(hostname))

