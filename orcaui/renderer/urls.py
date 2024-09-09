from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    # Accordion
    path("accordions/default",
         TemplateView.as_view(template_name="components/accordions/accordion_default.html")),
    path("accordions/preselected",
         TemplateView.as_view(template_name="components/accordions/accordion_preselected.html")),
    # Avatar
    path("avatars/default",
         TemplateView.as_view(template_name="components/avatars/avatar_default.html")),
    path("avatars/ring",
         TemplateView.as_view(template_name="components/avatars/avatar_with_ring.html")),
    path("avatars/sizes",
         TemplateView.as_view(template_name="components/avatars/avatar_sizes.html")),
    path("avatars/group",
         TemplateView.as_view(template_name="components/avatars/avatar_group.html")),
    path("avatars/online-offline",
         TemplateView.as_view(template_name="components/avatars/avatar_online_offline.html")),
]
