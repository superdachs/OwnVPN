from django.contrib import admin
from openvpn.models import OpenvpnClient
from openvpn.models import OpenvpnServer

admin.site.register(OpenvpnClient)
admin.site.register(OpenvpnServer)

