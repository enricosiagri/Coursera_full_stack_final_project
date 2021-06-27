from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL
    path('home/', views.home_request, name='home'),
    path('about/', views.about_us_request, name='about'),
    path('contacts/', views.contact_us_request, name='contacts'),
    path('registration/', views.registration_request, name='registration'),
    path('details/', views.get_dealer_details, name='details'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path(route='', view=views.get_dealerships, name='index'),
    # path for about view

    # path for contact us view

    # path for registration

    # path for login

    # path for logout

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
