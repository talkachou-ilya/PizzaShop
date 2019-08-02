from django.db import models
from django.contrib.auth.models import User


class PizzaShop( models.Model ):
	owner = models.OneToOneField( User, on_delete = models.CASCADE, related_name = 'PizzaShop' )
	name = models.CharField( max_length = 100 )
	phone = models.CharField( max_length = 100 )
	address = models.CharField( max_length = 100 )
	logo = models.ImageField( upload_to = 'pizza_shop_logo', blank = False )

	def __str__ ( self ):
		return self.name


class Pizza( models.Model ):
	pizza_shop = models.ForeignKey( PizzaShop, on_delete = models.CASCADE )
	name = models.CharField( max_length = 30 )
	short_description = models.CharField( max_length = 100 )
	image = models.ImageField( upload_to = 'pizza_image', blank = False )
	price = models.IntegerField( default = 0 )

	def __str__ ( self ):
		return self.name


class Client( models.Model ):
	user = models.OneToOneField( User, on_delete = models.CASCADE, related_name = 'client' )
	avatar = models.CharField( max_length = 500 )
	phone = models.CharField(max_length = 20, blank = True)
	address =  models.CharField(max_length = 30, blank = True)

	def __str__(self):
		return self.user.get_full_name()
