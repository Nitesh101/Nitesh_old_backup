sensor : sensor.o accelerometer_sensor.o gyroscope_sensor.o magnetosensor.o proximity_sensor.o gps_sensor.o
	gcc -o sensor sensor.o accelerometer_sensor.o gyroscope_sensor.o magnetosensor.o proximity_sensor.o gps_sensor.o
	

sensor.o : 
	gcc -c sensor.c
accelerometer_sensor.o : 
	gcc -c accelerometer_sensor.c
gyroscope_sensor.o : 
	gcc -c gyroscope_sensor.c
magnetosensor.o : 
	gcc -c magnetosensor.c
proximity_sensor.o : 
	gcc -c proximity_sensor.c
gps_sensor.o : 
	gcc -c gps_sensor.c
clear: 
	rm *.o
