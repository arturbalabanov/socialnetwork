from django.db import models
from django.utils import timezone

from users.models import UserProfile


class Post(models.Model):
    author = models.ForeignKey(UserProfile, related_name='timeline_posts')
    created = models.DateTimeField(default=timezone.now)
    text = models.TextField()
    likes = models.ManyToManyField(UserProfile, related_name='liked_timeline_posts')

    class Meta:
        ordering = ['-created']

    @property
    def number_of_likes(self):
        return self.likes.count()

    def like(self, user, commit=True):
        self.likes.add(user)

        if commit:
            self.save()
