from django.db import models


class BlogPost(models.Model):
    class Meta:
        verbose_name_plural = "Blog Posts"

    title = models.CharField('Title', max_length=63)
    post = models.TextField('Content')
    created = models.DateTimeField('Created', auto_now_add=True, auto_now=False)
    display = models.BooleanField('Display on Home Page?', default=False)
    heading = models.BooleanField('Display as Heading?', default=False)

    def __unicode__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=63)
    screen_shot = models.ImageField(upload_to='blog/static/screen_shots/')
    description = models.TextField()
    link = models.URLField()

    def __unicode__(self):
        return self.title
