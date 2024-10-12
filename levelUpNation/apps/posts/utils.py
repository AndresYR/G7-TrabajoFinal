import uuid

from django.utils.text import slugify


def generate_slug(string):
    id = str(uuid.uuid4())
    return slugify(f'{string}-{id[:6]}')

def set_slug(sender, instance, *args, **kwargs):
    if instance.slug:
        return
    
    slug = generate_slug(instance.titulo)

    while(sender.objects.filter(slug= slug).exists()):
        slug = generate_slug(instance.titulo)
    
    instance.slug = slug