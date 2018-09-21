#include<stdio.h>
#include<stdlib.h>
long int fact(int n)
{
	long fact=1;
	if(n<0)
	{
		printf("No fatorial for ngative\n");
		exit(1);
	}
	else if(n==0)
		return 1;
	else
	{
		while(n>0)
		{
			fact=fact*n;
			n--;
		}
		return fact;
	}
}
