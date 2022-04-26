##  # !/usr/bin/python
# -*- coding: utf-8 -*-
import threading
import usb.core
import usb.util
from time import sleep


class Lectora(threading.Thread):

    def __init__(self, device):
        threading.Thread.__init__(self)
        self.device = device

    def run(self):
        self.endpoint = self.device[0][(0, 0)][0]
        while True:
            self.data = []
            self.dataList = []
            for i in range(22):
                self.data = self.device.read(
                    self.endpoint.bEndpointAddress, self.endpoint.wMaxPacketSize, timeout=99999999999999999)
                self.dataList.append(self.data)
            self.convertData(self.dataList)  # TODO

    ##### Desconectar dispositivo del driver para poder hacer operaciones de E/S
    @staticmethod
    def desconectarDriver(self):
        if self.device.is_kernel_driver_active(0):
            try:
                self.device.detach_kernel_driver(0)
            except:
                print("error dev.detach_kernel_driver(0)")
                pass
        #print (usb.util.get_string(dev, dev.idProduct))

    def convertData(self, arraydata):
        self.CHARMAP0 = {30: '1', 31: '2', 32: '3', 33: '4', 34: '5', 35: '6',
                         36: '7', 37: '8', 38: '9', 39: '0', 40: ' ', 45: '-', 55: '.', 56: '/'}
        self.CHARMAP2 = {4: 'A', 5: 'B', 6: 'C', 7: 'D', 8: 'E', 9: 'F', 10: 'G', 11: 'H', 12: 'I', 13: 'J', 14: 'K', 15: 'L', 16: 'M',
                         17: 'N', 18: 'O', 19: 'P', 20: 'Q', 21: 'R', 22: 'S', 23: 'T', 24: 'U', 25: 'V', 26: 'W', 27: 'X', 28: 'Y', 29: 'Z',
                         33: '$', 34: '%', 46: '+'}
        i = 0
        val = ''
        while i < len(arraydata):
            index = arraydata[i][2]
            val += self.CHARMAP0[index]
            i += 2
        print val


def main():

    return 0
