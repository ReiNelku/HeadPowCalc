# HeadPowCalc
#### Video Demo: https://youtu.be/8Vo6wPyFi10
#### Description:
##### What is the purpose of this program?
For sound to play off your headphones, you need to have another 3 devices in your audio chain. Starting with the source, which could be your phone playing Spotify, your PC playing Youtube
etc. Your digital source outputs 1's and 0's, which are converted to analog signal by a device called Digital to Analog Converter(DAC). Then, this analog signal is passed on to an Amplifier(Amp), gets amplified and powers your headphones to play your favourite music.

Each headphone has it's own sensitivity and impedance, which determine how much power is needed from an Amp to reach a desired loudness(SPL).
High Sensitivity -> Low power needed
Low Sensitivity -> High power needed

High Impedance -> High power needed
Low Impedance -> Low power needed

HeadPowCalc purpose is just that, to calculate the power which the Amp should provide to power your headphone.
##### HeadPowCalc Features
This program offers these features:
1) Given the headphone sensitivity(in decibels per volt or decibels per miliwatt) and impedance (in ohms), HeadPowCalc will display your headphone specifications.
2) If you have given the sensitivity in dB/V you can convert it to dB/mW and vice-versa.
3) HeadPowCalc gives the user the option to calculate the exact power, voltage and current needed from an Amp to drive your headphones.
##### Project Files
1) project.py -> main project
2) test_project.py -> test file using pytest of project.py
3) classes.py -> a file of classes used in the main project
4) exceptions.py -> a file of exceptions used in the main project
5) requirements.txt -> a list of pip-installable libraries used in the main project
##### Project Code Description
The project started with the creation of the classes **Headphone** and **Amplifier**. Headphone class accepts these parameters: impedance(as an int or a float), sensitivity(as an non-negative int or float) and v(True or False value which signifies the unit of sensitivity, True for dB/V and False for dB/mW). Amplifier class accepts two parameters: headphone(an object instantiated by the Headphone class) and loudness(as an non-negative int or float). __init__ constructor of each class initializes their respective instance variables(Amplifier constructor borrows impedance, sensitivity and unit value from the headphone object). Headphone uses the __str__ method to return the specifications of the headphone object and sens_conv() method to convert the sensitivity from dB/V to dB/mW and vice-versa. Amplifier uses the __str__ method to return the power, voltage and current needed to drive the headphone object, which are calculated by the power(), voltage() and current() methods.
Then comes the main function, which houses the menu used in the program, starting with the name of the program. A headphone object is instatiated using  get_headphone() function, which asks the user for a correct impedance and sensitivity(also asking them for the unit), prompting them again if they are incorrect. After, the user are offered 3 options: to display the headphone specifications, convert the unit of sensitivity and calculating the power needed from the Amplifier.
Chosing the third option, the program will instatiate an amplifier object using get_amp() function, then the user has to provide the loudness in SPL(Sound Pressure Level measured in dB), prompting them again if it is incorrect. Finally, the program will print the required power(mW), voltage(VRMS) and current(mA) to drive the headphones to the specified SPL.