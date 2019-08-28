import logging
import rest_framework_datatables

from django.contrib.auth.models import Group

from rest_framework import viewsets, filters
from django_filters import rest_framework as df_filters

from flaim.database import models
from flaim.database import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

logger = logging.getLogger(__name__)


# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all().order_by('-created')
    serializer_class = serializers.ProductSerializer

    # Stacking a lot of df_filters here; this might be an issue but this is purely speculation
    filter_backends = [df_filters.DjangoFilterBackend,
                       rest_framework_datatables.filters.DatatablesFilterBackend,
                       filters.SearchFilter
                       ]
    filterset_fields = ('name', 'store', 'product_code', 'brand',
                        'loblaws_product__section', 'loblaws_product__subcategory')
    search_fields = ['name', 'store', 'brand']


class NutritionFactsViewSet(viewsets.ModelViewSet):
    queryset = models.NutritionFacts.objects.all().order_by('-created')
    serializer_class = serializers.NutritionFactsSerializer


class LoblawsProductViewSet(viewsets.ModelViewSet):
    queryset = models.LoblawsProduct.objects.all().order_by('-created')
    serializer_class = serializers.LoblawsProductSerializer


class WalmartProductViewSet(viewsets.ModelViewSet):
    queryset = models.WalmartProduct.objects.all().order_by('-created')
    serializer_class = serializers.WalmartProductSerializer


class AmazonProductViewSet(viewsets.ModelViewSet):
    queryset = models.AmazonProduct.objects.all().order_by('-created')
    serializer_class = serializers.AmazonProductSerializer


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = models.ProductImage.objects.all().order_by('-created')
    serializer_class = serializers.ProductImageSerializer


class FrontOfPackLabelViewSet(viewsets.ModelViewSet):
    queryset = models.FrontOfPackLabel.objects.all().order_by('-created')
    serializer_class = serializers.FrontOfPackLabelSerializer

    filter_backends = [df_filters.DjangoFilterBackend]
    filterset_fields = ('id', 'product_image', 'label_detected',)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('-name')
    serializer_class = serializers.GroupSerializer
