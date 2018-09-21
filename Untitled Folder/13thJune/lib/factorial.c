#include<stdio.h>

int facto(int num)
{
	int result = 1, temp;
	while(num != 0)
	{
		//temp = num%10;
		result = result * num;
		num = num-1;
	}
	return result;
}
