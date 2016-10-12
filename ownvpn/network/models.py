from django.db import models


class Interface(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    dev_name = models.CharField(max_length=10, unique=True)
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



