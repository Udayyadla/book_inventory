from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet,AuthViewSet
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


router = DefaultRouter()
router.register(r"books", BookViewSet)
router.register(r'auth',AuthViewSet,basename='auth')


urlpatterns = [
    path('token/',TokenObtainPairView.as_view(),name="token_obtain_pair"),#Login
    path("token/refresh/",TokenRefreshView.as_view(),name="token_refresh"), #Refresh Token
    path("", include(router.urls)),  # Include Router URLS
]
