# urls.py
from django.urls import path
from qr_code_generator.views import generate_qr_code  # Import your view function

urlpatterns = [
    path('', generate_qr_code, name='generate_qr_code'),  # Define a URL pattern for the root URL

]