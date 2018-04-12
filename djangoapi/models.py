from django.db import models


class Data(models.Model):
    fn = models.CharField(max_length=100)
    ln = models.CharField(max_length=100)
    number = models.IntegerField()

    def __str__(self):
        return self.fn
