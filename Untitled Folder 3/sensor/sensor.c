#include"sensor.h"

int main(void)
{
	struct sensor *SENSOR;
	SENSOR = (struct sensor*)malloc(sizeof(struct sensor));
	int choice;
	do
	{
		printf("1. Accelerometer \n2. Gyroscope \n3. Magnetosensor\n4. Proximity\n5. $GPRMC\n6. EXIT\n");
		printf("Please enter your choice: ");
		scanf("%d",&choice);
		switch(choice)
		{
			case 1:
				print_ACC(&SENSOR);
				break;
			case 2:
				print_GYR(&SENSOR);
				break;
			case 3:
				print_MAG(&SENSOR);
				break;
			case 4:
				print_PROX(&SENSOR);
				break;
			case 5:
				print_GPS(&SENSOR);
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







