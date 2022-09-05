from django.db import models

# Create your models here.

class product(models.Model):
    product_text = models.CharField(max_length=255)
    product_created_at = models.DateTimeField(auto_now_add=True)
    product_updated_at = models.DateTimeField(auto_now=True)

    # product_comments = GenericRelation(Comment)