class Solution {
public:
    int minFlips(int a, int b, int c) {
        int bitwiseOR = a | b;
        //cout << bitwiseOR << endl;
        int bwORxorC = bitwiseOR ^ c; 
        //returns 1 if at least one need to be changed
        //cout << bwORxorC << endl;
        int filteredC = bwORxorC & c;
        //cout << filteredC << endl;

        int result = 0;
        while(bwORxorC != 0){
            if (bwORxorC % 2 == 1){
                if (filteredC % 2 == 1){
                    result += 1;
                }
                else{ // if filteredC % 2 == 0
                    result += ((a % 2) ^ (filteredC % 2));
                    result += ((b % 2) ^ (filteredC % 2));
                }
            }
            a /= 2;
            b /= 2;
            bwORxorC /= 2;
            filteredC /= 2;
        }
        //cout << result << endl;

        return result;
    }
};