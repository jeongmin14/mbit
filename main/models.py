from django.db import models

class Developer(models.Model):
    name = models.CharField(max_length=50)
    count = models.IntegerField(default=0)

    class Meta:
        db_table = 'developers'
        