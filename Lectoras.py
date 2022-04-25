#!/usr/bin/python
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
            self.convertData(self.dataList)

    def convertData(self, arraydata):
        self.NUMMAP = {30: '1',
                       31: '2',
                       32: '3',
                       33: '4',
                       34: '5',
                       35: '6',
                       36: '7',
                       37: '8',
                       38: '9',
                       39: '0',
                       40: ' '}
        i = 0
        val = ''
        while i < len(arraydata):
            index = arraydata[i][2]
            val += self.NUMMAP[index]
            i += 2
        print val
