from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import get_object_or_404

from .models import origin, nodeList, linkList
from .serializers import OriginSerializer, NodeListSerializer, LinkListSerializer

class NodeView(APIView):

    def get(self, request):     # Метод обработки GET-запроса
        origins = origin.objects.all()
        nodeLists = nodeList.objects.all()
        linkLists = linkList.objects.all()

        # Параметр many указывает на то, что будет сериализовываться более одного сценария
        origin_serializer = OriginSerializer(origins, many=True)
        nodeList_serializer = NodeListSerializer(nodeLists, many=True)
        linkList_serializer = LinkListSerializer(linkLists, many=True)
        return Response([
            {'origins': origin_serializer.data},
            {'nodeList': nodeList_serializer.data},
            {'linkList': linkList_serializer.data}
        ])
    @csrf_exempt
    def post(self, request):    # Метод обработки POST-запроса
        origins = request.data.get('origin')
        nodeLists = request.data.get('nodeList')
        linkLists = request.data.get('linkList')

        # Создаем сценарий из введенных пользователем данных
        origin_serializer = OriginSerializer(data=origins)
        nodeList_serializer = NodeListSerializer(data=nodeLists)
        linkList_serializer = LinkListSerializer(data=linkLists)

        if ((origin_serializer.is_valid(raise_exception=True)) or (nodeList_serializer.is_valid(raise_exception=True)) or
                (linkList_serializer.is_valid(raise_exception=True))):
            origin_serializer.save()
            nodeList_serializer.save()
            linkList_serializer.save()
        return Response({
            "success": "Data was created successfully"
        })
    #
    # def put(self, request, pk):     # Метод обработки PUT-запроса
    #     saved_script = get_object_or_404(Script.objects.all(), pk=pk)
    #     data = request.data.get('script')
    #     serializer = ScriptSerializer(instance=saved_script, data=data, partial=True)
    #     if serializer.is_valid(raise_exception=True):
    #         script_saved = serializer.save()
    #
    #     return Response({
    #         "success": "Script step №'{}' in '{}' film updated successfully".format(script_saved.scriptstep, script_saved.filmname)
    #     })
    #
    # def delete(self, request, pk):      # Метод обработки запроса удаления
    #     script = get_object_or_404(Script.objects.all(), pk=pk)
    #     script.delete()
    #     return Response({
    #         "success": "Script step №'{}' in '{}' film was deleted  successfully".format(script.scriptstep, script.filmname)
    #     }, status=204)
