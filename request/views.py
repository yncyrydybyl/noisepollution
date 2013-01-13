from django.http import HttpResponse


def noise_level(request):
    """ Read location(s), return noise level """ 
    return HttpResponse("nice")