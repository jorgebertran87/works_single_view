from django.db import models


class Contributors(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "contributors"


class Works(models.Model):
    id = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    contributors = models.ManyToManyField(Contributors)
    iswc = models.CharField(max_length=255, primary_key=True)
    source = models.CharField(max_length=255)

    class Meta:
        db_table = "works"    
