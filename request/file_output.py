import csv
import cStringIO

from create.models import NoiseObjects


class FileOutput():
    
    def __init__(self):
        """ Constructor """
        self._reset()
        
    def _reset(self):
        """ Reset the manager """
        
    def get(self):
        """ Get the content """
        # Setup
        queue = cStringIO.StringIO()
        kml_field = 'geom'
        fields = [
            'osm_id',
            'classification',
            'name',
            'decibel',
            'geom',
            'kml'
        ]
        writer = csv.writer(queue, lineterminator='\n')
        # Get a handle on all noise objects
        matches = NoiseObjects.objects.all().values()
        # Loop through noise objects
        total = len(matches)
        for i in range(total):
            #if i > 1000: break
            # Report
            print "To CSV %s/%s" % (i, total)
            # Modify KML field
            matches[i]['kml'] = matches[i]["geom"].kml
            # Set fields
            row = []
            for field in fields:
                row.append(matches[i][field])
            # Write row
            writer.writerow(row)
        # Done
        value = queue.getvalue()
        return value