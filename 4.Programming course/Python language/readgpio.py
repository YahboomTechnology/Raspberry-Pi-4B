import wiringpi

GPIO_Output_Pin = 0
GPIO_Intput_Pin = 1
OUTPUT = 1
INPUT = 0
HIGH = 1
LOW = 0

wiringpi.wiringPiSetup()
wiringpi.pinMode(GPIO_Output_Pin,OUTPUT)
wiringpi.pinMode(GPIO_Intput_Pin,INPUT)

while 1:
    wiringpi.digitalWrite(GPIO_Output_Pin,HIGH)
    print('GPIO_Output_Pin OUTPUT =>HIGH')
    print('GPIO_Intput_Pin INPUT <=',wiringpi.digitalRead(GPIO_Intput_Pin))
    wiringpi.delay(1000)
    print()

    wiringpi.digitalWrite(GPIO_Output_Pin,LOW)
    print('GPIO_Output_Pin OUTPUT =>LOW')
    print('GPIO_Intput_Pin INPUT <=',wiringpi.digitalRead(GPIO_Intput_Pin))
    wiringpi.delay(1000)
    print()