#include<stdio.h>
#include<conio.h>
#include<stdlib.h>

typedef struct Node
{
    int data;
    struct Node *next;
} Node;

typedef struct 
{
    struct Node*top;
} stack;


void push(stack *s,int data)
{
    Node *newNode = (Node*)malloc(sizeof(Node));
    if(newNode==NULL)
    {
        printf("Empty");
        exit(1);
    }
    newNode -> data=data;
    newNode -> next=s->top;
    s-> top = newNode;
}

int pop(stack*s)
{
    if(s->top==NULL)
    {
        printf("empty");
        exit(1);
    }
    Node *temp=s->top;
    int poppeddata=temp->data;
    s->top=s->top->next;
    free(temp);
    return poppeddata;
}

void dispaly(stack *s)
{
    if(s->top==NULL)
    {
        printf("empty");
        exit(1);
    }
    Node*current=s->top;
    printf("stack elements are:");
    while(current != NULL)
    {
        printf("%d ->",current->data);
        current=current->next;
    }
    printf("\n");
}

stack* createstack()
{
    stack *s=(stack*)malloc(sizeof(stack*));
    if(s==NULL)
        return NULL;
    s->top=NULL;
    return s;
}

int main()
{
    stack *s=createstack();
    push(s,10);
    push(s,20);
    display(&s);
    return 0;
}