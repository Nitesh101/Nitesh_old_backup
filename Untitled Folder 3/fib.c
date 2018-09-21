#include<stdio.h>
void fib(int n)
{
	long x,y,z;
	int i;
	x=0;
	y=1;
	printf("%ld",y);
	for(i=1;i<n;i++)
	{
		z=x+y;
		printf("%ld",z);
		x=y;
		y=z;
	}
	printf("\n");
}


