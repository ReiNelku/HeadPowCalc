import math

class Headphone:
    def __init__(self, impedance, sensitivity, v):
        self.imp = impedance
        self.sens = sensitivity
        # Variable is true if the sensitivity is given in dB/V and false if it is in dB/mW
        self.is_v = v

    def __str__(self):
        # Return a string of the headphone impedance and sensitivity
        if self.is_v:
            return f"This headphone impedance is {self.imp} ohms and sensitivity is {self.sens} dB/V."
        else:
            return f"This headphone impedance is {self.imp} ohms and sensitivity is {self.sens} dB/mW."

    def sens_conv(self):
        # Convert sensitivity from dB/V to dB/mW and vice-versa
        if self.is_v:
            return round(self.sens + 10 * math.log(self.imp * 0.001, 10), 2)
        else:
            return round(self.sens + 10 * math.log(1000 / self.imp, 10), 2)


class Amplifier:
    def __init__(self, headphone, spl):
        self.imp = headphone.imp
        self.sens = headphone.sens
        self.is_v = headphone.is_v
        self.sens_conv = headphone.sens_conv()
        self.spl = spl

    # Return a string with the power, voltage and current needed to drive the headphone
    def __str__(self):
        return f"Power = {self.power()} mW \nVoltage = {self.voltage()} VRMS \nCurrent = {self.current()} mA"

    def voltage(self):
        # Calculate the voltage needed for the required loudness
        if self.is_v:
            return round(10 ** ((self.spl - self.sens) / 20), 2)
        else:
            return round(10 ** ((self.spl - self.sens_conv) / 20), 2)

    def power(self):
        # Calculate the power needed from the amp to drive the given headphones
        return round(1000 * self.voltage() ** 2 / self.imp, 2)

    def current(self):
        # Calculate the current needed from the amp to drive the given headphones
        return round(1000 * self.voltage() / self.imp, 2)
