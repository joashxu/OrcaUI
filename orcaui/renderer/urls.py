from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    # Accordion
    path("accordions/default",
         TemplateView.as_view(template_name="components/accordions/accordion_default.html")),
    path("accordions/preselected",
         TemplateView.as_view(template_name="components/accordions/accordion_preselected.html")),

]
