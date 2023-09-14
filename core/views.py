from http import HTTPStatus

from django.core import exceptions
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from core.forms import CreationForm


def csrf_failure(request: HttpRequest, reason: str = '') -> HttpResponse:
    del reason
    return render(request, 'core/403csrf.html')


def page_not_found(
    request: HttpRequest,
    exception: Http404,
) -> HttpResponse:
    del exception
    return render(
        request,
        'core/404.html',
        status=HTTPStatus.NOT_FOUND,
    )


def permission_denied(
    request: HttpRequest,
    exception: exceptions.PermissionDenied,
) -> HttpResponse:
    del exception
    return render(
        request,
        'core/403.html',
    )


def bad_request(
    request: HttpRequest,
    exception: exceptions.BadRequest,
) -> HttpResponse:
    del exception
    return render(
        request,
        'core/400.html',
    )


def server_error(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        'core/500.html',
        status=HTTPStatus.INTERNAL_SERVER_ERROR,
    )


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('movies:home')
    template_name = 'registration/signup.html'
