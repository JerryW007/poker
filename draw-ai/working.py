# -*- coding: utf-8 -*-
import pyscreenshot as pys
import time
import subprocess

def screen_shot(name):
    '''截图'''
    screenShot = pys.grab(bbox=(730,430,2749,1633))
    screenShot.save(name + '.png')

def check_gpu():
    simple_nvidia_smi_display = False#@param {type:"boolean"}
    if simple_nvidia_smi_display:
        #!nvidia-smi
        nvidiasmi_output = subprocess.run(['nvidia-smi', '-L'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        print(nvidiasmi_output)
    else:
        #!nvidia-smi -i 0 -e 0
        nvidiasmi_output = subprocess.run(['nvidia-smi'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        print(nvidiasmi_output)
        nvidiasmi_ecc_note = subprocess.run(['nvidia-smi', '-i', '0', '-e', '0'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        print(nvidiasmi_ecc_note)
        
if __name__ == '__main__':
    check_gpu()
    # for i in range(100):
    #     time.sleep(60*2)
    #     screen_shot('cat' + str(i))