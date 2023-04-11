from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown


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
    #======core========
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=50)

    #=======data========
    code_url = models.CharField(max_length=70, null=True)
    duration = models.CharField(max_length=20, null=True)
    tech_tag = models.ManyToManyField(TechTag, blank=True)
    lang_tag = models.ManyToManyField(LangTag, blank=True)
    #env(later)

    #======content=======
    #goals(later)
    motive = models.TextField(null=True)
    content = MarkdownxField()
    image = models.ImageField(upload_to='folio/images/portfolio', blank=True)
    version = models.CharField(max_length=10, null=True)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def get_content(self):
        return markdown(self.content)
    def __str__(self):
        return f'({self.pk}){self.title}'

    def get_url(self):
        return f'/folio/{self.pk}'

