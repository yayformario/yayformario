from django.db import models

# Create your models here.

"""
PageVisits is going to be a table
Going to have three columns:
1. HIdden 'id' column
2. 'path'
3. 'timestamp'

"""
class PageVisit(models.Model):

    #db -> table (db stored in a table)
    #Invisible column: 'id'
    #   id -> primary key -> autofield -> 1,2,3,4,5, etc...

    #Completely empty text field
    #blank = True
    #null = True
    path = models.TextField(blank=True, null=True) #col
    timestamp = models.DateTimeField(auto_now_add=True) #col
    pass

