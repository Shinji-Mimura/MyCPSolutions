
// Solution based on Python code by dityavyas1603

#include <bits/stdc++.h>

using namespace std;

int steadyGene(string gene) {
    
    map<char, int> counter;
    
    int times = gene.size() / 4;
    
    int upper = 0;
    int lower = 0;
    
    int minlen = gene.size();
        
    for (int i = 0; i < gene.size(); i++) {
        counter[gene[i]]++;
    }    
       
    if (counter['A'] == times && counter['T'] == times && counter['C'] == times && counter['G'] == times) {
        return 0;
    }
    
    else {
             
        while(upper < gene.size() && lower < gene.size()){
            while ((counter['A'] > times || counter['T'] > times || counter['C'] > times || counter['G'] > times) && upper < gene.size()) {
                counter[gene[upper]]--;
                upper++;
            }
            
            while (counter['A'] <= times && counter['T'] <= times && counter['C'] <= times && counter['G'] <= times) {
                counter[gene[lower]]++;
                lower++;
            }
            
            if ((upper - lower) < minlen){
                minlen = upper-lower+1;
            }            
            
        }

        return minlen;
    }

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string gene;
    getline(cin, gene);

    int result = steadyGene(gene);

    fout << result << "\n";

    fout.close();

    return 0;
}

