from django.db import models
from login_reg_app.models import User

# Create your models here.
class messages(models.Model):
    user = models.ForeignKey(User, related_name="messages", on_delete= models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class comments(models.Model):
    user = models.ForeignKey(User, related_name="comments", on_delete= models.CASCADE)
    message = models.ForeignKey(messages, related_name="comments", on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

