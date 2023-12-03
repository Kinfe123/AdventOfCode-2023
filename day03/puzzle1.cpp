#include <iostream>
#include <fstream>
#include <vector>
#include <set>

using namespace std;

set<pair<int, int>> start_indx;
vector<string> lists;

bool inbound(int x, int y) {
    return 0 <= x < lists.size() && 0 <= y < lists[0].size();
}

int main() {
    ifstream file("./input.txt");
    string line;
    while (getline(file, line)) {
        lists.push_back(line.substr(0, line.size() - 1));
    }
    file.close();

    int res = 0;

    int dxn[4][2] = {{1, 0}, {0, 1}, {1, 1}, {-1, -1}};

    for (int r = 0; r < lists.size(); r++) {
        string s = "";
        pair<int, int> start = {-1, -1};
        for (int c = 0; c < lists[r].size(); c++) {
            char curr = lists[r][c];
            if (curr != '.' && !isdigit(curr)) {
                for (int cr = r - 1; cr <= r + 1; cr++) {
                    for (int cc = c - 1; cc <= c + 1; cc++) {
                        if (inbound(cr, cc) && isdigit(lists[cr][cc])) {
                            while (cc > 0 && isdigit(lists[cr][cc - 1])) {
                                cc--;
                            }
                            start_indx.insert(make_pair(cr, cc));
                        }
                    }
                }
            }
        }
    }

    for (pair<int, int> start : start_indx) {
        int start_x = start.first;
        int start_y = start.second;
        string curr_num = "";
        while (start_y < lists[0].size() && isdigit(lists[start_x][start_y])) {
            curr_num += lists[start_x][start_y];
            start_y++;
        }
        res += stoi(curr_num);
    }

    cout << res << endl;

    return 0;
}
