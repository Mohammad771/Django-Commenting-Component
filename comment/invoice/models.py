from django.db import models

# Create your models here.

class invoice(models.Model):
    invoice_text = models.CharField(max_length=255)
    invoice_created_at = models.DateTimeField(auto_now_add=True)
    invoice_updated_at = models.DateTimeField(auto_now=True)

    # invoice_comments = GenericRelation(Comment)