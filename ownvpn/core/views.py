from django.shortcuts import render, render_to_response, get_object_or_404
from openvpn.models import OpenvpnServer, OpenvpnClient
from openvpn.forms import OpenvpnServerForm, OpenvpnClientForm

def start(request):
    context = {}
    return render(request, 'core/start.html', context)

def list_vpns(request):
    vpn_servers = OpenvpnServer.objects.all()
    vpn_clients = OpenvpnClient.objects.all()
    context = {
            'vpn_servers': vpn_servers,
            'vpn_clients': vpn_clients,
            }
    return render_to_response('core/list_vpns.html', context)

def create_vpn(request, vpn_type):
    return edit_vpn(request, vpn_type, None)

def edit_vpn(request, vpn_type, vpn_pk):
    if vpn_type == "openvpn_server":
        if not vpn_pk:
            vpn = OpenvpnServer()
        else:
            vpn = get_object_or_404(OpenvpnServer, pk=vpn_pk)
        form = OpenvpnServerForm(instance=vpn)
    elif vpn_type == "openvpn_client":
        if not vpn_pk:
            vpn = OpenvpnClient()
        else:
            vpn = get_object_or_404(OpenvpnClient, pk=vpn_pk)
        form = OpenvpnClientForm(instance=vpn)

    context = {
            'form': form,
            }
    return render_to_response('core/edit_vpn.html', context)

