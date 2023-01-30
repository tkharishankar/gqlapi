from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializers import ProjectSerializer
from projects.models import Project


@api_view(['GET'])
def getRoutes(req):
    routes = [
        {'GET': 'api/projects'},
        {'POST': 'api/users/token'}
    ]
    return Response(routes)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProjects(req):
    projects = Project.objects.all()
    serialize = ProjectSerializer(projects, many=True)
    return Response(serialize.data)
