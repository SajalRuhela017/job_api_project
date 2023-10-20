from django.db import models

class Job(models.Model):
    job_id = models.IntegerField(primary_key=True)
    job_value = models.IntegerField()