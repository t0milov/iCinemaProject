from django.db import models

class origin(models.Model):
    width = models.IntegerField()
    length = models.IntegerField()

class coordinate(models.Model):
    x_coordinate = models.IntegerField()
    y_coordinate = models.IntegerField()

class meta(models.Model):
    prop = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

class nodeList(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    width = models.IntegerField()
    height = models.IntegerField()
    coordinate = models.ForeignKey(coordinate, on_delete=models.CASCADE)
    meta = models.ForeignKey(meta, on_delete=models.CASCADE)

class startAt(models.Model):
    x_coordinate = models.IntegerField()
    y_coordinate = models.IntegerField()

class endAt(models.Model):
    x_coordinate = models.IntegerField()
    y_coordinate = models.IntegerField()

class linkList(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    startId = models.CharField(max_length=255)
    endId = models.CharField(max_length=255)
    startAt = models.ForeignKey(startAt, on_delete=models.CASCADE)
    endAt = models.ForeignKey(endAt, on_delete=models.CASCADE)
    meta = models.CharField(max_length=255, default=None)

