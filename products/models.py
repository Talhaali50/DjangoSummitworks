from django.db import models
from django.utils import timezone


# Create your models here.
class products(models.Model):
    product_id = models.CharField(max_length=30)
    text = models.TextField()
    purchased_date = models.DateTimeField(default=timezone.now)
    sold_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


from django.db import models

# Create your models here.
