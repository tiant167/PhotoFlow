from django.db import models

# Create your models here.
class BlogManager(models.Manager):
    def get_blog_list(self):
        '''
        returns the list of all blogs.

        content is cutted
        '''
        blogs = self.all()
        for blog in blogs:
            if len(blog.content) > 100:
                blog.content = blog.content[:100] + '...'
        return blogs


class Blog(models.Model):
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=300,blank=True,null=True)
    abstract = models.TextField()
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    pinned = models.BooleanField(default=False)
    tags = models.ManyToManyField('Tag',blank=True,null=True)

    objects = BlogManager()

    def __unicode__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=300)
    color = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name