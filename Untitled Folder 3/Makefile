app:test.o fact.o fib.o prime.o
	gcc test.o fact.o fib.o prime.o -o app
test.o:test.c ffp.h
	gcc -c test.c
fact.o:fact.c ffp.h
	gcc -c fact.c
fib.o:fib.c ffp.h
	gcc -c fib.c
prime.o:prime.c ffp.h
	gcc -c prime.c
clean:
	rm -rf *.o

