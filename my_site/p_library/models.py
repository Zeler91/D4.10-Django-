from django.db import models

# Create your models here.
  
class Author(models.Model):  
    full_name = models.TextField()  
    birth_year = models.SmallIntegerField()  
    country = models.CharField(max_length=2)

    def __str__(self):
        return "{self.full_name}".format(self = self) 

class Redaction(models.Model):
    name = models.TextField()
    creation_year = models.SmallIntegerField()
    description = models.TextField()
    
    def __str__(self):
        return "{self.name}".format(self = self) 


class Friend(models.Model):
    name = models.TextField()

    def __str__(self):
        return "{self.name}".format(self = self)

class Book(models.Model):  
    ISBN = models.CharField(max_length=13)  
    title = models.TextField()  
    description = models.TextField()  
    year_release = models.SmallIntegerField()  
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    redaction = models.ForeignKey(Redaction, on_delete=models.CASCADE)
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE, blank = True, null = True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    copy_count = models.SmallIntegerField(default = 1)
    image = models.ImageField(upload_to='book_images/', blank=True)

    def __str__(self):
        return "{self.title} ".format(self = self) 
