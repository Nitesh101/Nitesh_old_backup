#include<stdio.h>
#include<stdlib.h>
void prime(int n)
{
	int i,count=0;
	for(i=2;i<n;i++)
	{
		if(n%i==0)
			count++;
	}
	if(count==2)
	{
		printf("%d is Not prime Number\n",n);
			//exit(1);
	}
	else
	{
		printf("%d is Prime Number\n",n);
			//exit(1);
	}
	exit(1);
}
	

