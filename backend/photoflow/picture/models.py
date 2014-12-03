from django.db import models

# Create your models here.
class Picture(models.Model):
    img_height = models.PositiveIntegerField(null=True,blank=True)
    img_width = models.PositiveIntegerField(null=True,blank=True)
    img = models.ImageField(upload_to='images',width_field='img_width',height_field='img_height')
    title = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title