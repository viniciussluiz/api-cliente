from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome': "Esse campo não deve conter números"})
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': "O CPF não é válido"})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg': "Esse campo deve conter 9 digitos"})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular': "O número de celular deve seguir esse modelo: 31 97856-6785 (respeitando espaços e traço)"})
        return data