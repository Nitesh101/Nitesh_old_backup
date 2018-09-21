#include <stdio.h>
#include<json/json.h>
#include<string.h>
//#include"header_app.h"
#include"../Headers/VITA_DM.h"

uint32_t VITA_DM_Init(void);
uint32_t VITA_DM_Discover(disc_ptr callback);
void VITA_DM_Get(const char *handle, onGet_ptr callback);
void VITA_DM_Put(const char *handle, json_object *obj);
void VITA_DM_Observe(const char *handle, onobserve_ptr callback, int32_t start_stop);

void user_discover_callback(Resource_info*);
void user_get_callback(handle_t, json_object*);
//void user_put_callback(handle_t, json_object*);
void user_observe_callback(handle_t, json_object*);

typedef struct node {
    Resource_info *res;
    struct node *next;
}listNode;

listNode *header = NULL;
//json_object* get_local;// = json_object_new_object();

void user_discover_callback(Resource_info* res_info) {
    listNode *local_node= header;

    listNode *travel_list;
    listNode *new_node;
    travel_list = header;
    while(travel_list != NULL) {
        if(strcmp(travel_list->res->name, res_info->name)==0) {
            printf("****************************************************\n");
            printf("Resource name: %s\n",travel_list->res->name);
            printf("Resource handle: %p \n",travel_list->res->handle);
            printf("****************************************************\n\n");
            return;
        }
        else {
            // printf("comparision else in app level %s,%s========>AAAAAAAAAAAAAAAA\n",res_info->name,travel_list->res->name);
            travel_list = travel_list->next;
        }
    }
    if(strcmp(res_info->name,"/oic/p")==0
            || strcmp(res_info->name,"/oic/d")==0
            ||strcmp(res_info->name,"/oic/sec/doxm")==0
            ||strcmp(res_info->name,"/oic/sec/pstat")==0 ) {
        return;
    }
    new_node = (listNode *)malloc(sizeof(listNode));
    new_node->res = res_info;
    new_node->next = NULL;

    printf("****************************************************\n");
    printf("Resource name: %s\n",new_node->res->name);
    printf("Resource handle: %p \n",new_node->res->handle);
    printf("****************************************************\n\n");

    if(local_node == NULL) {
        header = new_node;
    }
    else {
        while(local_node->next != NULL) {
            local_node = local_node->next;
        }
        local_node->next = new_node;
    }
    return ;
}

void user_get_callback(handle_t handle, json_object* jsonObj)
{
    json_object_object_foreach(jsonObj, key, val)
    {
        printf("Key :%s\t",key);
        switch(json_object_get_type(val))
        {
        case json_type_boolean:  printf("value type: boolean value: %s\n", json_object_get_boolean(val)? "true": "false");
            break;
        case json_type_int: printf("value type: integer value:%d\n",json_object_get_int(val));
            break;
        case json_type_string: printf("value type: string value:%s\n",json_object_get_string(val));
            break;
        case json_type_double: printf("value type: double value: %lf\n", json_object_get_double(val));
            break;
        case json_type_object: printf("value type: json_type_object value\n");
            break;
        case json_type_array: printf("value type: json_type_array value\n ");
            break;
        case json_type_null: printf("value type: Null value\n ");
            break;
        }
    }
}

void user_observe_callback(handle_t handle, json_object* jsonObj)
{
    printf("handle in app:%p\n",handle);
    json_object_object_foreach(jsonObj, key, val)
    {
        printf("Key :%s\t\t",key);
        switch(json_object_get_type(val))
        {
        case json_type_boolean:  printf("boolean value: %s\n", json_object_get_boolean(val)? "true": "false");
            break;
        case json_type_int: printf("integer value:%d\n",json_object_get_int(val));
            break;
        case json_type_string: printf("string value:%s\n",json_object_get_string(val));
            break;
        case json_type_double: printf("double value: %lf\n", json_object_get_double(val));
            break;
        case json_type_object: printf("json_type_object value\n");
            break;
        case json_type_array: printf("json_type_array value\n ");
            break;
        case json_type_null: printf("Null value\n ");
            break;
        }
    }
}



int main()
{
    return 0;
}
