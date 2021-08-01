from django.db import models

# Create your models here.

class Spot(models.Model):
    title =models.CharField(max_length=50)

    # areaTags
    # genreTags
    # keywordTags
    image =models.URLField(blank =True)
    # postalCode
    # address
    phoneNumber =models.PositiveIntegerField(blank=True)
    priceEstimated =models.PositiveIntegerField(blank=True)
    timeEstimated =models.PositiveIntegerField(blank=True)
    # transportation
    description =models.CharField(blank=True,max_length=200)
    created_at =models.DateField(auto_now_add=True)

    # タイトル名
    def __str__(self):
        return self.title