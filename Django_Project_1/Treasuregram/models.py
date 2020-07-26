from django.db import models

# Create your models here.
""" *
    *   we will create a Treasure model with same attributes as our Treasure class, but using the below steps
    *
    *   Treasure class inherits from models.Model so that Django knows we are creating a model
    *
    *   we will use special type of model types that corresponds to database types
    *
    *   if you notice we don't have to create a constructor in our treasure model because the model has one built in 
    *   where you use th attribute names to set each one 
    *
    *   when we create a model and model objects in Django, we are actually creating a database table and database 
    *   entries but we don't have to writs any sql, because Django ORM(Object Relational Mapping) translates the Python 
    *   code to SQL for us behind the scenes, it will automatically translate the python commands to sql commands 
    *   unless you edit the structure of your model then you need to do extra step called migration.
    *
    *   we will need to do it now since we just created a model
    * """
class Treasure(models.Model):

    name = models.CharField(max_length=256)
    value = models.CharField(max_length=256)
    material = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.name}, {self.value}"