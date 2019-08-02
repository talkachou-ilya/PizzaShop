from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from .forms import UserForm, PizzaShopForm, UserFormForEdit, PizzaForm
from django.contrib.auth.models import User

from .models import Pizza


def home ( request ):
	return redirect( shop )


#
@login_required( login_url = '/sign-in/' )
def shop ( request ):
	return redirect( pizza_page )


# Зарегистрироваться
def sign_up ( request ):
	user_form = UserForm()
	pizza_shop_form = PizzaShopForm()

	if request.method == 'POST':
		user_form = UserForm( request.POST )
		pizza_shop_form = PizzaShopForm( request.POST, request.FILES )

		if user_form.is_valid() and pizza_shop_form.is_valid():
			new_user = User.objects.create_user( **user_form.cleaned_data )
			new_pizza_shop = pizza_shop_form.save( commit = False )
			new_pizza_shop.owner = new_user
			new_pizza_shop.save()
			user = authenticate(
				username = user_form.cleaned_data[ 'username' ],
				password = user_form.cleaned_data[ 'password' ]
			)

			login( request, user )

			return redirect( home )

	return render( request, 'PizzaShopApp/sign-up.html', {
		'pizza_shop_form': pizza_shop_form,
		'user_form': user_form
	} )


# Профиль
@login_required( login_url = '/sign-in/' )
def account ( request ):
	user_form = UserFormForEdit( instance = request.user )
	pizza_shop_form = PizzaShopForm( instance = request.user.PizzaShop )

	if request.method == 'POST':
		user_form = UserFormForEdit( request.POST, instance = request.user )
		pizza_shop_form = PizzaShopForm( request.POST, request.FILES, instance = request.user.PizzaShop )

		if user_form.is_valid() and pizza_shop_form.is_valid():
			user_form.save()
			pizza_shop_form.save()

	return render( request, 'PizzaShopApp/account.html', {
		'pizza_shop_form': pizza_shop_form,
		'user_form': user_form
	} )


# Все пиццы
@login_required( login_url = '/sign-in/' )
def pizza_page ( request ):
	pizzas = Pizza.objects.filter( pizza_shop = request.user.PizzaShop ).order_by( '-id' )

	return render( request, 'PizzaShopApp/pizza.html', {
		'pizzas': pizzas
	} )


# Добавить пиццу
@login_required( login_url = '/sign-in/' )
def add_pizza ( request ):
	form = PizzaForm()
	if request.method == 'POST':
		form = PizzaForm( request.POST, request.FILES )
		if form.is_valid():
			pizza = form.save( commit = False )
			pizza.pizza_shop = request.user.PizzaShop
			pizza.save()

			return redirect( pizza_page )

	return render( request, 'PizzaShopApp/add_pizza.html', {
		'form': form
	} )


def edit_pizza ( request, pizza_id ):
	form = PizzaForm( instance = Pizza.objects.get( id = pizza_id ) )
	if request.method == 'POST':
		form = PizzaForm( request.POST, request.FILES, instance = Pizza.objects.get( id = pizza_id ) )
		if form.is_valid():
			form.save()
			

			return redirect( pizza_page )

	return render( request, 'PizzaShopApp/edit_pizza.html', {
		'form': form
	} )
