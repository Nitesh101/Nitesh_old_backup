#include"sensor.h"

void print_ACC(struct sensor **SENSOR)
{
	FILE* fp;
	int choice,index = 0,index1;
	fp = fopen("file.txt","r");
	char str2[20],buff[200],x[10],buff1[30],s1;
	while(fgets(buff,100,fp))
	{
		sscanf(buff,"%s",str2);
		if(strcmp("Accelerometer",str2)==0)
		{
			sscanf(buff,"%s%s%s%s",x,(*SENSOR)->ACC.x,(*SENSOR)->ACC.y,(*SENSOR)->ACC.z);
		}
	}
	scanf("%c",&s1);
	printf("Enter either x or y or z you want: ");
	scanf("%30[0-9a-zA-Z ]",buff1);
	while(1)
	{
		index1 = index - 1;
		if(buff1[index] == ' ' || buff1[index] == '\0' )
		{
			printf("%c : ",buff1[index1]);
			if(buff1[index-1] == 'x')
			{
				puts((*SENSOR)->ACC.x);
			}			
			else if(buff1[index-1] == 'y')
			{			
				puts((*SENSOR)->ACC.y);
			}			
			else if(buff1[index-1] == 'z')
			{			
				puts((*SENSOR)->ACC.z);
			}			
			else
				printf("Wrong input\n");
		}
		if(buff1[index] == '\0')
			break;
		index++;
	}
	fclose(fp);	
}
