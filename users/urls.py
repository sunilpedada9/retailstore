from django.conf.urls import url,include
from django.urls import path
from users.views import SignUp,UsersList,UserViewAndEdit
from django.views.generic import TemplateView

# Password issue https://github.com/iMerica/dj-rest-auth/issues/118 
urlpatterns=[
    url(r'^signup$',SignUp.as_view()),
    url(r'',include('rest_auth.urls')),
    url(r'^list$',UsersList.as_view()),
    url(r'^view&update/$',UserViewAndEdit.as_view()),
    path('password-reset/confirm/<uidb64>/<token>/', TemplateView.as_view(), name='password_reset_confirm') 
]
