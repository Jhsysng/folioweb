from django.db import models

class Portfolio(models.Model):
    title=models.CharField(max_length=50)
    #tech_stack_tag
    #urls

    #goals
    #motivation
    content=models.TextField(null=True)
    #images

    #tag
    #version

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'({self.pk}){self.title}'

    def get_url(self):
        return f'/folio/{self.pk}'

# Create your models here.
