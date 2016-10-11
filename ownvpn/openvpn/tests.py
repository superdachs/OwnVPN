from django.test import TestCase
from openvpn.models import OpenvpnServer
from openvpn.models import Tools
import subprocess

class OpenvpnServerTestCase(TestCase):
    def setUp(self):
        OpenvpnServer.objects.create(name='testserver', description='Keine Beschreibung', port=1194, tun_ip='10.0.0.1', config='server-testserver-on', start_on_boot=False, client_ip='10.0.0.2')

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

