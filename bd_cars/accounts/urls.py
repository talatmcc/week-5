from django.urls import path
from .views import SignupView, ProfileEditView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('profile/edit/', ProfileEditView.as_view(), name='edit_profile'),
]
