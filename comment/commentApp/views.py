from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Comment as Comment_Model
from .functions import *
from invoice.models import invoice as invoice_model
# Create your views here.

def home(request):
    sample_object = invoice_model.objects.get(pk=1)
    
    #  ========> Create a comment for an object

    # sample_comment = Comment_Model(content_object=sample_object, comment_text='This is a new comment', comment_creator=request.user)
    # sample_comment.save()



    #  ========> Get history of comments for an object 

    # print(get_comments_history(sample_object))



    #  ========> Get the newest comment for an object 

    # print(get_newest_comment(sample_object))
    
    return HttpResponse('Hello, this is a reusable commenting component')

