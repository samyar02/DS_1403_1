#include <iostream>
#include <vector>
#include <cmath>
#include <string>
using namespace std;

struct Tower {
    int a, b, c;
    long long left, right;

    Tower(int a, int b, int c) : a(a), b(b), c(c), left(0), right(0) {}
};

// Manual stack implementation
template <typename T>
class Stack {
    vector<T> elems;

public:
    void push(const T& elem) {
        elems.push_back(elem);
    }

    void pop() {
        if (!elems.empty()) {
            elems.pop_back();
        }
    }

    T& top() {
        return elems.back();
    }

    bool empty() const {
        return elems.empty();
    }
};

int main() {
    int n;
    cin >> n;
    vector<string> output;

    for (int t = 0; t < n; ++t) {
        int m;
        cin >> m;
        vector<Tower> towers;
        Stack<Tower*> tower_stack;
        long long leftsum = 0;

        for (int i = 0; i < m; ++i) {
            int a, b, c;
            cin >> a >> b >> c;
            Tower* tower = new Tower(a, b, c);
            towers.push_back(*tower); 
        }
        
        for (int i = 0; i < m; ++i) {
            Tower& tower = towers[i];
            tower.left = leftsum;
            while (!tower_stack.empty() && tower_stack.top()->a < tower.a) {
                leftsum -= tower_stack.top()->c;
                tower_stack.pop();
            }
            tower_stack.push(&tower);
            leftsum += tower.c;
        }

        while (!tower_stack.empty()) tower_stack.pop();

        long long righsum = 0;
        vector<int> result;

        for (int i = m - 1; i >= 0; --i) {
            Tower& tower = towers[i];
            tower.right = righsum;

            while (!tower_stack.empty() && tower_stack.top()->a < tower.a) {
                righsum -= tower_stack.top()->c;
                tower_stack.pop();
            }
            tower_stack.push(&tower);
            righsum += tower.c;

            result.push_back((int)ceil((double)tower.b / (tower.left + tower.right)));
        }

        string res_str = "";
        for (int i = result.size() - 1; i >= 0; --i) {
            res_str += to_string(result[i]);
            if (i != 0) res_str += " ";
        }
        output.push_back(res_str);
    }

    for (const string& res : output) {
        cout << res << endl;
    }

    return 0;
}
