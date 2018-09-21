#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>



struct sensor
{
	struct Accelerometer
	{
		char x[10];
		char y[10];
		char z[10];
	}ACC;
	struct Gyroscope
	{
		char x[10];
		char y[10];
		char z[10];
	}GYR;
	struct Magnetosensor
	{
		char x[10];
		char y[10];
		char z[10];
	}MAG;
	char Proximity[10];
	
};

void print_ACC(struct sensor **SENSOR);
void print_GYR(struct sensor **SENSOR);
void print_MAG(struct sensor **SENSOR);
void print_PROX(struct sensor **SENSOR);
