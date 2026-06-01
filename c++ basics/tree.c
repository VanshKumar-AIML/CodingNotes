#include <stdio.h>
#include <conio.h>
#include <stdlib.h>

typedef struct Node{                 //structure of the node
    int data;
    struct Node* left;
    struct Node* right;
} Node;

Node *createNode(int data)          //new node function
{
    Node*newNode= (Node *)malloc(sizeof(struct Node));
    if(!newNode)
    {
        printf("Memory full");
        exit(1);
    }
    newNode->data=data;
    newNode->left=NULL;
    newNode->right=NULL;
}

void insert(Node **root,int data)           //recursive insertion
{
    if(*root==NULL)
    {
        *root=createNode(data);
        return;
    }

    if(*root > NULL)
        insert(&((*root)->right),data);

    else
        insert(&((*root)->left),data);
}



