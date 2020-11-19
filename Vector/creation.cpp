#include <iostream>
#include <vector>

using namespace std;

int main()
{
    // This is how you create a vector of a int class.
    vector<int> g;

    for(int i = 1; i <= 10; i++)
        g.push_back(i);

    // This is for getting a pointer i which can be changed.
    cout << "\nOutput of begin and end: "; 
    for(auto i = g.begin(); i != g.end(); ++i) 
        cout << *i << " "; 
    
    // This is for getting constants.
    cout << "\nOutput of cbegin and cend: "; 
    for (auto i = g.cbegin(); i != g.cend(); ++i) 
        cout << *i << " "; 

    // Same as begin and end but in reverse order.
    cout << "\nOutput of rbegin and rend: "; 
    for (auto ir = g.rbegin(); ir != g.rend(); ++ir) 
        cout << *ir << " "; 
  
    // Same as cbegin and cend but in reverse order.
    cout << "\nOutput of crbegin and crend : "; 
    for (auto ir = g.crbegin(); ir != g.crend(); ++ir) 
        cout << *ir << " "; 

    return 0;
}