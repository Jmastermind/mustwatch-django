from django import forms, template
from django.utils.safestring import SafeText

register = template.Library()


@register.simple_tag
def form_tag(
    field: forms.BoundField,
    name: SafeText,
    par: SafeText,
) -> SafeText:
    return field.as_widget(attrs={name: par})
