from django.db import models
from django.contrib.auth.models import User
class Portfolio(models.Model):
    id = models.AutoField(primary_key=True)
    user=models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title=models.CharField(max_length=50)
    #tech_stack_tag
    #urls
    code_url=models.CharField(max_length=70, null=True)
    #goals
    #duration

    #motivation
    motive=models.TextField(null=True)
    content=models.TextField(null=True)
    image=models.ImageField(upload_to='folio/images/portfolio', blank=True)

    #tag
    #version

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'({self.pk}){self.title}'

    def get_url(self):
        return f'/folio/{self.pk}'
