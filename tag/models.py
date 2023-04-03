from django.db import models


class TechTag(models.Model):
    name = models.CharField(max_length=10,null=False)
    image = models.ImageField(upload_to='tag/techtag',blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class LangTag(models.Model):
    name = models.CharField(max_length=8, null=False)
    image = models.ImageField(upload_to='tag/langtag',blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
# Create your models here.
