from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.contenttypes.models import ContentType
from .models import Comment as Comment_Model
from invoice.models import invoice as invoice_model
# Create your views here.

def home(request):
    sample_object = invoice_model.objects.get(pk=1)


    #  ========> Create a comment for an object

    # sample_comment = Comment_Model(content_object=sample_object, comment_text='This invoice has an error')
    # sample_comment.save()



    #  ========> Get history of comments for an object 

    # my_model = type(sample_object)
    # object_content_type = ContentType.objects.get_for_model(my_model)
    # x = Comment_Model.objects.filter(content_type=object_content_type, object_id=sample_object.pk)
    # print(x)


    #  ========> Get the newest comment for an object 

    # my_model = type(sample_object)
    # object_content_type = ContentType.objects.get_for_model(my_model)
    # newest_comment = Comment_Model.objects.filter(content_type=object_content_type, object_id=sample_object.pk).latest()
    # print(newest_comment)

    return HttpResponse('Hello, this is a reusable commenting component')

