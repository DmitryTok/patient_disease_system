from django.urls import path
from authentication.views import profile, login_user, logout_user, register


urlpatterns = [
    path('register/', view=register, name='register'),
    path('login/', view=login_user, name='login'),
    path('logout/', view=logout_user, name='logout'),
    path('profile/<int:user_id>', view=profile, name='profile'),
]
