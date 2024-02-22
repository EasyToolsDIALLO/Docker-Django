from django.urls import re_path, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, include

from ocr_api import views

schema_view = get_schema_view(
    openapi.Info(
        title="OCR API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('v1/', include([
         path('docs/', schema_view.with_ui('swagger',
                                           cache_timeout=0), name='schema-swagger-ui'),

            # factures
             path('factures/', views.FactureAPIView.as_view()),
             path('factures/<str:id>', views.FactureByIdAPIView.as_view()),
             
            # produits
             path('produits/', views.ProduitAPIView.as_view()),
             path('produits/<str:id>', views.ProduitByIdAPIView.as_view()),
             
             # extraction
             path('extract_facture/', views.ExtractionFactureAPIView.as_view()),
             
         ])
         )



]
