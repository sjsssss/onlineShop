# online_shop_web/urls.py

# from django.urls import path
# from .views import FrontendAppView

# urlpatterns = [
#     path("", FrontendAppView.as_view(), name='home'),
# ]



from django.urls import path
from .views import frontend

urlpatterns = [
    path('', frontend),
]
