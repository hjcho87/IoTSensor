import os
from ota_updater import OTAUpdater

wifi_ssid = "<SSID>"
wifi_password = "<PASSWORD>"

def download_and_install_update_if_available():
  o = OTAUpdater('https://github.com/hjcho87/IoTSensor')
  o.autoUpdate(wifi_ssid, wifi_password)

def start():
  download_and_install_update_if_available()

if __name__ == '__main__':
  start()
