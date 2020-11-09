#include<stdio.h>
#include<wiringPi.h>
#include<softPwm.h>
#define PWM_Pin 1

int main()
{
	printf("This is an experiment of output PWM\n");
	wiringPiSetup();
	softPwmCreate(PWM_Pin,0,100);
	softPwmWrite(PWM_Pin,50);
	while(1)
	{

	}
	return 0;
}

