import wiringpi

OUTPUT = 1
PIN_TO_PWM = 1

wiringpi.wiringPiSetup()
wiringpi.pinMode(PIN_TO_PWM,OUTPUT)
wiringpi.softPwmCreate(PIN_TO_PWM,0,100
wiringpi.softPwmWrite(PIN_TO_PWM,50)