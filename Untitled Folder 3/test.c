#include<stdio.h>
#include"ffp.h"
#include<stdlib.h>

int main()
{
	int data,n;
	printf("The app gives you fact/fib/prime output\n");
	printf("Enter 1 for fact , 2 for fib and 3 for prime: \n");
	scanf("%d",&data);
	if(data==1)
	{
		printf("Enter a fact number:\n");
		scanf("%d",&n);	
		fact(n);
	}
	else if(data==2)
	{
		printf("Enter number of terms: \n");
		scanf("%d",&n);
		fib(n);
	}
	
	else if(data==3)
	{
		printf("Enter a range number: \n");
		scanf("%d",&n);
		prime(n);
	}
	else
	{
		printf("wrong option\n");
		exit(1);
	}

	return 0;
}
