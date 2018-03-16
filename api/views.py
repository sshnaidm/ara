#  Copyright (c) 2018 Red Hat, Inc.
#
#  This file is part of ARA Records Ansible.
#
#  ARA is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  ARA is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with ARA.  If not, see <http://www.gnu.org/licenses/>.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from api import models, serializers

from rest_framework import generics


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'playbooks': reverse('playbook-list', request=request, format=format),
        'plays': reverse('play-list', request=request, format=format),
        'tasks': reverse('task-list', request=request, format=format),
        'files': reverse('file-list', request=request, format=format)
    })


class PlaybookList(generics.ListCreateAPIView):
    queryset = models.Playbook.objects.all()
    serializer_class = serializers.PlaybookSerializer


class PlaybookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Playbook.objects.all()
    serializer_class = serializers.PlaybookSerializer


class PlayList(generics.ListCreateAPIView):
    queryset = models.Play.objects.all()
    serializer_class = serializers.PlaySerializer


class PlayDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Play.objects.all()
    serializer_class = serializers.PlaySerializer


class TaskList(generics.ListCreateAPIView):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer


class FileList(generics.ListCreateAPIView):
    queryset = models.File.objects.all()
    serializer_class = serializers.FileSerializer


class FileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.File.objects.all()
    serializer_class = serializers.FileSerializer
