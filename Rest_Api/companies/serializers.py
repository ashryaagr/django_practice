from rest_framework import serializers
from .models import Stock

class StockSerializer(serializers.ModelSerializer):

    class Meta :
        model = Stock
        # field = ('ticker', 'volume')
        fields = '__all__' # for sending all of the fields