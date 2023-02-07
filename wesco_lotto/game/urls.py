from django.urls import path,include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from .views import *
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from .views import *
schema_view = get_schema_view(
   openapi.Info(
      title="WESCO LOTTOHUB",
      default_version='v1',
      description="description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="gitech@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('api-token-auth/', obtain_jwt_token),
    path('api-refresh-token/', refresh_jwt_token),
    path('getgame/', getgameAPIview.as_view()),
    path('cancelticket/', cancelticketviewset.as_view()),
    path('checkwinner/', checkwinnerviewset.as_view()),
    path('ticketstatus/', ticketstatusviewset.as_view()),
    path('updatewinner/', Updatewinnerviewset.as_view()),
    path('sellticket/', sellticketviewset.as_view()),
    path('winnerlist/', winnerlistviewset.as_view()),
    path('swagger/', schema_view.with_ui('swagger')),
    path('swaggerdocs/', schema_view.with_ui('redoc')),
]
