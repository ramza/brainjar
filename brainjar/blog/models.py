from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Model for our blog post, contains all the information about the post
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=256)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # set the date and commit to the database
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # pk is the PRIMARY KEY and is added automatically by DJANGO
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title
