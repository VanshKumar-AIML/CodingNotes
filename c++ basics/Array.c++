#include <iostream>
using namespace std;

// Function Declarations
int choice();
    int array();                //for array declaration do
        int arr1d();            //datatype array_name={elements..};
        int arr2d();
        int arr3d();

int main() {
    array();
    return 0;
}

int array() {
    int c;
    cout << "Enter a choice (1D array(1), 2D array(2), 3D array(3)): ";
    cin >> c;

    if (c == 1)
        arr1d();
    else if (c == 2)
        arr2d();
    else if (c == 3)
        arr3d();
    else
        cout << "Invalid choice!" << endl;

    return 0;
}

int arr1d() {
    int n, arr[10];
    cout << "Enter number of elements: ";
    cin >> n;
    cout << "Enter elements: ";
    for (int i = 0; i < n; i++) cin >> arr[i];

    cout << "1D Array is: ";
    for (int i = 0; i < n; i++) cout << arr[i] << " ";
    cout << endl;

    return 0;
}

int arr2d() {
    int x, y, arr[10][10];
    cout << "Enter rows and columns: ";
    cin >> x >> y;
    cout << "Enter elements row-wise: ";
    for (int i = 0; i < x; i++)
        for (int j = 0; j < y; j++)
            cin >> arr[i][j];

    cout << "The matrix (2D array):\n";
    for (int i = 0; i < x; i++) {
        for (int j = 0; j < y; j++)
            cout << arr[i][j] << "\t";
        cout << endl;
    }
    return 0;
}

int arr3d() {
    int x, y, z, arr[5][5][5];
    cout << "Enter 3 dimensions: ";
    cin >> x >> y >> z;
    cout << "Enter elements: ";
    for (int i = 0; i < x; i++)
        for (int j = 0; j < y; j++)
            for (int k = 0; k < z; k++)
                cin >> arr[i][j][k];

    cout << "3D Array:\n";
    for (int i = 0; i < x; i++) {
        for (int j = 0; j < y; j++) {
            for (int k = 0; k < z; k++) {
                cout << arr[i][j][k] << "\t";
            }
            cout << endl;
        }
        cout << endl;
    }

    return 0;
}