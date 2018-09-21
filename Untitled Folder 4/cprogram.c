#include<stdio.h>
int my_sum(int a,int b);
int main()
{
 int a=7,b=8,sum;
  sum = my_sum(a,b);
   printf("%d",sum);
} 
int my_sum(int a, int b)
{
	return a+b;

}

