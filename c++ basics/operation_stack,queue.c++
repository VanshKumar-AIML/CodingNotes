#include <iostream>
using namespace std;

#define MAX 5   // Maximum size for array-based stack/queue

// ---------------- STACK USING ARRAY ----------------
int stackArr[MAX];
int top = -1;

void pushArr(int x) {
    if (top == MAX - 1) cout << "Stack Overflow\n";
    else {
        stackArr[++top] = x;
        cout << x << " pushed into stack\n";
    }
}

void popArr() {
    if (top == -1) cout << "Stack Underflow\n";
    else cout << stackArr[top--] << " popped from stack\n";
}

void peekArr() {
    if (top == -1) cout << "Stack empty\n";
    else cout << "Top element: " << stackArr[top] << "\n";
}

void displayArrStack() {
    if (top == -1) cout << "Stack empty\n";
    else {
        cout << "Stack elements: ";
        for (int i = top; i >= 0; i--) cout << stackArr[i] << " ";
        cout << "\n";
    }
}

// ---------------- QUEUE USING ARRAY ----------------
int queueArr[MAX];
int front = -1, rear = -1;

void enqueueArr(int x) {
    if (rear == MAX - 1) cout << "Queue Overflow\n";
    else {
        if (front == -1) front = 0;
        queueArr[++rear] = x;
        cout << x << " enqueued into queue\n";
    }
}

void dequeueArr() {
    if (front == -1 || front > rear) cout << "Queue Underflow\n";
    else cout << queueArr[front++] << " dequeued from queue\n";
}

void peekArrQ() {
    if (front == -1 || front > rear) cout << "Queue empty\n";
    else cout << "Front element: " << queueArr[front] << "\n";
}

void displayArrQueue() {
    if (front == -1 || front > rear) cout << "Queue empty\n";
    else {
        cout << "Queue elements: ";
        for (int i = front; i <= rear; i++) cout << queueArr[i] << " ";
        cout << "\n";
    }
}

// ---------------- STACK USING LINKED LIST ----------------
struct Node {
    int data;
    Node* next;
};

Node* topLL = NULL;

void pushLL(int x) {
    Node* temp = new Node();
    temp->data = x;
    temp->next = topLL;
    topLL = temp;
    cout << x << " pushed into stack (LL)\n";
}

void popLL() {
    if (topLL == NULL) cout << "Stack Underflow\n";
    else {
        cout << topLL->data << " popped from stack (LL)\n";
        Node* temp = topLL;
        topLL = topLL->next;
        delete temp;
    }
}

void peekLL() {
    if (topLL == NULL) cout << "Stack empty\n";
    else cout << "Top element: " << topLL->data << "\n";
}

void displayLLStack() {
    if (topLL == NULL) cout << "Stack empty\n";
    else {
        cout << "Stack elements: ";
        Node* temp = topLL;
        while (temp != NULL) {
            cout << temp->data << " ";
            temp = temp->next;
        }
        cout << "\n";
    }
}

// ---------------- QUEUE USING LINKED LIST ----------------
Node* frontLL = NULL;
Node* rearLL = NULL;

void enqueueLL(int x) {
    Node* temp = new Node();
    temp->data = x;
    temp->next = NULL;
    if (rearLL == NULL) {
        frontLL = rearLL = temp;
    } else {
        rearLL->next = temp;
        rearLL = temp;
    }
    cout << x << " enqueued into queue (LL)\n";
}

void dequeueLL() {
    if (frontLL == NULL) cout << "Queue Underflow\n";
    else {
        cout << frontLL->data << " dequeued from queue (LL)\n";
        Node* temp = frontLL;
        frontLL = frontLL->next;
        if (frontLL == NULL) rearLL = NULL;
        delete temp;
    }
}

void peekLLQ() {
    if (frontLL == NULL) cout << "Queue empty\n";
    else cout << "Front element: " << frontLL->data << "\n";
}

void displayLLQueue() {
    if (frontLL == NULL) cout << "Queue empty\n";
    else {
        cout << "Queue elements: ";
        Node* temp = frontLL;
        while (temp != NULL) {
            cout << temp->data << " ";
            temp = temp->next;
        }
        cout << "\n";
    }
}

// ---------------- MENU DRIVER ----------------
int main() {
    int choice, val;
    while (true) {
        cout << "\n=== MENU ===\n";
        cout << "1. Push (Array Stack)\n";
        cout << "2. Pop (Array Stack)\n";
        cout << "3. Peek (Array Stack)\n";
        cout << "4. Display (Array Stack)\n";
        cout << "5. Enqueue (Array Queue)\n";
        cout << "6. Dequeue (Array Queue)\n";
        cout << "7. Peek (Array Queue)\n";
        cout << "8. Display (Array Queue)\n";
        cout << "9. Push (LL Stack)\n";
        cout << "10. Pop (LL Stack)\n";
        cout << "11. Peek (LL Stack)\n";
        cout << "12. Display (LL Stack)\n";
        cout << "13. Enqueue (LL Queue)\n";
        cout << "14. Dequeue (LL Queue)\n";
        cout << "15. Peek (LL Queue)\n";
        cout << "16. Display (LL Queue)\n";
        cout << "0. Exit\n";
        cout << "Enter choice: ";
        cin >> choice;

        switch (choice) {
            case 1: cout << "Enter value: "; cin >> val; pushArr(val); break;
            case 2: popArr(); break;
            case 3: peekArr(); break;
            case 4: displayArrStack(); break;
            case 5: cout << "Enter value: "; cin >> val; enqueueArr(val); break;
            case 6: dequeueArr(); break;
            case 7: peekArrQ(); break;
            case 8: displayArrQueue(); break;
            case 9: cout << "Enter value: "; cin >> val; pushLL(val); break;
            case 10: popLL(); break;
            case 11: peekLL(); break;
            case 12: displayLLStack(); break;
            case 13: cout << "Enter value: "; cin >> val; enqueueLL(val); break;
            case 14: dequeueLL(); break;
            case 15: peekLLQ(); break;
            case 16: displayLLQueue(); break;
            case 0: cout << "Exiting...\n"; return 0;
            default: cout << "Invalid choice\n";
        }
    }
}