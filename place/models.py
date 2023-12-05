from django.db import models

class PlaceModel(models.Model):
    name = models.CharField(max_length=255)
    attribute1 = models.BooleanField()
    attribute2 = models.BooleanField()
    attribute3 = models.BooleanField()
    attribute4 = models.BooleanField()
    attribute5 = models.BooleanField()
    attribute6 = models.BooleanField()
    attribute7 = models.BooleanField()
    attribute8 = models.BooleanField()
    attribute9 = models.BooleanField()
    attribute10 = models.BooleanField()
    attribute11 = models.BooleanField()
    attribute12 = models.BooleanField()
    attribute13 = models.BooleanField()
    attribute14 = models.BooleanField()
    attribute15 = models.BooleanField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(max_length=255)

    # ... (one-hot 벡터에 해당하는 각 속성에 대한 필드 추가)

# Create your models here.
