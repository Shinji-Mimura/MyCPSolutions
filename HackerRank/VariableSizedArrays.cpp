#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    
    int n_arrays, queries;
    cin >> n_arrays >> queries;
    
    vector<vector<int>> vector_of_vectors;
    
    for (int i = 0; i < n_arrays; i++) {
        int vector_size;
        cin >> vector_size;
        vector<int> my_vec;
        for(int j = 0; j < vector_size; j++){
            int number;
            cin >> number;
            my_vec.push_back(number);
        }
        vector_of_vectors.push_back(my_vec);
    }
    
    int index_vector, value_of_index_vector;
    
    for(int i=0; i<n_arrays; i++){
        cin >> index_vector >> value_of_index_vector;
        cout << vector_of_vectors[index_vector][value_of_index_vector]<< endl;
    }
    
    return 0;
}

