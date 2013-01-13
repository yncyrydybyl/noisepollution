from django.http import HttpResponse


def api(request):
    """ Read location(s), return noise level """ 
    return HttpResponse("nice")