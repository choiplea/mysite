
from django.http import HttpResponse


def index(request):
    return HttpResponse("바다야 힘내라!.")
