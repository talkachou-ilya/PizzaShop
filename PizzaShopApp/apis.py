from django.http import JsonResponse

from .serializers import PizzaShopSerializer, PizzaSerializer
from .models import PizzaShop, Pizza


def client_get_pizza_shops ( request ):
	pizza_shops = PizzaShopSerializer(
		PizzaShop.objects.all().order_by( '-id' ),
		many = True,
		context = { 'request': request },
	).data

	return JsonResponse( { 'pizza_shops': pizza_shops } )


def client_get_pizzas ( request, pizza_shop_id ):
	pizzas = PizzaSerializer(
		Pizza.objects.all().filter( pizza_shop_id = pizza_shop_id ).order_by( '-id' ),
		many = True,
		context = { 'request': request },
	).data
	return JsonResponse( { 'pizzas': pizzas } )
