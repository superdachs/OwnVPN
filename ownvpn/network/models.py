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

    def get_conf_dhcp(ifname):
        addresses = netifaces.ifaddresses(ifname)
        if len(addresses[netifaces.AF_INET]) == 0:
            raise Exception("Not configured")
        address = addresses[netifaces.AF_INET][0]
        return address['addr'], address['netmask']


       
class Interface(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    dev_name = models.CharField(max_length=10, unique=True, choices=Tools.nic_choices())
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    netmask = models.GenericIPAddressField(null=True, blank=True)
    gateway = models.GenericIPAddressField(null=True, blank=True)
    dhcp = models.BooleanField(default=True)
    is_wlan_nic = models.BooleanField(default=False)


    @classmethod
    def from_db(cls, *args, **kwargs):
        instance = super(Interface, cls).from_db(*args, **kwargs)
        if instance.dhcp:
            instance.ip_address, instance.netmask = Tools.get_conf_dhcp(instance.dev_name)


        return instance



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



