#include <my_global.h>
#include <mysql.h>
MYSQL *con;
void finish_with_error(MYSQL *con)
{
  fprintf(stderr, "%s\n", mysql_error(con));
  mysql_close(con);
  exit(1);        
}

void mysql_Connect()
{
   MYSQL *con = mysql_init(NULL);

  
 if (con == NULL)
  {
      fprintf(stderr, "%s\n", mysql_error(con));
      exit(1);
  }

  if (mysql_real_connect(con, "localhost", "Test_Team", "votary",
          "DM_Testing", 0, NULL, 0) == NULL)
  {
      finish_with_error(con);
  }
return;
}

void mysql_Disconnect()
{
	
	mysql_close(con);

}

void mysql_Insert_Discover(const char *name, char *handle)
{
     char consulta[1002];
     MYSQL *con = mysql_init(NULL);

   if (con == NULL)
  {
      fprintf(stderr, "%s\n", mysql_error(con));
      exit(1);
  }

  if (mysql_real_connect(con, "localhost", "Test_Team", "votary",
          "DM_Testing", 0, NULL, 0) == NULL)
  {
      finish_with_error(con);
  }

   sprintf(consulta,"insert into DM_Discover values('%d','%s','%p')",NULL,name,handle);
   if(mysql_query(con,consulta))
  {
      finish_with_error(con);
  }
  
return ;
}


void mysql_Insert_Get(char *handle,char *key , char *value)
{
    
     char consulta[1002];
     MYSQL *con = mysql_init(NULL);

   if (con == NULL)
  {
      fprintf(stderr, "%s\n", mysql_error(con));
      exit(1);
  }

  if (mysql_real_connect(con, "localhost", "Test_Team", "votary",
          "DM_Testing", 0, NULL, 0) == NULL)
  {
      finish_with_error(con);
  }
   sprintf(consulta,"insert into DM_GET values('%d','%s','%p','%s','%s')",NULL,handle,handle,key,value);
   if(mysql_query(con,consulta))
  {
      finish_with_error(con);
  }
  
 
return ;
}


void mysql_Insert_Observe(char *handle,char *key , char *value)
{
     char consulta[1002];
     MYSQL *con = mysql_init(NULL);

   if (con == NULL)
  {
      fprintf(stderr, "%s", mysql_error(con));
      exit(1);
  }

  if (mysql_real_connect(con, "localhost", "Test_Team", "votary",
          "DM_Testing", 0, NULL, 0) == NULL)
  {
      finish_with_error(con);
  }
  // printf("\n\t\t\t\t******* Insert Observe\n");
   sprintf(consulta,"insert into DM_Observe values('%d','%s','%p','%s','%s')",NULL,handle,handle,key,value);
   if(mysql_query(con,consulta))
  {
      finish_with_error(con);
  }
  
 
return ;
}


void mysql_Delete_Resource(char *handle)
{
    
     char consulta[1002];
     printf("handle_Delete : %p\n",handle);

     MYSQL *con = mysql_init(NULL);

   if (con == NULL)
  {
      fprintf(stderr, "%s\n", mysql_error(con));
      exit(1);
  }

  if (mysql_real_connect(con, "localhost", "Test_Team", "votary",
          "DM_Testing", 0, NULL, 0) == NULL)
  {
      finish_with_error(con);
  }
   
   printf("deleting from discover \n");
   sprintf(consulta,"DELETE FROM DM_Discover WHERE Handle = '%p'" ,handle);

   if(mysql_query(con,consulta))
  {
      finish_with_error(con);
  }
  sleep(2);
  sprintf(consulta,"DELETE FROM DM_GET WHERE Handle = '%p'" ,handle);

   if(mysql_query(con,consulta))
  {
      finish_with_error(con);
  }

  sleep(2);
 
return ;
}

