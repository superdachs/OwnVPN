from django.forms import ModelForm
from openvpn.models import OpenvpnServer, OpenvpnClient

class OpenvpnServerForm(ModelForm):
    class Meta:
        model = OpenvpnServer
        fields = '__all__'

class OpenvpnClientForm(ModelForm):
    class Meta:
        model = OpenvpnClient
        fields = '__all__'

