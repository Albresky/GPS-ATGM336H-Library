import smbus
import time
import math

# 第一阶段电压-PPM转换
# volat = [1.54, 3.482]
def gas_1(volat):
    return -111.080423+72.01658*volat

# 第二阶段电压-PPM转换
# volat = (3.482, 3.975]
def gas_2(volat):
    return 7868.159413-4363.868362*volat+617.37*(volat**2)
# 指数拟合
# return 0.99689*math.exp(1.40569*volat)

# 第三阶段电压-PPM转换
# volat = [3.975, 4.2]
def gas_3(volat):
    return -3387.56585+922.075319*volat

def getGas():
    address = 0x48
    A0 = 0x40
    A1 = 0x41
    A2 = 0x42
    A3 = 0x43

    bus = smbus.SMBus(1)

    while True:
        bus.write_byte(address,A0)
        value=bus.read_byte(address)
        volat= (value)/105*4.216
        gas=0.0
        if volat>=0 and volat<=1.54:
            gas = 0.0
        elif volat<=3.482:
            gas = gas_1(volat)
        elif volat<3.975:
                gas = gas_2(volat)
        elif volat<=4.215:
            gas = gas_3(volat)             
        print("{:.1f}".format(gas))
        time.sleep(0.31)
        
if __name__=='__main__':
    getGas()

    