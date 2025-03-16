from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_GET

from short_link.models import LinkMapped


@require_GET
def load_url(request, url_hash: str) -> HttpResponse:
    """Перенаправление на оригинальную ссылку."""

    original_url = get_object_or_404(
        LinkMapped, url_hash=url_hash
    ).original_url
    return redirect(original_url)
