#include <stdio.h>
#include <conio.h>
#include <stdlib.h>

typedef struct Node  //node structure
{
    int data;
    struct Node*next;
} Node;

Node *createNode(int data)   //creating newnode
{
    Node*newNode = (Node *)malloc(sizeof(Node));
    if(!newNode)
    {
        printf("Memory error");
        exit(1);
    }
    newNode ->data = data;
    newNode->next=NULL;
    return newNode;
}

void traverseList(Node *head)  //list traversal
{
    Node *current = head;
    while(current != NULL)
    {
        printf("%d ->",current->data);
        current =current-> next;
    }
    printf("NULL\n");
}

void traverseListrecursive(Node *current)  //by recursion
{
    if(current==NULL)
    {
        printf("NULL\n");
        return ;
    }
    printf("%d -> ",current->data);
    return traverseListrecursive(current ->next);
}

Node *search(Node*head,int key)  //finding key pointer
{
    Node *current=head;
    while(current != NULL)
    {
        if(current->data==key)
            return current;
        current=current->next;
    }
    return NULL;
}

//insert at beginning
void insertatbeg(Node **head,int key,int data)
{
    Node *newNode=createNode(key);
    newNode ->data = data;
    newNode ->next=*head;
    *head=newNode;
}

//inserting after a specific location
void insertafter(Node *prevNode,int key,int data)
{
    if(prevNode==NULL)
    {
        printf("the given node cannot be null");
        return ;
    }
    Node *newNode=createNode(key);
    newNode->data=data;
    newNode->next=prevNode->next;
    prevNode->next=newNode;
}

//deleting from beginning
void deletefrombeg(Node **head)
{
    if( *head==NULL)
    {
        printf("Empty list");
        return ;
    }
    Node *temp=*head;
    *head=(*head)->next;
    free(temp);
}

//deletion from end
void deleteafter(Node *prevNode)
{
    if(prevNode==NULL || (prevNode)->next ==NULL)
    {
        printf("NULL node");
        return;
    }
    Node *temp= prevNode->next;
    prevNode->next=temp->next;
    free(temp);
}

//reverse of the link list
void reverse(Node **head)
{
    Node *prev=NULL;
    Node *current=*head;
    Node *next=NULL;
    while(current!=NULL)
    {
        next=current->next;
        current->next=prev;
        prev=current;
        current=next;
    }
    *head=prev;
}

//reverse by recursion
Node *reverser (Node *h1)
{
    if(h1->next=NULL)
    {
        return h1;
    }
    Node *rest=reverser(h1->next);
    h1->next->next=h1;
    h1->next=NULL;
    return rest;
}

int main()
{
    Node *head=createNode(1);   //giving head data
    head ->next=createNode(2);  //data for next node
    head ->next ->next=createNode(3);
    printf("linked list:\n");
    traverseList(head);
    return 0;
}