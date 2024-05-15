"""
URL configuration for yummy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.contrib import admin
from django.urls import include, path

from django.urls import path, include
from django.conf import settings

from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from users.views import CustomLoginView

from users.forms import LoginForm

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('dashboard/', include(('dashboard.urls', 'dashboard'), namespace='dashboard')),
    path('users/', include('users.urls')),
    path('restaurants/', include(('restaurants.urls',
         'restaurants'), namespace='restaurants')),
    path('menus/', include(('menus.urls', 'menus'), namespace='menus')),
    path('orders/', include(('orders.urls', 'orders'), namespace='orders')),
    path('contacts/', include(('contacts.urls', 'contacts'), namespace='contacts')),


    # added by mash      # need to remove this --> comment by naqibullah
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='users/login.html',                                        authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# ended by mash
