#include<stdio.h>
#include<wiringPi.h>

#define Output_Pin 0
#define Input_Pin 1
int main()
{
	printf("This is an example of a raspberry PI pin reading\n");
	wiringPiSetup();
	pinMode(Output_Pin,OUTPUT);
	pinMode(Input_Pin,INPUT);
	
	printf("Set Output_Pin : H\n");
    digitalWrite(Output_Pin,HIGH);
    delay(200);
	printf("Input_Pin : %d\n",digitalRead(Input_Pin));
    delay(2000);
    
	printf("Set Output_Pin: L\n");
	digitalWrite(Output_Pin,LOW);
	delay(200);
	printf("Input_Pin : %d\n",digitalRead(Input_Pin));
	while(1)
	{

	}
	return 0;
}

