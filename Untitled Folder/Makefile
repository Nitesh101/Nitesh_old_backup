fact_fibo_prime:fact.o fibo.o prime.o main.o
	gcc -o fact_fibo_prime fact.o fibo.o prime.o main.o
fact.o:fact.c
	gcc -c fact.c
fibo.o:fibo.c
	gcc -c fibo.c
prime.o:prime.c
	gcc -c prime.c
main.o:main.c
	gcc -c main.c
clean:
	rm  *.o
	rm fact_fibo_prime
