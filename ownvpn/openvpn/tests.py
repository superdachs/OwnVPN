from django.test import TestCase
from openvpn.models import OpenvpnServer
import subprocess

class OpenvpnServerTestCase(TestCase):
    def setUp(self):
        OpenvpnServer.objects.create(name='testserver', description='Keine Beschreibung', port=1194, tun_ip='10.0.0.1', config='server-testserver-on', start_on_boot=False, client_ip='10.0.0.2')

    def test_start_on_boot(self):

        server = OpenvpnServer.objects.get(name="testserver")

        server.start_on_boot = True
        server.save()
        cmd = "systemctl status openvpn@server-testserver"
        p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        out_en, err_en = p.communicate()
        ret = p.wait()
        server.start_on_boot = False
        server.save()
        cmd = "systemctl status openvpn@server-testserver"
        p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        out_dis, err_dis = p.communicate()
        ret = p.wait()

        server = OpenvpnServer.objects.get(name='testserver')
        server.delete()
 
        self.assertTrue(b'enabled' in out_en)
        self.assertFalse(b'enabled' in out_dis)


