from django.db import models

class Portfolio(models.Model):
    id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    #tech_stack_tag
    #urls

    #goals
    #motivation
    #content
    content=models.TextField(null=True)
    #image(sample_image)
    image=models.ImageField(upload_to='folio/images/portfolio', blank=True)


    #tag
    #version

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'({self.pk}){self.title}'

    def get_url(self):
        return f'/folio/{self.pk}'

# Create your models here.
