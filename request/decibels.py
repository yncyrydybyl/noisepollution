from django.contrib.gis.geos import GEOSGeometry
from create.models import NoiseObjects


class NoiseMeasure:
    """ Manager class for noise measurement requests """
    
    def __init__(self, lat, lng):
        """ Constructor """
        self._reset()
        self._lat = lat
        self._lng = lng
        
    def _reset(self):
        """ Reset the manager """
        self._lat = None
        self._lng = None
        
    def get(self):
        """ Get the measurement """
        # Build point from lat lng
        pnt = GEOSGeometry('srid=4326;POINT(%s %s)')
        # Get objects
        matches = NoiseObjects.objects.filter(geom__intersection=pnt)
        # Get the decibel from the matches
        decibel = 0
        for match in matches:
            dec = matches["decibel"]
            if dec > decibel: decibel = dec
        # Return decibel
        return decibel