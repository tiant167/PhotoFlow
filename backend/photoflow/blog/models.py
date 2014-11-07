from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    pinned = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title
