from django.urls import path, include
from . import views, apis
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
	path( '', views.home, name = 'home' ),
	path( 'shop/', views.shop, name = 'shop' ),
	path( 'sign-in/', LoginView.as_view( template_name = 'PizzaShopApp/sign-in.html' ), name = 'sign-in' ),
	path( 'sign-out/', LogoutView.as_view( next_page = '/' ), name = 'sign-out' ), path( 'shop/', views.shop, name = 'shop' ),
	path( 'sign-up/', views.sign_up, name = 'sign-up' ),
	path( 'account/', views.account, name = 'account' ),
	path( 'pizza/', views.pizza_page, name = 'pizza' ),
	path( 'pizza/add/', views.add_pizza, name = 'add_pizza' ),
	path( 'pizza/edit/<int:pizza_id>/', views.edit_pizza, name = 'edit_pizza' ),

	# APIs
	path( 'api/client/pizza-shops/', apis.client_get_pizza_shops ),
	path( 'api/client/pizzas/<int:pizza_shop_id>/', apis.client_get_pizzas ),

	# Facebook OAuth2
	path( 'api/social/', include( 'rest_framework_social_oauth2.urls' ) ),

	# /convert-token (sign-in / sign-up)
	# /revoke-token (sign-out)

]
