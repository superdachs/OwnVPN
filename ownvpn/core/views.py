from django.shortcuts import render, render_to_response
from openvpn.models import OpenvpnServer

def start(request):
    context = {}
    return render(request, 'core/start.html', context)

def list_vpns(request):
    vpn_servers = OpenvpnServer.objects.all()
    context = {
            'vpn_servers': vpn_servers,
            }
    return render_to_response('core/list_vpns.html', context)

def edit_vpn(request, vpn_pk):

    vpn = OpenvpnServer.objects.get(pk=vpn_pk)



    return None
