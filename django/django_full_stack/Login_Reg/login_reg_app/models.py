from django.db import models
import re
import bcrypt

# Create your models here.
class regManager(models.Manager):
    def validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name'])< 2:
            errors['first_name'] = "First name should be at least 2 characters"
        if len(postData['last_name'])< 2:
            errors['first_name'] = "Last name should be at least 2 characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address"
        if len(postData['password']) < 8:
            errors['password'] = "Password too short, must be 8 characters"
        if postData['password'] != postData['confirm_pw']:
            errors['confirm_pw'] = "Passwords do not match"
        if len(User.objects.filter(email=postData['email'])) != 0:
            errors['email'] = "Email already registered"
        return errors
    
    def validatorLogin(self, postData):
        errors = {}
        user = User.objects.filter(email=postData['user_email'])
        if len(user) == 0:
            errors["user_email"] = "Email is not found"
        else: 
            logged_user = user[0]
            if not bcrypt.checkpw(postData['password_login'].encode(),     logged_user.password.encode()):
                errors['password_login'] = "Password is incorrect"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = regManager()
