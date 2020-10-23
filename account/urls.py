from django.urls import path
from account.views import (
            register_view,
            activate_view, 
            login_view, 
            logout_view,
            profile_view,
            profile_edit_view,
)

urlpatterns = [
    path('register', register_view, name='register'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name="logout"),
    path('activate/<int:uid>/<str:token>', activate_view, name='activate'),

    path('profile', profile_view, name='profile'),
    path('profile/edit', profile_edit_view, name='profile_edit')
]
