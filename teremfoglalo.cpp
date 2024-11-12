#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct Foglalas {
    string tanar_neve;
    string tantargy;
    int terem_szam;
    int nap; // 1 - Hétfő, 2 - Kedd, ..., 7 - Vasárnap
    int kezd_ido; // Kezdési időpont (óra 0-tól 23-ig)
    int veg_ido;  // Befejezési időpont (óra 0-tól 23-ig)
};

bool utkozik(const Foglalas& uj_foglalas, const vector<Foglalas>& foglalasok) {
    for (const auto &foglalas: foglalasok) {
        if (foglalas.terem_szam == uj_foglalas.terem_szam && foglalas.nap == uj_foglalas.nap) {
            if ((uj_foglalas.kezd_ido < foglalas.veg_ido && uj_foglalas.veg_ido > foglalas.kezd_ido)) {
                return true;
            }
        }
    }
    return false;
}
// Új teremfoglalás hozzáadása
void uj_foglalas(vector<Foglalas>& foglalasok) {
    Foglalas uj_foglalas;
    cout << "Tanár neve: ";
    cin >> uj_foglalas.tanar_neve;
    cout << "Tantárgy neve: ";
    cin >> uj_foglalas.tantargy;
    cout << "Terem száma: ";
    cin >> uj_foglalas.terem_szam;
    cout << "Nap (1-Hétfő, 2-Kedd, ..., 7-Vasárnap): ";
    cin >> uj_foglalas.nap;
    cout << "Kezdési idő (0-23): ";
    cin >> uj_foglalas.kezd_ido;
    cout << "Befejezési idő (0-23): ";
    cin >> uj_foglalas.veg_ido;

    if (uj_foglalas.kezd_ido >= uj_foglalas.veg_ido) {
        cout << "Hiba: A kezdési időpont nem lehet nagyobb vagy egyenlő a befejezési időpontnal.\n";
        return;
    }
    if (utkozik(uj_foglalas, foglalasok)) {
        cout << "Hiba: Utkozes van a teremfoglalások kozott.\n";
    } else {
        foglalasok.push_back(uj_foglalas);
        cout << "Foglalas sikeresen hozzaadva.\n";
    }
}

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

int main() {
    vector<Foglalas> foglalasok;
    uj_foglalas(foglalasok);
    return 0;
}
