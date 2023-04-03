from django.db import models
from django.contrib.auth.models import User
class Portfolio(models.Model):
    #core
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=50)
    #tag
    tech_tag = models.ManyToManyField('tag.TechTag', null=True)
    lang_tag = models.ManyToManyField('tag.LangTag', null=True)
    #data
    code_url = models.CharField(max_length=70, null=True)
    #goals
    #duration

    #content
    motive = models.TextField(null=True)
    content = models.TextField(null=True)
    image = models.ImageField(upload_to='folio/images/portfolio', blank=True)

    #tag
    #version

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'({self.pk}){self.title}'

    def get_url(self):
        return f'/folio/{self.pk}'

