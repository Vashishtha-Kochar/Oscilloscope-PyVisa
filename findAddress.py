import pyvisa

def getAddress():
    rm = pyvisa.ResourceManager()
    resourceList = rm.list_resources()

    usbAddress = [str(resource) for resource in resourceList if "USB" in resource][0]

    return usbAddress

if __name__ == "__main__":
    print(getAddress())
