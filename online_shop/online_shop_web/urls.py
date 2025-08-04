"""
URL configuration for online_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path, include
from django.conf.urls.static import static

urlpatterns = [
    # ... 你的 API 路由
    # re_path(r'^.*$', TemplateView.as_view(template_name="index.html")),  # 捕获所有路径
    path('', include('online_shop_backend.urls')),
]

from django.conf import settings

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
