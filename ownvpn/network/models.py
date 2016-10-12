from django.db import models
import netifaces
import subprocess

class Tools:
    
    def list_physical_nics():
        all_nics = netifaces.interfaces()
        physical_nics = []
        for nic in all_nics:
            cmd = "ethtool -i %s | grep bus-info" % nic
            p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
            out, err = p.communicate()
            p.wait()
            print("out: %s" % out)
            if b"N/A" not in out and out != b'':
                physical_nics.append(nic)

        return physical_nics

    def nic_choices():
        nics = Tools.list_physical_nics()
        choices = []
        for nic in nics:
            choices.append((nic, nic))
        return choices

       
class Interface(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    dev_name = models.CharField(max_length=10, unique=True, choices=Tools.nic_choices())
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    netmask = models.GenericIPAddressField(null=True, blank=True)
    dhcp = models.BooleanField(default=True)
    is_wlan_nic = models.BooleanField(default=False)

    def __str__(self):
        return "%s (%s)" % (self.name, self.dev_name)

class Wlan(models.Model):
    name = models.CharField(max_length=255)
    ssid = models.CharField(max_length=255)
    wpa_key = models.CharField(max_length=255)

    class Meta:
        unique_together = ('ssid', 'wpa_key')

    def __str__(self):
        return "%s (%s)" % (self.name, self.ssid)



