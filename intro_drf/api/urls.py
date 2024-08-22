from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InstitutionsView

# router = DefaultRouter()
# router.register(r'mymodel', MyModelViewSet)

urlpatterns = [
    path('get-institution-sell', InstitutionsView.as_view(), name='get-institution-sell'),
]