from django.contrib import admin
from openvpn.models import OpenvpnClient
from openvpn.models import OpenvpnServer
from openvpn.models import AddressPort

admin.site.register(AddressPort)
admin.site.register(OpenvpnClient)
admin.site.register(OpenvpnServer)

