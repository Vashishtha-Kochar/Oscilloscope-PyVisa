import visa
import sys
import argparse
import numpy as np
from struct import unpack
import pylab
import threading
import matplotlib.animation as animation

def getReading():
    

def animate(i, times, Volts):

    # Create figure for plotting
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    


if __name__ == '__main__':
    
    # Parse command line arguements
    parser = argparse.ArgumentParser(description='Connect to oscilloscope')
    parser.add_argument('-a', '--address', type=str, required=True, help='Address of instrument')
    parser.add_argument('-i', '--interval', type=str, required=True, help='Intervals of time for every plot')
    args = parser.parse_args()
    instAddress = args.address
    timeInterval = args.interval

    try:
        rm = visa.ResourceManager()
        scope = rm.get_instrument(instAddress)
        # example instAddress ='GPIB0::12::INSTR'
        # you can find out the address using findAddress.py
        print(scope.ask("*IDN?"))
    except Exception as e:
        print("Error creating instance: {0}".format(e))
        sys.exit()

    scope.write('DATA:SOU CH1')
    scope.write('DATA:WIDTH 1')
    scope.write('DATA:ENC RPB')


    ymult = float(scope.ask('WFMPRE:YMULT?'))
    yzero = float(scope.ask('WFMPRE:YZERO?'))
    yoff = float(scope.ask('WFMPRE:YOFF?'))
    xincr = float(scope.ask('WFMPRE:XINCR?'))

    scope.write('CURVE?')
    data = scope.read_raw()
    # data is a block of the form #<x><yyy><data><newline>
    # <x> is the number of y bytes
    # <yyy> is the number of bytes to transfer
    # <data> is the curve data
    # <newline> is single byte newline character at the end of data
    headerlen = 2 + int(data[1])
    # header = data[:headerlen]
    ADC_wave = data[headerlen:-1]

    ADC_wave = np.array(unpack('%sB' % len(ADC_wave),ADC_wave))

    Volts = (ADC_wave - yoff) * ymult  + yzero

    Time = np.arange(0, xincr * len(Volts), xincr)