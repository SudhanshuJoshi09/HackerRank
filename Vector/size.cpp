#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> g;

    for(int i = 1; i <= 5; i++)
        g.push_back(i);

    // Checking the size of the vector.
    cout << "Size: " << g.size() << endl;
    // Checking the max capacity of the vector.
    cout << "Capacity: " << g.capacity() << endl;
    // Checking the max size possible.
    cout << "Max_Size: " << g.max_size() << endl;
    
    g.resize(4);

    cout << "Size: " << g.size() << endl;

    // For checking weather the vector is empty or not.
    if (g.empty() == false) 
        cout << "Vector is not empty" << endl;
    else
        cout << "Vector is empty";

    // I don't know what this statement does.
    g.shrink_to_fit();
    for (auto it = g.begin(); it != g.end(); it++) 
        cout << *it << " "; 

    return 0;
}