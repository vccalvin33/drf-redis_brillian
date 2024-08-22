from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.cache import cache
from .models import *
from .serializers import *


# TODO: FIX THE PLACEMENT OF CACHE
class InstitutionsView(ListAPIView):
    queryset = Institutions.objects.all()
    serializer_class = InstituionsSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        queryset = super().get_queryset()
        institution_name = self.request.query_params.get('name', None)
        if institution_name:
            queryset = queryset.filter(top_sellers__contains=[{'name': institution_name}])
        return queryset
    
    def list(self, request):
        cache_key = 'institution-sell'
        result = cache.get(cache_key)
        if not result:
            print('Hitting DB')
            result = self.get_queryset()
            result = result.values_list('symbol')
            cache.set(cache_key, list(result), 60)
        else:
            print('Cache retrieved!')

        return Response([r[0] for r in result])


#TODO: Create Institution Top Buy

#TODO: Create Get All Sub Sector slugs