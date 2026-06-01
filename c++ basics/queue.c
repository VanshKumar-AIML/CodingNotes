#include <stdio.h>
#include <stdlib.h>
#define MAX 5   // Maximum size for array-based queue

// ---------------- QUEUE USING ARRAY ----------------
int queueArr[MAX];
int front = -1, rear = -1;

void enqueueArr(int x) {
    if (rear == MAX - 1) {
        printf("Queue Overflow (Array)\n");
    } else {
        if (front == -1) front = 0; // First element
        queueArr[++rear] = x;
        printf("%d enqueued (Array)\n", x);
    }
}

void dequeueArr() {
    if (front == -1 || front > rear) {
        printf("Queue Underflow (Array)\n");
    } else {
        printf("%d dequeued (Array)\n", queueArr[front++]);
    }
}

void peekArr() {
    if (front == -1 || front > rear) {
        printf("Queue empty (Array)\n");
    } else {
        printf("Front element (Array): %d\n", queueArr[front]);
    }
}

void displayArr() {
    if (front == -1 || front > rear) {
        printf("Queue empty (Array)\n");
    } else {
        printf("Queue elements (Array): ");
        for (int i = front; i <= rear; i++) {
            printf("%d ", queueArr[i]);
        }
        printf("\n");
    }
}

// ---------------- QUEUE USING LINKED LIST ----------------
struct Node {
    int data;
    struct Node* next;
};

struct Node* frontLL = NULL;
struct Node* rearLL = NULL;

void enqueueLL(int x) {
    struct Node* temp = (struct Node*)malloc(sizeof(struct Node));
    temp->data = x;
    temp->next = NULL;

    if (rearLL == NULL) {
        frontLL = rearLL = temp; // First element
    } else {
        rearLL->next = temp;
        rearLL = temp;
    }
    printf("%d enqueued (Linked List)\n", x);
}

void dequeueLL() {
    if (frontLL == NULL) {
        printf("Queue Underflow (Linked List)\n");
    } else {
        printf("%d dequeued (Linked List)\n", frontLL->data);
        struct Node* temp = frontLL;
        frontLL = frontLL->next;
        if (frontLL == NULL) rearLL = NULL; // Queue becomes empty
        free(temp);
    }
}

void peekLL() {
    if (frontLL == NULL) {
        printf("Queue empty (Linked List)\n");
    } else {
        printf("Front element (Linked List): %d\n", frontLL->data);
    }
}

void displayLL() {
    if (frontLL == NULL) {
        printf("Queue empty (Linked List)\n");
    } else {
        printf("Queue elements (Linked List): ");
        struct Node* temp = frontLL;
        while (temp != NULL) {
            printf("%d ", temp->data);
            temp = temp->next;
        }
        printf("\n");
    }
}

// ---------------- MENU DRIVER ----------------
int main() {
    int choice, val;
    while (1) {
        printf("\n=== QUEUE MENU ===\n");
        printf("1. Enqueue (Array)\n");
        printf("2. Dequeue (Array)\n");
        printf("3. Peek (Array)\n");
        printf("4. Display (Array)\n");
        printf("5. Enqueue (Linked List)\n");
        printf("6. Dequeue (Linked List)\n");
        printf("7. Peek (Linked List)\n");
        printf("8. Display (Linked List)\n");
        printf("0. Exit\n");
        printf("Enter choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1: printf("Enter value: "); scanf("%d", &val); enqueueArr(val); break;
            case 2: dequeueArr(); break;
            case 3: peekArr(); break;
            case 4: displayArr(); break;
            case 5: printf("Enter value: "); scanf("%d", &val); enqueueLL(val); break;
            case 6: dequeueLL(); break;
            case 7: peekLL(); break;
            case 8: displayLL(); break;
            case 0: printf("Exiting...\n"); return 0;
            default: printf("Invalid choice\n");
        }
    }
}