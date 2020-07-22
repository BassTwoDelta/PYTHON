from django.db import models
import bcrypt

# Create your models here.
class regManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['name']) < 3:
            erros['name'] = "Name must be at least 3 characters"
        if len(postData['username']) < 3:
            erros['username'] = "Username must be at least 3 characters"
        if len(postData['password']) < 8:
            errors['password'] = "*Password should be at least 8 characters"
        if postData['password'] != postData['confirm_pw']:
            errors['confirm_pw'] = "Passwords do not match"
        if len(User.objects.filter(username=postData['username'])) != 0:
            errors['username'] = "Usernane is already registered"
        return errors

    def validatorLogin(self, postData):
        errors = {}
        user = User.objects.filter(username=postData['username_login'])
        if len(user) == 0:
            errors["username_login"] = "Username not found"
        else: 
            logged_user = user[0]
            if not bcrypt.checkpw(postData['password_login'].encode(), logged_user.password.encode()):
                errors['password_login'] = "Password is incorrect"
        return errors

class itemManager(models.Manager):
    def itemValidator(self, postData):
        errors = {}
        if len(postData["add_item"]) ==0:
            errors["add_item"] = "You must enter an item name!"
        if len(postData['add_item']) < 3:
            errors['add_item'] = "Item must have at least 3 characters"
        return errors

        
class User(models.Model):
    name = models.CharField(max_length=60)
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    date_hired = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = regManager()

class Item(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, related_name="wish_list", on_delete=models.CASCADE)
    favoritors = models.ManyToManyField(User, related_name="wish_items")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = itemManager()



