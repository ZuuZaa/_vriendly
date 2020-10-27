from django.urls import path
from account.views import (
            register_view,
            activate_view, 
            login_view, 
            logout_view,
            password_reset_view,
            password_reset_done_view,
            password_confirm_view,
            profile_view,
            user_profile_view,
            profile_edit_view,
)

urlpatterns = [
    path('register', register_view, name='register'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name="logout"),
    path('activate/<int:uid>/<str:token>', activate_view, name='activate'),
    path('password/reset', password_reset_view, name='password_reset'),
    path('password/reset/done', password_reset_done_view, name='password_reset_done'),
    path('password/<int:uid>/<str:token>', password_confirm_view, name='password_confirm'),

    path('profile', profile_view, name='profile'),
    path('profile/edit', profile_edit_view, name='profile_edit'),
    path('profile/<int:uid>', user_profile_view, name='user_profile'),
]
