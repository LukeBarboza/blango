from django.contrib.auth import get_user_model
user_model = get_user_model()

from django import template

from django.utils.html import escape
from django.utils.safestring import mark_safe

# Create an instance of the Library class
register = template.Library()

# Define your custom filter function
@register.filter
def author_details(author, current_user):

  #Checking if the author is a USER
  if not isinstance(author, user_model):
    return ""

  if author == current_user:
    return mark_safe(f"<strong>me</strong>")

  prefix = f'<a href="mailto:f{author.email}">'
  suffix = f'</a>'
  
  name = f"{author.first_name} {author.last_name}" if author.last_name else f"{author.username}"

  return mark_safe(f"{prefix}{name}{suffix}")
