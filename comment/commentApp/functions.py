from .models import Comment as Comment_Model
from django.contrib.contenttypes.models import ContentType

def get_comments_history(object_instance):

    object_model = type(object_instance)
    object_content_type = ContentType.objects.get_for_model(object_model)
    history = Comment_Model.objects.filter(content_type=object_content_type, object_id=object_instance.pk)
    return history


def get_newest_comment(object_instance):

    object_model = type(object_instance)
    object_content_type = ContentType.objects.get_for_model(object_model)
    newest_comment = Comment_Model.objects.filter(content_type=object_content_type, object_id=object_instance.pk).latest()
    return newest_comment