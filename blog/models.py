from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.

#post model
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    title = models.CharField(max_length = 256)
    text = models.TextField()
    create_date = models.DateTimeField(timezone.now())
    publish_date = models.DateTimeField(blank = True, null = True)

    #publishing
    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    #where to go after publishing post
    def get_absolute_url(self):
        return reverse('post_detail', kwargs = {'pk':self.pk})

    #showing approved comments
    def approveComments(self):
        return self.comments.filter(approved_comment = True)

    #string representation of the post object
    def __str__(self):
        return self.title


#comment class model
class Comment(models.Model):
    author = models.CharField(max_length = 100)
    post = models.ForeignKey('blog.Post', related_name = 'comments', on_delete = models.CASCADE)
    text = models.TextField()
    create_date = models.DateTimeField(timezone.now())
    approved_comment = models.BooleanField(default = False)


    def approve(self):
        self.approved_comment = True
        slef.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text
