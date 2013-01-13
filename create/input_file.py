import csv
import os

from django.conf import settings
from django.contrib.gis.geos import fromstr

from create.models import Measurements


"""
Manager class for CSV resources
"""
class NoiseCsv:
    
    def __init__(self, path):
        """ Constructor """
        self._reset()
        self._path = path
        
    def _reset(self):
        """ Reset the manager """
        self._path = None
        
    def read(self):
        """ Read the file """
        # Setup
        content = []
        # Read file
        with open(self._path, 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter='|', quotechar='"')
            headers = spamreader.next()
            #headers = [tmp.replace('"', '')  for tmp in headers[0].split(",")]
            # Loop through rows
            for row in spamreader:
                # Setup
                row_content = {}
                # Loop through columns
                for i in range(len(row)):
                    label = headers[i]
                    value = row[i]
                    row_content[label] = value
                # Post-process row
                row_content = self.post_process(row_content)
                content.append(row_content)
        # Done
        return content
                    
    def get(self):
        """ Get the content of the CSV file in a structured List of Lists """
        return self.read()
        
    def post_process(self, row_content):
        # Setup
        processed_row_content = {}
        column_processors = {
            
        }
        remap = {
            'osm_id': 'osm_id',
            'highway': 'classification',
            'name': 'name',
            'noise_level': 'decibel',
            'geometry': 'geom'
        }
        # Add geometry column
        row_content['geometry'] = self.get_polygon(row_content['osm_id'], row_content['highway'], row_content['wkt'])
        # Remap, excluding unwanted columns
        for column in remap:
            processed_row_content[remap[column]] = row_content[column]
        # Return processed row
        return processed_row_content
    
    def get_polygon(self, osm_id, classification, line_wkt):
        """ Build buffered polygons """
        # Build polygon from WKT
        polygon = fromstr(line_wkt)
        # Get classification
        buffer_distance = self.get_buffer_distance(classification, osm_id)
        # Buffer polygon
        polygon = polygon.buffer(buffer_distance)
        # Return it
        return polygon
    
    def get_buffer_distance(self, classification, osm_id):
        # Try to get a distinct measurement
        matched_ids = Measurements.objects.filter(osm_id=osm_id)
        if not matched_ids == None and len(matched_ids) > 0:
            print 'match: %s' % (matched_ids[0].value)
            return matched_ids[0].value
        else: return settings.CLASSIFICATIONS[classification][1]