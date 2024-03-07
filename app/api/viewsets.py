from rest_framework.viewsets import ModelViewSet
from ..models import ViaCep
from .serializers import ViaCepSerializer


class ViaCepViewset(ModelViewSet):
    serializer_class = ViaCepSerializer
    queryset = ViaCep.objects.all()


    def create(self, request):
        cep = request.data.get('cep','00000000')

        site = f'https://viacep.com.br/ws/{cep}/json/'

        requisicao = requests.get(site)

        json = requisicao.json()

        cep = json.get('cep','')
        logradouro = json.get('logradouro','')
        complemento = json.get('complemento','')
        bairro = json.get('bairro','')
        localidade = json.get('localidade','')
        uf = json.get('uf','')

        dados_recebidos = {
            "cep": f'{cep}',
            "logradouro": f'{logradouro}',
            "complemento": f'{complemento}',
        }


