from django.db import models

class ContactMe(models.Model):

    class Meta:
        verbose_name_plural = "Contact Inquiries"
    
    email = models.EmailField('Email')
    subject = models.CharField('Subject', max_length=160)
    body = models.TextField('Body')
    created = models.DateTimeField('Created', auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.subject
