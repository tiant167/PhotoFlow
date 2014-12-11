#! /usr/bin/env python
#-*-coding:utf-8-*-
from django.db import models
from django.conf import settings
# Create your models here.

# thumbnail thanks to http://www.yilmazhuseyin.com/blog/dev/create-thumbnails-imagefield-django/
class Picture(models.Model):
    img_height = models.PositiveIntegerField(null=True,blank=True)
    img_width = models.PositiveIntegerField(null=True,blank=True)
    img = models.ImageField(upload_to=settings.IMAGE_UPLOAD_ROOT,width_field='img_width',height_field='img_height')
    thumbnail = models.ImageField(upload_to=settings.IMAGE_UPLOAD_ROOT,null=True,blank=True)
    middle = models.ImageField(upload_to=settings.IMAGE_UPLOAD_ROOT,null=True,blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    long = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    def create_thumbnail(self):
        # original code for this method came from
        # http://snipt.net/danfreak/generate-thumbnails-in-django-with-pil/

        # If there is no image associated with this.
        # do not create thumbnail
        if not self.img:
         return

        from PIL import Image
        from cStringIO import StringIO
        from django.core.files.uploadedfile import SimpleUploadedFile
        import os

        # Set our max thumbnail size in a tuple (max width, max height)
        if self.img_height * 2 < self.img_width:
            self.long = True

        if self.long:
            # 竖着的长图我就不考虑了
            THUMBNAIL_SIZE = (1870,500)
            MIDDLE_SIZE = (3560,1000)
        else:
            if self.img_height > self.img_width:
                THUMBNAIL_SIZE = (750,933)
                MIDDLE_SIZE = (1500,1866)
            else:
                THUMBNAIL_SIZE = (622,500)
                MIDDLE_SIZE = (1866,1500)

        try:
            DJANGO_TYPE = self.img.file.content_type
            if DJANGO_TYPE == 'image/jpeg':
                PIL_TYPE = 'jpeg'
                FILE_EXTENSION = 'jpg'
            elif DJANGO_TYPE == 'image/png':
                PIL_TYPE = 'png'
                FILE_EXTENSION = 'png'
        except AttributeError:
            # if update the object will get a File Object not UploadFile Obj
            # so it should get the ext from name
            ext = self.img.file.name.split('.')[-1]
            if ext in ('jpg','jpeg','JPG','JPEG'):
                PIL_TYPE = 'jpeg'
                FILE_EXTENSION = 'jpg'
            elif ext in ('png','PNG'):
                PIL_TYPE = 'png'
                FILE_EXTENSION = 'png' 

        # Open original photo which we want to thumbnail using PIL's Image
        image = Image.open(StringIO(self.img.read()))
        self.img.seek(0)
        middle_image = Image.open(StringIO(self.img.read()))
        # Convert to RGB if necessary
        # Thanks to Limodou on DjangoSnippets.org
        # http://www.djangosnippets.org/snippets/20/
        #
        # I commented this part since it messes up my png files
        #
        #if image.mode not in ('L', 'RGB'):
        #    image = image.convert('RGB')

        # We use our PIL Image object to create the thumbnail, which already
        # has a thumbnail() convenience method that contrains proportions.
        # Additionally, we use Image.ANTIALIAS to make the image look better.
        # Without antialiasing the image pattern artifacts may result.
        image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)
        middle_image.thumbnail(MIDDLE_SIZE, Image.ANTIALIAS)
        # Save the thumbnail
        temp_handle = StringIO()
        middle_temp_handle = StringIO()
        image.save(temp_handle, PIL_TYPE)
        middle_image.save(middle_temp_handle, PIL_TYPE)
        temp_handle.seek(0)
        middle_temp_handle.seek(0)

        # Save image to a SimpleUploadedFile which can be saved into
        # ImageField
        suf = SimpleUploadedFile(os.path.split(self.img.name)[-1],
            temp_handle.read(), content_type=DJANGO_TYPE)
        middle_suf = SimpleUploadedFile(os.path.split(self.img.name)[-1],
            middle_temp_handle.read(), content_type=DJANGO_TYPE)
        # Save SimpleUploadedFile into image field
        self.thumbnail.save('%s_thumbnail.%s'%(os.path.splitext(suf.name)[0],FILE_EXTENSION), suf, save=False)
        self.middle.save('%s_middle.%s'%(os.path.splitext(middle_suf.name)[0],FILE_EXTENSION), middle_suf, save=False)

    def save(self):
        # create a thumbnail
        if self.thumbnail == None or self.thumbnail == '':
            self.create_thumbnail()

        super(Picture, self).save()