from django.db import models


class EmpFeedBack(models.Model):
    eid = models.IntegerField()
    fbeid = models.IntegerField()
    rating = models.IntegerField()
    feedback = models.CharField(max_length=300)
