#include <iostream>
#include <vector>
using namespace std;

struct LU_struct {
    vector<vector<double>> L;
    vector<vector<double>> U;
};

LU_struct LU_decomposition(vector<vector<double>>& A);
vector<double> forward_substitution(vector<vector<double>>& L, vector<double>& b);
vector<double> backward_substitution(vector<vector<double>>& U, vector<double>& y);
void print_matrix (vector<vector<double>>& A);
void print_vector(vector<double>& y);

int main() {
    cout << "Start" << endl;
    vector<vector<double>> A = {{2,1,1},{4,3,3},{8,7,9}};
    cout << "Original matrix" << endl;
    print_matrix(A);

    auto [L, U] = LU_decomposition(A);    
    cout << "U matrix: " << endl;
    print_matrix(U);
    cout << "L matrix: " << endl;
    print_matrix(L);

    vector<double> b = {4, 10, 24};
    vector<double> y = forward_substitution(L, b);

    vector<double> x = backward_substitution(U, y);

    return 0;
}

LU_struct LU_decomposition(vector<vector<double>>& A) {
    double n = A.size();
    cout << "The size of the matrix: " << n << endl; 
    vector<vector<double>> L(n, vector<double>(n, 0));
    vector<vector<double>> U = A;

    int pivot_ind = 0;
    while (pivot_ind < n) {
        double pivot = U[pivot_ind][pivot_ind];
        int row = pivot_ind + 1;
        while (row < n) {
            L[row][pivot_ind] = U[row][pivot_ind] / U[pivot_ind][pivot_ind];
            int col = pivot_ind + 1;
            while (col < n) {
                U[row][col] -= L[row][pivot_ind] * U[pivot_ind][col];
                col++;
            }

            row++;
        }
        L[pivot_ind][pivot_ind] = 1;
        pivot_ind++;
    }
    return {L, U};
}

vector<double> forward_substitution(vector<vector<double>>& L, vector<double>& b) {
    int n = b.size();
    cout << "original b vector: " << endl;
    print_vector(b);
    vector<double> y(b.size(), 0);

    int row = 0;
    while ( row < n ) {
        int col = 0;
        double dot_product = 0;
        while (col < row) {
            dot_product += (L[row][col] * y[col]);
            col++;
        }
        y[row] = b[row] - dot_product;
        row++;
    }
    cout << "The y vector: " << endl;
    print_vector(y);
    return y;
}

vector<double> backward_substitution(vector<vector<double>>& U, vector<double>& y) {
    int n = y.size();
    vector<double> x(n, 0);
    cout << "backward substituion" << endl;


    int row = n - 1;
    while (row >= 0) {
        int col = row + 1;
        double dot_product = 0;
        while (col < n) {
            dot_product += U[row][col] * x[col];

            col++;
        }
        x[row] = (y[row] - dot_product) / U[row][row];
        row--;
    }

    cout << "solution: " << endl;
    print_vector(x);
    return x;
}

void print_matrix (vector<vector<double>>& A) {
    for (vector<double> row : A) {
        for (double num: row) {
            cout << num << " ";
        }
        cout << endl;
    }
    cout << endl;
}

void print_vector(vector<double>& y) {
    for (double num : y) {
        cout << num << " ";
    }
    cout << endl << endl;
}