#include"sensor.h"


void print_PROX(struct sensor **SENSOR)
{
	FILE* fp;
	fp = fopen("file.txt","r");
	char str2[20],buff[200],x[10];
	while(fgets(buff,100,fp))
	{
		sscanf(buff,"%s",str2);
		if(strcmp("Proximity",str2)==0)
		{
			sscanf(buff,"%s%s",x,(*SENSOR)->Proximity);
			puts((*SENSOR)->Proximity);
		}
	}
	fclose(fp);
}
