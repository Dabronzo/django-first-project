from django.db import models

# Create your models here.


class Itens(models.Model):
    """ Model class to create the itens for the database
    Notice that null=false means that the name need to have a value
    and can not be an empty value"""
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    # here we gonna rewrite on function in the model documentation
    #  to display a better name of the item
    # in the admin page

    def __str__(self):
        return f"{self.name}"
