from rest_framework.authtoken.models import Token

def generate_tokens(request):
    token = Token.objects.create(user=request.user)
    print(token.key)