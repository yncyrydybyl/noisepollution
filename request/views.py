import json

from django.http import HttpResponse, HttpResponseBadRequest

from request.decibels import NoiseMeasure


def api(request):
    """ Read location(s), return noise level """ 
    # Setup
    parameters = None
    required = ["lat", "lng"]
    sources = ["POST", "GET"]
    # Assert parameters
    for source in sources:
        if not parameters == None: break
        s = getattr(request, source)
        valid = True
        for req in required:
            if not req in s: valid = False
        if valid: parameters = s
    if parameters == None: return HttpResponseBadRequest("Need parameters lat and lng")
    # Get result
    measure = NoiseMeasure(parameters["lat"], parameters["lng"])
    result = measure.get()
    # Return response
    response = json.dumps({'decibel': result})
    return HttpResponse(response)