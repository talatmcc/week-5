from django.urls import path
from .views import HomeView, CarListView, CarDetailView, PurchaseView, ProfileView,edit_profile
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    # path('car/<int:pk>/comment/', CommentCreateView.as_view(), name='comment_create'),
    path('cars/<int:brand_id>/', CarListView.as_view(), name='car_list'),
    path('cars/purchase/<int:pk>/', PurchaseView.as_view(), name='purchase_car'),
    path('accounts/profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)