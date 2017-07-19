from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        ordering = ['name']

    def __str__(self):
        return self.name

class PublicBoozManager(models.Manager):
    def get_queryset(self):
        qs = super(PublicBoozManager, self).get_queryset()
        return qs.filter(is_public=True)


class Booz(models.Model):
    subject_matter = models.CharField(max_length=50,verbose_name='Title')
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField('public', default=True)
    owner = models.ForeignKey(User, verbose_name='owner',related_name='boozs')
    via = models.URLField(blank=True,
            verbose_name='(optional)web address for further verification(e.g http://bobos-booboos.com)')
    tags = models.ManyToManyField(Tag, blank=True)

    objects = models.Manager()
    public = PublicBoozManager()

    class Meta:
        verbose_name = 'booz'
        verbose_name_plural = 'boozs'
        ordering = ['-created_on']

    def total_likes(self):
        return self.like_set.count()

    def __str__(self):
        return self.subject_matter


class Like(models.Model):
    booz = models.ForeignKey(Booz,related_name='likes')
    approved_like = models.BooleanField(default=False)

    def approve(self):
        self.approved_like = True
        self.save()


class Comment(models.Model):
    booz = models.ForeignKey('booz.Booz', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
