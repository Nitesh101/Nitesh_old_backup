#include"sensor.h"

/*int main(void)
{
	struct sensor *SENSOR;
	SENSOR=(struct sensor *)malloc(sizeof(struct sensor));
	print_MAG(&SENSOR);
}*/


void print_MAG(struct sensor **SENSOR)
{
	FILE* fp;
	int choice,index = 0,index1 = 0;
	fp = fopen("file.txt","r");
	char str2[20],buff[200],x[10],s1,buff1[30];
	while(fgets(buff,100,fp))
	{
		sscanf(buff,"%s",str2);
		if(strcmp("Magnetosensor",str2)==0)
		{
			sscanf(buff,"%s%s%s%s",x,(*SENSOR)->MAG.x,(*SENSOR)->MAG.y,(*SENSOR)->MAG.z);
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
				puts((*SENSOR)->MAG.x);
			}			
			else if(buff1[index-1] == 'y')
			{			
				puts((*SENSOR)->MAG.y);
			}			
			else if(buff1[index-1] == 'z')
			{			
				puts((*SENSOR)->MAG.z);
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
