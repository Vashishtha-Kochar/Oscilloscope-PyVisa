import visa
import argparse
import sys
import matplotlib.pyplot as plt
import findAddress

if __name__ == '__main__':
    
    # Parse command line arguements
    parser = argparse.ArgumentParser(description='Connect to oscilloscope')
    parser.add_argument('-a', '--address', default = findAddress.getAddress(), type=str, help='Address of instrument')
    parser.add_argument('-c','--channel',help='scope channel to use',action='store', default='1', type=int, choices=range(1, 2))
    parser.add_argument('-p','--plot',help='plot captured waveform',action='store_true')
    parser.add_argument('-s','--sampling',help='sampling frequency, default is 1 M', action='store', default='1000000')
    args = parser.parse_args()
    instAddress = args.address
    ch = 'channel'+str(args.channel)
    #try:
    rm = visa.ResourceManager()
    myScope = rm.get_instrument(instAddress)
    # example instAddress ='GPIB0::12::INSTR'
    # you can find out the address using findAddress.py
    print("reached " + instAddress)
    print(myScope.ask("*IDN?"))
    #print(myScope.query('*IDN?'))    #except Exception as e:
    # #print("Error creating instance: {0}".format(e))
    # #sys.exit()

    # myScope.write("WGEN:FREQ 50000") #connect the wavegen to channel 1
    # myScope.write("WGEN:FUNC SIN")
    # myScope.write("WGEN:OUTP ON")
    # myScope.write("WGEN:VOLT 2")

    # myScope.write(":TIMebase:SCALe 3.0E-5")
    # myScope.write(":WAVeform:SOURce CHANnel1")
    # myScope.write(":WAVeform:FORMat ASCII")
    # myScope.write(":WAVeform:POINts 1000")

    # data = myScope.query("WAV:DATA?")

    # print(data)