from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User
# Create your models here.

class Active_comments_manager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(comment_deleted_at=None)


class Comment(models.Model):
    comment_text = models.CharField(max_length=255)
    comment_creator = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    comment_created_at = models.DateTimeField(auto_now_add=True)
    comment_updated_at = models.DateTimeField(auto_now=True)
    comment_deleted_at = models.DateTimeField(null=True, blank= True, default=None)

    content_type = models.ForeignKey(ContentType, blank=True, null=True, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    objects = models.Manager() 
    active_comments = Active_comments_manager() 

    def __str__(self):
        return self.comment_text

    class Meta:
        get_latest_by = ['comment_created_at']



    