#include"sensor.h"
void time_date_formate(char *time);
void print_GPS(struct sensor **SENSOR)
{
	FILE *fp;
	fp=fopen("file.txt","r");
	char temp[10];
	char buff[100],str1[100],status[10];
	char direction[2][4];
	int choice;
	while(fgets(buff,100,fp))
	{
		sscanf(buff,"%s",str1);
		if(strcmp(str1,"$GPRMC,")==0)
		{
			sscanf(buff,"%s%s%s",temp,time,status);
			if(status[0]=='A')
			{
				sscanf(buff,"%s%s%s%s%s%s%s%s%s%s",temp,(*SENSOR)->GPS.time,
								   status,(*SENSOR)->GPS.latitude,
								   direction[0],(*SENSOR)->GPS.longitude,
								   direction[1],(*SENSOR)->GPS.speed,
								   temp,(*SENSOR)->GPS.date);
				while(1)
				{
				printf("1.time\n2.lattitude\n3.longitude\n4.speed\n5.date\n6.main menu\n");
				printf("enter your choice:");
				scanf("%d",&choice);
				switch(choice)
				{
					case 1:
						time_date_formate((*SENSOR)->GPS.time);
						puts((*SENSOR)->GPS.time);break;
					case 2:
						if((strncmp(direction[0],"N",1)==0)||(strncmp(direction[0],"E",1)==0))
							printf("lat:%s\n",(*SENSOR)->GPS.latitude);
						else
							printf("lat:-%s\n",(*SENSOR)->GPS.latitude);
							
						break;
					case 3:
						if((strncmp(direction[1],"N",1)==0)||(strncmp(direction[1],"E",1)==0))
							printf("long:%s\n",(*SENSOR)->GPS.longitude);
						else
							printf("long:-%s\n",(*SENSOR)->GPS.longitude);
						break;
					case 4:puts((*SENSOR)->GPS.speed);break;
					case 5:
						time_date_formate((*SENSOR)->GPS.date);
						puts((*SENSOR)->GPS.date);break;
					case 6:puts("Exiting from gps");return;
				}
				}

			}
			else
			{
				puts("gps is INACTIVE");
				break;
			}
		
	
	}
}
}
void time_date_formate(char *time)
{
	char *buff;
	buff=calloc(1,20);
	strncpy(buff,time,2);
	strcat(buff,":");
	strncpy(buff+3,time+2,2);
	strcat(buff,":");
	strncpy(buff+6,time+4,2);
	strcpy(time,buff);
}
