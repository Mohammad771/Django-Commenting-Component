from .models import Comment as Comment_Model
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

def get_comments_history(object_instance):

    object_model = type(object_instance)
    object_content_type = ContentType.objects.get_for_model(object_model)
    history = Comment_Model.active_comments.filter(content_type=object_content_type, object_id=object_instance.pk)
    return history


def get_newest_comment(object_instance):

    object_model = type(object_instance)
    object_content_type = ContentType.objects.get_for_model(object_model)
    newest_comment = Comment_Model.active_comments.filter(content_type=object_content_type, object_id=object_instance.pk).latest()
    return newest_comment

def update_comment(comment_instance, current_user, new_comment_text):

    if (comment_instance.comment_creator == current_user):
        comment_instance.comment_text = new_comment_text
        comment_instance.save()
        return True

    else:
        print("Unauthorized update request, only the comment's creator can update this comment")
        return False

def delete_comment(comment_instance, current_user):

    if (comment_instance.comment_creator == current_user):
        comment_instance.comment_deleted_at = timezone.now()
        comment_instance.save()
        return True

    else:
        print("Unauthorized delete request, only the comment's creator can delete this comment")
        return False
    

