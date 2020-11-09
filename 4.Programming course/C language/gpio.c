#include<stdio.h>
#include<wiringPi.h>

#define GPIO0 0 
int main()
{
	printf("This is an example of controlling the high and low levels of GPIO pin output\n");
	wiringPiSetup();
	pinMode(GPIO0,OUTPUT);
	//printf("Set GPIO0 : H\n");
    //digitalWrite(GPIO0,HIGH); 
	printf("Set GPIO0 : L\n");
	digitalWrite(GPIO0,LOW);
	while(1)
	{

	}
	return 0;
}
