#include"sensor.h"
//void print_str(SENSOR *,char *);
int main(void)
{
	//struct sensor *SENSOR;
	//SENSOR=(struct sensor *)malloc(sizeof(struct sensor));
	SENSOR *sensor;
	char str[20];
	int choice;
	do
	{
		printf("1. Accelerometer \n2. Gyroscope \n3. Magnetosensor\n4. Proximity\n5. $GPRMC\n6.EXIT\n");
		printf("Please enter your choice: ");
		scanf("%d",&choice);
		switch(choice)
		{
/*			case 1:
				strcpy(str,"Accelerometer");
				print_str(sensor,str);
				accel(sensor,str);
				break;
			case 2:
				strcpy(str,"Gyroscope");
				print_str(str);
				break;
			case 3:
				strcpy(str,"Magnetosensor");
				print_str(str);
				break;
			case 4:
				strcpy(str,"Proximity");
				print_str(str);
				break;
	*/
			case 5:
				strcpy(str,"$GPRMC,");
				gps(str);
				break;
			default:
				printf("Please enter proper choice: ");
				break;
			case 6:
				printf("Exiting");
				return 0;
		}
		
	}while(choice <= 5);

}
/*void print_str(SENSOR *SENS,char *str)
{
	FILE* fp;
	fp = fopen("file.txt","r");
	char str2[20],buff[200],x[10];
	SENS=calloc(1,sizeof(SENS));
	while(fgets(buff,100,fp))
	{
		sscanf(buff,"%s",str2);
		if(strcmp(str,str2)==0)
		{
			puts(buff);
			sscanf(buff,"%s%s%s%s",x,SENS->x,SENS->y,SENS->z);
			puts(SENS->x);
			puts(SENS->y);
			puts(SENS->z);
		}
	}
	fclose(fp);
}*/
