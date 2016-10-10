from django.forms import ModelForm
from openvpn.models import OpenvpnServer

class OpenvpnServerForm(ModelForm):
    class Meta:
        model = OpenvpnServer
        fields = '__all__'

