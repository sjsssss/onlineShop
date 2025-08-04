# from django.shortcuts import render
# from django.views.generic import TemplateView
# # Create your views here.

# class FrontendAppView(TemplateView):
#     template_name = "index.html"



from django.http import FileResponse
import os

def frontend(request):
    file_path = os.path.join('online_shop_backend', 'static', 'index.html')
    return FileResponse(open(file_path, 'rb'), content_type='text/html')
