from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import mixins
from rest_framework import generics


class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    # GenericAPIView for core functionality
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    # from list mixin
    # explicitly bind get method to appropriate action
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # from create mixin
    # explicitly bind post method to appropriate action
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    # GenericAPIView for core functionality
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    # from retrieve mixin
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    # from update mixin
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # from destroy mixin
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
