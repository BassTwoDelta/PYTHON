from django.db import models

# Create your models here.
class TitanicPassengers(models.Model):
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    gender = models.TextField(db_column='Gender', blank=True, null=True)  # Field name made lowercase.
    class_dept = models.TextField(db_column='Class/Dept', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cabin = models.TextField(db_column='Cabin', blank=True, null=True)  # Field name made lowercase.
    joined = models.TextField(db_column='Joined', blank=True, null=True)  # Field name made lowercase.
    occupation = models.TextField(db_column='Occupation', blank=True, null=True)  # Field name made lowercase.
    survived_field = models.TextField(db_column='Survived?', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    boat = models.TextField(db_column='Boat', blank=True, null=True)  # Field name made lowercase.
    body = models.TextField(db_column='Body', blank=True, null=True)  # Field name made lowercase.
    url = models.TextField(db_column='URL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'titanic_passengers'