import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response

from core.models import Url
from core.serializers import UrlSerializer


class UrlViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return an Url instance.
    list:
        Return all Urls.
    create:
        Create a new Url.
    delete:
        Remove an existing Url.
    partial_update:
        Update one or more fields on an existing Url.
    update:
        Update one or more fields on an existing Url.
    """
    queryset = Url.objects.all()
    serializer_class = UrlSerializer

    def get_queryset(self, *args, **kwargs):
        """
        Search by url fields (url, short_url or user).
        """
        if self.request.query_params:
            data = {}
            for param in self.request.query_params:
                _param = self.request.query_params.get(param, '')
                if param in ['url', 'short_url'] and _param != '':
                    data[param + '__icontains'] = _param

                if param == 'user' and _param != '':
                    data[param] = _param

            return Url.objects.filter(**data)

        return Url.objects.all()


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def get_url(request, pk):
    queryset = Url.objects.all()
    url = get_object_or_404(queryset, pk=pk)

    if datetime.datetime.now() > url.expire_at.replace(tzinfo=None):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    redirect_url = url.url if url.url[:8].lower() == 'https://' or url.url[:8].lower() == 'http://' else 'https://{0}'\
        .format(url.url)
    return HttpResponseRedirect(redirect_url)
