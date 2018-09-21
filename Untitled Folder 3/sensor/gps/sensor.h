#include<stdio.h>
#include<stdlib.h>
#include<string.h>

typedef struct sensor
{
		char x[10];
		char y[10];
		char z[10];
	
}SENSOR;
typedef struct gps
{
	char time[10];
	char longitude[20],latitude[20],speed[20];
	char date[10];
}GPS;
void accel(SENSOR *,char *);
void gps(char *);
