from django.db import models

class Blog(models.Model):
    user = models.CharField(max_length=100)
    blog_title = models.CharField(max_length=100)
    blog_subtitle = models.CharField(max_length=100)
    content = models.TextField(max_length=5000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog_title

    #def snippet(self):
        #return self.content[:50] + '...'
