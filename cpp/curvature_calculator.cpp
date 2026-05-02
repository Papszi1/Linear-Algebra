#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

double my_function(double x) {
    return x * x;
}

struct PointData {
    double x;
    double y;
    double slope;
    double curvature;
};

vector<PointData> analyze_function(const vector<double>& x_coords) {
    int n = x_coords.size();
    vector<PointData> results;

    for (int i = 1; i < n - 1; i++) {
        double h_prev = x_coords[i] - x_coords[i-1];
        double h_next = x_coords[i+1] - x_coords[i];

        PointData p;
        p.x = x_coords[i];
        p.y = my_function(p.x);
        p.slope = (my_function(x_coords[i+1]) - my_function(x_coords[i-1])) / (h_prev + h_next);

        double slope_forward = (my_function(x_coords[i+1]) - my_function(x_coords[i])) / h_next;
        double slope_backward = (my_function(x_coords[i]) - my_function(x_coords[i-1])) / h_prev;
        p.curvature = (slope_forward - slope_backward) / ((h_prev + h_next) / 2.0);

        results.push_back(p);
    }
    
    return results;
}

int main() {
    vector<double> x_coordinates = {0.0, 0.2, 0.5, 1.2, 2.0};
    
    vector<PointData> analysis = analyze_function(x_coordinates);
    cout << "x   " << "y    " << "y'   " << "y''" << endl; 
    for (const auto& p : analysis) {
        cout << p.x << " " << p.y << " " << p.slope << "  " << p.curvature << endl;
    }
    cout << "Since the h intervalls are not equal, the calculated derivative values are not 100% match";
    return 0;
}