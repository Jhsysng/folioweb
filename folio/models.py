from django.db import models
from django.contrib.auth.models import User


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


class Portfolio(models.Model):
    #core
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=50)
    #tag
    tech_tag = models.ManyToManyField(TechTag, blank=True)
    lang_tag = models.ManyToManyField(LangTag, blank=True)
    #=======data========
    code_url = models.CharField(max_length=70, null=True)
    #duration
    #goals


    #======content=======
    motive = models.TextField(null=True)
    content = models.TextField(null=True)
    image = models.ImageField(upload_to='folio/images/portfolio', blank=True)

    #version

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'({self.pk}){self.title}'

    def get_url(self):
        return f'/folio/{self.pk}'

