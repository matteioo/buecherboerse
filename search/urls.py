from django.urls import path, include
from rest_framework.routers import DefaultRouter
#from .views import SellerViewSet  # Assuming TransactionViewSet is commented out for now
from .views import LogoutAPIView, CurrentUserAPIView, OfferListAPIView, SellerViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
# offer endpoints
#router.register(r'offers', OfferListAPIView.as_view(), basename="offer")
router.register(r'sellers', SellerViewSet, basename="seller")
# todo: add transaction adding via api


# router.register(r'sellers', SellerViewSet)
# router.register(r'transactions', TransactionViewSet)  # Commented out for now

urlpatterns = [
    path('offers', OfferListAPIView.as_view(), name="offer_filter"),
    path('', include(router.urls)),
    path('api/auth/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/logout', LogoutAPIView.as_view(), name='auth_logout'),
    path('api/auth/user', CurrentUserAPIView.as_view(), name='auth_user'),
]
