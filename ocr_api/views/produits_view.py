from ocr_api.serializers import *
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from ..models import *
# clients


class ProduitAPIView(generics.CreateAPIView):
    """
    POST api/v1/produits/
    """
    queryset = produit.objects.all()
    serializer_class = ProduitSerializer

    def post(self, request, format=None):
        serializer = ProduitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
        # return Response( status=400)

    def get(self, request, format=None):
        items = produit.objects.all().order_by('pk')
        serializer = ProduitSerializer(items, many=True)
        return Response({"count": items.count(), "data": serializer.data})


class ProduitByIdAPIView(generics.CreateAPIView):
    # permission_classes = (
    #     permissions.IsAuthenticated,
    # )
    queryset = produit.objects.all()
    serializer_class = ProduitSerializer

    def get(self, request, id, format=None):
        try:
            item = produit.objects.get(pk=id)
            serializer = ProduitSerializer(item)
            return Response(serializer.data)
        except produit.DoesNotExist:
            return Response({
                "status": 404,
                "message": "no such item with this id",
            }, status=404)

    def put(self, request, id, format=None):
        try:
            item = produit.objects.all().get(pk=id)
        except produit.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
            }, status=404)
        self.data = request.data.copy()
        serializer = ProduitSerializer(item, data=self.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, *args, **kwargs):
        try:
            item = produit.objects.all().get(id=kwargs["id"])
        except produit.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
            }, status=404)
        item.delete()
        return Response({"message": "deleted"}, status=204)
