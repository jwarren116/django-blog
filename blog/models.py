from django.db import models


class BlogPost(models.Model):
    class Meta:
        verbose_name_plural = "Blog Posts"

    title = models.CharField('Title', max_length=120)
    post = models.TextField('Content')
    blurb = models.TextField('Blurb')
    created = models.DateTimeField('Created', auto_now_add=True, auto_now=False)
    display = models.BooleanField('Display on Home Page?', default=False)
    heading = models.BooleanField('Display as Heading?', default=False)

    def __unicode__(self):
        return self.title
