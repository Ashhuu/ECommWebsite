from rest_framework.response import Response
from rest_framework.views import APIView

from web.models import ProductDetails
from .serializers import ProductSerializer


class ProductView(APIView):
    def get(self, request):
        product = ProductDetails.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response({"product": serializer.data})