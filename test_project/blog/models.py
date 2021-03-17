import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    post_uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    # this function is needed, so that the CreateView class is able to redirect 
    # to the url specified in the reverse function
    def get_absolute_url(self):
        return reverse('Post-Detail', kwargs={'pk': self.pk})