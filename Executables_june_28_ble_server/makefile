# the compiler: gcc for C program
CC = gcc

# compiler flags:
#  -g    adds debugging information to the executable file
#  -Wall turns on most, but not all, compiler warnings
CFLAGS  = -g

curr_dir = $(shell pwd)

all : main

main :
	
#	gcc -g testapp_dev.c  -o testapp_dev -ljson -L./Executables/lib/ -lDM -lDeM -lCM -lDSM -L./ -lDM_iotivity -L./release -lconnectivity_abstraction -loc_logger -loctbstack -loc 


	gcc -shared -o libmysql_c.so -fPIC mysql_c.c `mysql_config --cflags --libs`
	gcc -shared -o testapp.so testapp.c -ljson -I/usr/include/mysql libmysql_c.so -L./Executables/lib/ -lDM -lDeM -lCM -lDSM -L./ -lDM_iotivity -L./release -lcoap -lconnectivity_abstraction -loc_logger -loctbstack -loc -fPIC 

	#export LD_LIBRARY_PATH=./:./release:./Executables/lib



clean :
	rm *.exe
