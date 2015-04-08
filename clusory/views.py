from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from rest_framework import permissions, viewsets

from clusory.models import Debate
from clusory.permissions import IsAuthorOrReadOnly
from clusory.serializers import DebateSerializer, UserSerializer


@csrf_protect
@ensure_csrf_cookie
def index(request):
    user = authenticate(username='zra', password='zra')
    if user is not None:
        login(request, user)
        return render(request, 'clusory/index.html')


class DebatesViewSet(viewsets.ModelViewSet):
    queryset = Debate.objects.all()
    serializer_class = DebateSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly,)

    def pre_save(self, obj):
        obj.user = self.request.user


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
