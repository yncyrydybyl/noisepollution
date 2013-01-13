from django.contrib.gis.db import models

class NoiseObjects(models.Model):
    osm_id = models.CharField(max_length=256, null=True,blank=True)
    name = models.TextField(null=True,blank=True)
    classification = models.CharField(max_length=256, null=True,blank=True)
    decibel = models.FloatField(null=True,blank=True)
    geom = models.GeometryField(null=True,blank=True)
    objects = models.GeoManager()
    class Meta:
        db_table = 'noise_objects'
        
class Measurements(models.Model):
    osm_id = models.CharField(max_length=256, null=True,blank=True)
    value = models.FloatField(null=True,blank=True)
    class Meta:
        db_table = 'noise_measurements'