#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct Foglalas {
    string tanar_neve;
    string tantargy;
    int terem_szam;
    int nap;
    int kezd_ido;
    int veg_ido;
};

//meglévő foglalások részleteinek kilistázása
void mutat_foglalasok(vector<Foglalas> foglalasok) {
    cout << ("\n\t\t Lefoglalt termek");
    cout << ("\n\t\t ----------------\n\n");
    
    if (foglalasok.empty())
        cout << "Jelenleg nincsenek lefoglalt termek\n";
    else {
        for (auto& a : foglalasok) {
            cout << ("Tanar neve: " + a.tanar_neve + "\n");
            cout << ("Tantargy: " + a.tantargy + "\n");
            cout << ("Nap: " + to_string(a.nap) + "\n");
            cout << ("Kezdesi idopont: " + to_string(a.kezd_ido) + "\n");
            cout << ("Befejezesi idopont: " + to_string(a.veg_ido) + "\n");
            cout << ("----------------------------------------\n");
        }
    }
}

int main()
{
    vector<Foglalas> foglalasok;
    mutat_foglalasok(foglalasok);
}
