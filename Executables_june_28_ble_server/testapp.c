#include <stdio.h>
#include<json/json.h>
#include<string.h>
#include"VITA_DM.h"

typedef struct node {
    Resource_info *res;
    struct node *next;
}listNode;

listNode *header = NULL;

void user_discover_callback(Resource_info* res_info)    //                        Discover
{
    //printf("\t\t\tin Discover:\n");
    if(strcmp(res_info->name,"/oic/p")==0
            || strcmp(res_info->name,"/oic/d")==0
            ||strcmp(res_info->name,"/oic/sec/doxm")==0
            ||strcmp(res_info->name,"/oic/sec/acl2")==0
            ||strcmp(res_info->name,"/oic/sec/cred")==0
            ||strcmp(res_info->name,"/oic/sec/crl")==0
            ||strcmp(res_info->name,"/oic/sec/csr")==0
            ||strcmp(res_info->name,"/oic/sec/roles")==0
            ||strcmp(res_info->name,"/introspection")==0
            ||strcmp(res_info->name,"/oic/sec/pstat")==0 )
    { 
            return;
    }
    else
    {   
    	printf("****************************************************\n");
     	printf("Resource name: %s\n",res_info->name);
     	printf("Resource handle: %p \n",res_info->handle);
     	printf("****************************************************\n\n");

	mysql_Insert_Discover(res_info->name, res_info->handle);          
	return;
    }
}

void user_get_callback(handle_t handle, json_object* jsonObj)         //                   Get
{
     char buff[1200],*ptr;
    json_object_object_foreach(jsonObj, key, val)
    {
        switch(json_object_get_type(val))
        {
        case json_type_boolean: sprintf(buff,"%s", json_object_get_boolean(val)? "true":"false");
            break;
        case json_type_int:sprintf(buff,"%d", json_object_get_int(val));
            break;
        case json_type_string:strcpy(buff,json_object_get_string(val));
			ptr=strchr(buff,39);
			if(ptr!=NULL)
				*(buff+(ptr-buff))='-';
			else
				strcpy(buff,json_object_get_string(val));
            break;
       } 
	mysql_Insert_Get(handle,key,buff);
    }
}

void put_data(void * inputHandle, char newstr[], char ch[], int i, char s[])   //               Put
{
	json_object* put_local;
	put_local = json_object_new_object();
	//printf(" hanle : %s key : %s valuetype : %s int %d string %s\n",inputHandle,newstr,ch, i,s);
	switch(ch[0])
	{
		case 'i': 
			json_object_object_add(put_local, newstr, json_object_new_int(i));
			break;
		case 's':
			json_object_object_add(put_local, newstr, json_object_new_string(s));
			break;
		case 'b':
			json_object_object_add(put_local, newstr, json_object_new_boolean(i));
			break;
	}	
	VITA_DM_Put(inputHandle, put_local);
	
}

void user_observe_callback(handle_t handle, json_object* jsonObj)    //             Observe
{
	char buff[1200],*ptr;
    //printf("handle in app:%p\n",handle);
    json_object_object_foreach(jsonObj, key, val)
    {
       // printf("Key :%s\t\t",key);
        switch(json_object_get_type(val))
        {
        case json_type_boolean:	sprintf(buff,"%s", json_object_get_boolean(val)? "true":"false");
                break;
        case json_type_int:sprintf(buff,"%d", json_object_get_int(val));
                break;
        case json_type_string: strcpy(buff,json_object_get_string(val));
			ptr=strchr(buff,39);
			if(ptr!=NULL)
				*(buff+(ptr-buff))='-';
			else
				strcpy(buff,json_object_get_string(val));
            break;
        }
	mysql_Insert_Observe(handle,key,buff);
    }
}

void user_delete_callback(handle_t h)  //                                          Delete
{
     if(h)
	{
	      	mysql_Delete_Resource(h);
	}   
       return;
}

int main(void)
{
   return 0;
}
