from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from account.models.member import Member
from account.util.email_handler import send_register_email
from account.util.redis_connection import connection
from account.serializers.serializer_verify_account import VerifyAccountSerializer


class VerifyView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=VerifyAccountSerializer, responses={200: {}})
    def put(self, request):
        serializer = VerifyAccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['username']
        code = serializer.validated_data['code']
        saved_code = connection.get(email)
        if code == None:
            return Response(status=404, data={"message": "the email was not found"}, exception=True)

        if code != int(saved_code):
            return Response(status=400, data={"message": "the verification code is not correct"})

        try:
            Member.objects.filter(username=email).update(verified=True)
            return Response(status=200, data={"message": "account verified successfuly"})
        except:
            return Response(status=404, data={"message": "user not found"})

    def get(self, request):
        username = request.data.get('username', None)
        if not username or not Member.objects.filter(username=username).exists():
            return Response(status=404, data={"message": "user not found"})
        send_register_email(username)
        return Response({
            "message": "verify code has been sent to your email.",
            "code": "OK"})

