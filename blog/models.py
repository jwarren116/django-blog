from django.db import models


class BlogPost(models.Model):
    class Meta:
        verbose_name_plural = "Blog Posts"

    title = models.CharField('Title', max_length=63)
    post = models.TextField('Content')
    created = models.DateTimeField('Created', auto_now_add=True, auto_now=False)
    display = models.BooleanField('Display on Home Page?', default=False)

    def __unicode__(self):
        return self.title


class Project(models.Model):
    class Meta:
        verbose_name_plural = "Projects"

    title = models.CharField(max_length=63)
    screen_shot = models.ImageField(upload_to='screen_shots')
    description = models.TextField()
    link = models.URLField()
    display = models.BooleanField('Display on Home Page?', default=False)

    def __unicode__(self):
        return self.title
