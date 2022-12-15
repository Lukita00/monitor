import psutil

class Monitor:

    def __init__(self) -> None:
        pass

    def getCpu(self):

        self.cpuCount   = psutil.cpu_count()
        self.cpuPercent = psutil.cpu_percent(interval=1)
        return {
            "cpu_Counter":self.cpuCount, 
            "cpu_percent":self.cpuPercent
        }

    def getMem(self):
        
        self.totalMem       = psutil.virtual_memory().total 
        self.usedMem        = psutil.virtual_memory().used
        self.percentMem     = psutil.virtual_memory().percent
        self.freeMem        = psutil.virtual_memory().free

        self.totalMemSwap   = psutil.swap_memory().total
        self.usedMemSwap    = psutil.swap_memory().used
        self.percentMemSwap = psutil.swap_memory().percent

        return {
            'total_Mem'        : self.totalMem,
            'used_Mem'         : self.usedMem,
            'percent_Mem'      : self.percentMem,
            'free_Mem'         : self.freeMem,
            'total_Mem_Swap'   : self.totalMemSwap,
            'used_Mem_Swap'    : self.usedMemSwap,
            'percent_Mem_Swap' : self.percentMemSwap
        }

    def getTemp(self):
        try:
            self.cpuTemp = psutil.sensors_temperatures()

            return {
                'cpu_Temp' : self.cpuTemp
            }
        except AttributeError as error:

            print(error)
            return {
                'cpu_Temp' : ''
            }

    def getBattery(self):
        try:
            self.battery = psutil.sensors_battery().percent

            return {
                'battery_Percent' : self.battery
            }
        except AttributeError as error:

            print(error)
            return {
                 'battery_Percent' : ''
            }


if __name__ == '__main__':
    monitor = Monitor()

    print(monitor.getCpu())
    print(monitor.getMem())
    print(monitor.getTemp())
    print(monitor.getBattery())