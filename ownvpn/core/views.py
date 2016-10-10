from django.shortcuts import render, render_to_response, get_object_or_404
from openvpn.models import OpenvpnServer
from openvpn.forms import OpenvpnServerForm

def start(request):
    context = {}
    return render(request, 'core/start.html', context)

def list_vpns(request):
    vpn_servers = OpenvpnServer.objects.all()
    context = {
            'vpn_servers': vpn_servers,
            }
    return render_to_response('core/list_vpns.html', context)

def edit_vpn(request, vpn_type, vpn_pk):

    if vpn_type == "openvpn_server":
        vpn = get_object_or_404(OpenvpnServer, pk=vpn_pk)
        form = OpenvpnServerForm(instance=vpn)

    context = {
            'form': form,
            }
    return render_to_response('core/edit_vpn.html', context)

