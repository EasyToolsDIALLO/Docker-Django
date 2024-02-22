from ocr_api.serializers import *
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from ..models import *
# clients


class FactureAPIView(generics.CreateAPIView):
    """
    POST api/v1/factures/
    """
    queryset = factures.objects.all()
    serializer_class = FactureSerializer

    def post(self, request, format=None):
        serializer = FactureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
        # return Response( status=400)

    def get(self, request, format=None):
        items = factures.objects.all().order_by('pk')
        serializer = FactureSerializer(items, many=True)
        return Response({"count": items.count(), "data": serializer.data})


class FactureByIdAPIView(generics.CreateAPIView):
    # permission_classes = (
    #     permissions.IsAuthenticated,
    # )
    queryset = factures.objects.all()
    serializer_class = FactureSerializer

    def get(self, request, id, format=None):
        try:
            item = factures.objects.get(pk=id)
            serializer = FactureSerializer(item)
            return Response(serializer.data)
        except factures.DoesNotExist:
            return Response({
                "status": 404,
                "message": "no such item with this id",
            }, status=404)

    def put(self, request, id, format=None):
        try:
            item = factures.objects.all().get(pk=id)
        except factures.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
            }, status=404)
        self.data = request.data.copy()
        serializer = FactureSerializer(item, data=self.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, *args, **kwargs):
        try:
            item = factures.objects.all().get(id=kwargs["id"])
        except factures.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
            }, status=404)
        item.delete()
        return Response({"message": "deleted"}, status=204)
