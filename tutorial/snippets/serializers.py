from rest_framework import serializers
from django.contrib.auth.models import User
from snippets.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id',
                  'title',
                  'code',
                  'line_numbered',
                  'language',
                  'style',
                  'owner')

    # snippets are associated with owners
    owner = serializers.ReadOnlyField(source='owner.username')


class UserSerializer(serializers.ModelSerializer):
    """Represent users in API."""
    snippets = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Snippet.objects.all()
    )

    class Meta:
        model = User
        """
        'snippets' is a reverse relationship on user model, and will not be
        included by default. We must add an explicit field for it.

        """
        fields = ('id', 'username', 'snippets')
