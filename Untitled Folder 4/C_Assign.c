
/*
//1.Dec to bin
#include<stdio.h>
int main()
{
	int num,arr[16],i,j;
	printf("enter a decimal value: ");
	scanf("%d",&num);
	i=0;
	while(num>0)
	{
		arr[i]=num%2;
		num/=2;
		i++;
	}
	printf("Binary number: ");
	for(j=i-1;j>=0;j--)
		printf("%d",arr[j]);
	printf("\n");
	return 0;
}

//2.string length
#include<string.h>
int main()
{
	char str[20];
	printf("enter a string: ");
	fgets(str);
	printf("length od str: %u\n",strlen(str));
	return 0;
}

// 3. string cmp and copy

int main()
{
	char str1[20],str2[20];
        printf("enter two strings: ");
        fgets(str1);
        fgets(str2);
	if((strcmp(str1,str2))==0)
		printf("strings are same");
	else
        	printf("strings are not same");
	strcpy(str2,"Hyderabad");
		printf("str1:%s\t\tstr2:%s\n",str1,str2);
        return 0;
}

//4.strin cancatinate
int main()
{
	
	char str1[20],str2[20];
        printf("enter two strings: ");
        fgets(str1);
        fgets(str2);
	strcat(str1,str2);
	printf("str1:%s\t\tstr2:%s\n",str1,str2);
	return 0;
}
//5. Auto
int main()
{
	auto int num = 10;
	printf("%d\n",num*10);
	return 0;
}

//6.static
void fun();
static int a=3,b=4;
int main()
{
	fun();
	fun();
	fun();
	return 0;
}
void fun()
{

	printf("%d\t%d\n",a,b);
	a++;
	b++;
}

//7.Array of pointers
int main()
{
	int i,j,arr[3][4]={{10,11,12,13},{20,21,22,23},{30,31,32,33}};
	int *ptr[3];
	for(i=0;i<3;i++)
		ptr[i]=arr[i];
	for(i=0;i<3;i++)
	{
		for(j=0;j<4;j++)
			printf("%d  ",ptr[i][j]);
		printf("\n");
	}
	return 0;
}

//8.DMA
#include<stdio.h>
#include<stdlib.h>
int main()
{
	int *p,n,i;
	printf("enter number of ele : ");
	scanf("%d",&n);
	p=(int *)malloc(n*sizeof(int));
	for(i=0;i<n;i++)
	{
		printf("enter a integer: ");
		scanf("%d",p+i);
	}
	for(i=0;i<n;i++)
	{
		printf("%d\t",*(p+i));
	}
	
	p=(int *)realloc(p,9*sizeof(int));
	for(i=n;i<9;i++)
	{
		*(p+i)=i*10;
	}
	
	for(i=0;i<9;i++)
	{
		printf("%d\t",*(p+i));
	}
	printf("\n");
	free(p);
	return 0;
}*/

