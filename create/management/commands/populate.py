import os

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from create.models import NoiseObjects
from create.input_file import NoiseCsv


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Get CSV data
        csv_data = self.get_csv_data()
        # Reset database
        all = NoiseObjects.objects.all();
        all.delete()
        # Write to database
        print csv_data
        self.write_db(csv_data)
        
    def get_csv_data(self):
        """ Transform local CSV file into List """
        # Read file
        manager = NoiseCsv(os.path.join(settings.RESOURCES,'berlin_highway_lines.csv'))
        csv = manager.get()
        return csv
    
    def write_db(self, data):
        # Loop through rows
        total = len(data)
        for i in range(total):
            print data[i]
            print 'Writing %s/%s' % (i, total)
            item = NoiseObjects(**data[i])
            item.save()
        