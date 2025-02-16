from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import TextEntry
from .serializers import TextEntrySerializer

@api_view(['POST'])
def save_text(request):
    serializer = TextEntrySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_texts(request):
    texts = TextEntry.objects.all()
    serializer = TextEntrySerializer(texts, many=True)
    return Response(serializer.data)
