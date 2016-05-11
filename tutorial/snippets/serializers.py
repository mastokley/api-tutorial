from rest_framework import serializers
from django.contrib.auth.models import User
from snippets.models import Snippet


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name='snippet-highlight',
        format='html'
    )

    class Meta:
        model = Snippet
        fields = ('url',
                  'highlight',
                  'owner',
                  'title',
                  'code',
                  'line_numbered',
                  'language',
                  'style')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True,
                                                   view_name='snippet-detail',
                                                   read_only=True)

    class Meta:
        model = User
        """
        'snippets' is a reverse relationship on user model, and will not be
        included by default. We must add an explicit field for it.
        """
        fields = ('url', 'username', 'snippets')
