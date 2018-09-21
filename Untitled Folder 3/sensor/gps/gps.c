#include"sensor.h"
void time_date_formate(char *time);
void gps(char *str)
{
	GPS *phone_gps;
	phone_gps = (GPS*)malloc(sizeof(GPS));
	FILE *fp;
	fp=fopen("file.txt","r");
	char temp[10];
	char buff[100],str1[100],status[10],time[20],latitude[10],longitude[10];
	char direction[2][4],speed[10],date[10];
	int choice;
	while(fgets(buff,100,fp))
	{
		sscanf(buff,"%s",str1);
		if(strcmp(str1,str)==0)
		{
			printf("%s",str);
			sscanf(buff,"%s%s%s",temp,phone_gps->time,status);
			printf("%s %s %s",temp,phone_gps->time,status);
			if(status[0]=='A')
			{
				
				
//				sscanf(buff,"%s%s",temp,phone_gps->time,status,phone_gps->latitude,phone_gps->longitude);
				sscanf(buff,"%s%s%s%s%s%s%s%s%s%s",temp,time,status,latitude,direction[0],longitude,direction[1],speed,temp,date);
				puts(latitude);
				puts(longitude);
				puts(speed);
				int i;
				i=strlen(speed);
				printf("%d\n",i);

				strncpy(phone_gps->time,time,strlen(time)-1);
				strncpy(phone_gps->latitude,latitude,strlen(latitude)-1);
				phone_gps->latitude[strlen(latitude)]='\0';
				strncpy(phone_gps->longitude,longitude,strlen(longitude)-1);
				phone_gps->longitude[strlen(longitude)]='\0';
				strncpy(phone_gps->speed,speed,strlen(speed)-1);
				i=strlen(speed);
				printf("%d\n",i);
				phone_gps->speed[strlen(speed)]='\0';
				strncpy(phone_gps->date,date,strlen(date)-1);
				while(1)
				{
				printf("1.time\n2.lattitude\n3.longitude\n4.speed\n5.date\n6.main menu\n");
				printf("enter your choice:");
				scanf("%d",&choice);
				switch(choice)
				{
					case 1:
						time_date_formate(phone_gps->time);
						puts(phone_gps->time);break;
					case 2:
						if((strncmp(direction[0],"N",1)==0)||(strncmp(direction[0],"E",1)==0))
							printf("lat:%s\n",phone_gps->latitude);
						else
							printf("lat:-%s\n",phone_gps->latitude);
							
						break;
					case 3:
						if((strncmp(direction[1],"N",1)==0)||(strncmp(direction[1],"E",1)==0))
							printf("long:%s\n",phone_gps->longitude);
						else
							printf("long:-%s\n",phone_gps->longitude);
						break;
					case 4:puts(phone_gps->speed);break;
					case 5:
						time_date_formate(phone_gps->date);
						puts(phone_gps->date);break;
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
	fclose(fp);
}}

void time_date_formate(char *time)
{
	char *buff;
	buff=calloc(1,10);
	strncpy(buff,time,2);
	strcat(buff,":");
	strncpy(buff+3,time+2,2);
	strcat(buff,":");
	strncpy(buff+6,time+4,2);
	strcpy(time,buff);
}
