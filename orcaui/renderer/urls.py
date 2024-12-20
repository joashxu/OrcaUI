from django.urls import path
from django.views.generic import TemplateView

# Buttons
urlpatterns_button = [
    path("buttons/default", TemplateView.as_view(template_name="components/buttons/button_default.html")),
    path("buttons/state-color", TemplateView.as_view(template_name="components/buttons/button_state_color.html")),
    path("buttons/modifier", TemplateView.as_view(template_name="components/buttons/button_with_modifier.html")),
    path("buttons/sizes", TemplateView.as_view(template_name="components/buttons/button_sizes.html")),
    path("buttons/icons", TemplateView.as_view(template_name="components/buttons/icon_button.html")),
    path("buttons/icons-shape", TemplateView.as_view(template_name="components/buttons/icon_button_shape.html")),
    path("buttons/icons-shape-modifier", TemplateView.as_view(template_name="components/buttons/icon_button_shape_modifier.html")),
    path("buttons/with-icon", TemplateView.as_view(template_name="components/buttons/button_with_icon.html")),
    path("buttons/states", TemplateView.as_view(template_name="components/buttons/button_states.html")),
    path("buttons/loading", TemplateView.as_view(template_name="components/buttons/button_loading.html")),
    path("buttons/link", TemplateView.as_view(template_name="components/buttons/link_as_button.html")),
]

# Modal
urlpatterns_modal = [
    path("modals/default", TemplateView.as_view(template_name="components/modals/modal_default.html")),
    path("modals/remote-url", TemplateView.as_view(template_name="components/modals/modal_remote_url.html")),
    path("modals/error-handling", TemplateView.as_view(template_name="components/modals/modal_error_handling.html")),
    path("modals/size", TemplateView.as_view(template_name="components/modals/modal_size.html")),
    path("modals/detached", TemplateView.as_view(template_name="components/modals/modal_detached.html")),
]

# Accordions
urlpatterns_accordion = [
    path("accordions/default", TemplateView.as_view(template_name="components/accordions/accordion_default.html")),
    path("accordions/preselected", TemplateView.as_view(template_name="components/accordions/accordion_preselected.html")),
]

# Avatars
urlpatterns_avatar = [
    path("avatars/default", TemplateView.as_view(template_name="components/avatars/avatar_default.html")),
    path("avatars/ring", TemplateView.as_view(template_name="components/avatars/avatar_with_ring.html")),
    path("avatars/sizes", TemplateView.as_view(template_name="components/avatars/avatar_sizes.html")),
    path("avatars/group", TemplateView.as_view(template_name="components/avatars/avatar_group.html")),
    path("avatars/online-offline", TemplateView.as_view(template_name="components/avatars/avatar_online_offline.html")),
]

# Badges
urlpatterns_badge = [
    path("badges/brand-color", TemplateView.as_view(template_name="components/badges/badge_brand_color.html")),
    path("badges/outline", TemplateView.as_view(template_name="components/badges/badge_outline.html")),
    path("badges/sizes", TemplateView.as_view(template_name="components/badges/badge_sizes.html")),
    path("badges/empty", TemplateView.as_view(template_name="components/badges/badge_empty.html")),
    path("badges/state-color", TemplateView.as_view(template_name="components/badges/badge_state_color.html")),
    path("badges/in-text", TemplateView.as_view(template_name="components/badges/badge_in_text.html")),
    path("badges/in-button", TemplateView.as_view(template_name="components/badges/badge_in_button.html")),
]

# Cards
urlpatterns_card = [
    path("card/default", TemplateView.as_view(template_name="components/cards/card_default.html")),
    path("card/top-image", TemplateView.as_view(template_name="components/cards/card_top_image.html")),
    path("card/bottom-image", TemplateView.as_view(template_name="components/cards/card_bottom_image.html")),
    path("card/horizontal", TemplateView.as_view(template_name="components/cards/card_horizontal.html")),
    path("card/showcase", TemplateView.as_view(template_name="components/cards/card_showcase.html")),
]

# Kbd
urlpatterns_kbd = [
    path("kbd/default", TemplateView.as_view(template_name="components/kbd/kbd_default.html")),
    path("kbd/sizes", TemplateView.as_view(template_name="components/kbd/kbd_sizes.html")),
    path("kbd/in-text", TemplateView.as_view(template_name="components/kbd/kbd_in_text.html")),
    path("kbd/combination", TemplateView.as_view(template_name="components/kbd/kbd_combi.html")),
    path("kbd/function-key", TemplateView.as_view(template_name="components/kbd/kbd_function_key.html")),
]



urlpatterns = urlpatterns_button + urlpatterns_modal
urlpatterns += urlpatterns_accordion + urlpatterns_avatar
urlpatterns += urlpatterns_badge + urlpatterns_card
urlpatterns += urlpatterns_badge + urlpatterns_kbd
