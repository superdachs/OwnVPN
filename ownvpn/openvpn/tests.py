from django.test import TestCase
from openvpn.models import OpenvpnServer, OpenvpnClient, AddressPort
from openvpn.models import Tools
from network.models import Interface
import subprocess

class OpenvpnServerTestCase(TestCase):
    def setUp(self):
        interface = Interface.objects.create()
        addressport = AddressPort.objects.create(port=1194)
        OpenvpnServer.objects.create(name='testserver', description='Keine Beschreibung', bind_to=addressport, tun_ip='10.0.0.1', start_on_boot=False, client_ip='10.0.0.2')

    def test_key_creation(self):
        key = Tools.create_key()

        self.assertTrue(key)

    def systemdstatus(self):
        cmd = "systemctl status openvpn@server-testserver"
        p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        out, err_en = p.communicate()
        ret = p.wait()
        return out

    def test_systemd(self):
        server = OpenvpnServer.objects.get(name="testserver")

        server.start_on_boot = True
        server.save()
        out_en = self.systemdstatus()
        server.start_on_boot = False
        server.save()
        out_dis = self.systemdstatus()

        server.control('start')
        out_start = self.systemdstatus()

        server.control('restart')
        out_restart = self.systemdstatus()

        server.control('stop')
        out_stop = self.systemdstatus()

        server.delete()

        self.assertTrue(b'enabled' in out_en)
        self.assertFalse(b'enabled' in out_dis)
        self.assertTrue(b'active (running)' in out_start)
        self.assertTrue(b'active (running)' in out_restart)
        self.assertFalse(b'active (running)' in out_stop)

class OpenvpnClientTestCase(TestCase):
    def setUp(self):
        server_address_port = AddressPort.objects.create(port=1195)
        client_address_port = AddressPort.objects.create(port=1196)
        OpenvpnServer.objects.create(name='testserver_client', description='Keine Beschreibung', bind_to=server_address_port, tun_ip='10.0.0.1', start_on_boot=False, client_ip='10.0.0.2')
        self.server = OpenvpnServer.objects.get(name='testserver_client')
        self.server.control('start')
        OpenvpnClient.objects.create(name='testclient', description='Keine Beschreibung', bind_to=client_address_port, server_port=1199, tun_ip='10.0.0.2', start_on_boot=False, gateway='localhost', server_ip='10.0.0.1', static_key=self.server.static_key)

    def systemdstatus(self):
        cmd = "systemctl status openvpn@client-testclient"
        p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        out, err_en = p.communicate()
        ret = p.wait()
        return out

    def test_systemd(self):
        client = OpenvpnClient.objects.get(name="testclient")

        client.start_on_boot = True
        client.save()
        out_en = self.systemdstatus()
        client.start_on_boot = False
        client.save()
        out_dis = self.systemdstatus()

        client.control('start')
        out_start = self.systemdstatus()

        client.control('restart')
        out_restart = self.systemdstatus()

        client.control('stop')
        out_stop = self.systemdstatus()

        self.server.control('stop')

        
        client.delete()
        self.server.delete()

        self.assertTrue(b'enabled' in out_en)
        self.assertFalse(b'enabled' in out_dis)
        self.assertTrue(b'active (running)' in out_start)
        self.assertTrue(b'active (running)' in out_restart)
        self.assertFalse(b'active (running)' in out_stop)

