from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def getRoutes(req):
    routes = [
        {'POST': 'api/users/token'}
    ]
    return Response(routes)


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def getProjects(req):
#     projects = Project.objects.all()
#     serialize = ProjectSerializer(projects, many=True)
#     return Response(serialize.data)
