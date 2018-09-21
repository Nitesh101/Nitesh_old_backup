#include"sensor.h"

int main(void)
{
	int choice;
	do
	{
		printf("1. Accelerometer \n2. Gyroscope \n3. Magnetosensor\n4. Proximity\n5. $GPRMC\n6. EXIT\n");
		printf("Please enter your choice: ");
		scanf("%d",&choice);
		switch(choice)
		{
			case 1:
				execl("./accelerometer_sensor","accelerometer_sensor.c",(char *)0);
				break;
			case 2:
				execl("./gyroscope_sensor","gyroscope_sensor.c",(char *)0);
				break;
			case 3:
				execl("./magnetosensor","magnetosensor.c",(char *)0);
				break;
			case 4:
				execl("./proximity_sensor","proximity_sensor.c",(char *)0);
				break;
			/*case 5:
				strcpy(str,"$GPRMC,");
				print_str(str);
				break;*/
			default:
				printf("Please enter proper choice: ");
				break;
			case 6:
				printf("Exiting");
				return 0;
		}
		
	}while(choice <= 5);

}







