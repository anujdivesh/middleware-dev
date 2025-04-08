from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Account
from .serializers import AccountSerializer
from rest_framework.permissions import IsAuthenticated  # Ensure authentication for accessing accounts

class AccountViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]  # Only authenticated users can access account details

    def list(self, request):
        # Retrieve all accounts (for testing purposes)
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        # Get the Account associated with the currently authenticated user
        account = Account.objects.filter(user=request.user).first()
        if not account:
            return Response({"detail": "Account not found."}, status=404)
        
        serializer = AccountSerializer(account)
        return Response(serializer.data)
