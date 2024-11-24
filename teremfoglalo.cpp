#include <iostream>
#include <vector>
#include <string>
#include <bits/stdc++.h>

using namespace std;
int keys=0;

struct Foglalas {
    int key;
    string tanar_neve;
    string tantargy;
    int terem_szam;
    int nap; // 1 - Hétfõ, 2 - Kedd, ..., 7 - Vasárnap
    int kezd_ido; // Kezdési idõpont (óra 0-tól 23-ig)
    int veg_ido;  // Befejezési idõpont (óra 0-tól 23-ig)
};

// Ellenõrzi, hogy van-e ütközés a foglalások között
bool utkozik(const Foglalas& uj_foglalas, const vector<Foglalas>& foglalasok) {
    for (const auto& foglalas : foglalasok) {
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
    cout << "Tanar neve: ";
    cin >> uj_foglalas.tanar_neve;
    cout << "Tantargy neve: ";
    cin >> uj_foglalas.tantargy;
    cout << "Terem szama: ";
    cin >> uj_foglalas.terem_szam;
    cout << "Nap (1-Hetfo, 2-Kedd, ..., 7-Vasarnap): ";
    cin >> uj_foglalas.nap;
    cout << "Kezdesi ido (0-23): ";
    cin >> uj_foglalas.kezd_ido;
    cout << "Befejezesi ido (0-23): ";
    cin >> uj_foglalas.veg_ido;

    if (uj_foglalas.kezd_ido >= uj_foglalas.veg_ido) {
        cout << "Hiba: A kezdesi idopont nem lehet nagyobb vagy egyenlo a befejezesi idopontnal.\n";
        return;
    }

    if (utkozik(uj_foglalas, foglalasok)) {
        cout << "Hiba: Utkozes van a teremfoglalások kozott.\n";
    } else {
        keys++;
        uj_foglalas.key=keys;
        foglalasok.push_back(uj_foglalas);
        cout << "Foglalas sikeresen hozzaadva.\n";
    }
}

// Teremfoglalások megjelenítése
void mutat_foglalasok(const vector<Foglalas>& foglalasok) {
    if (foglalasok.empty()) {
        cout << "Nincsenek jelenlegi foglalasok.\n";
        return;
    }

    for (const auto& foglalas : foglalasok) {
        cout << "Foglalas kulcs: " << foglalas.key
             << ", Tanar: " << foglalas.tanar_neve
             << ", Tantargy: " << foglalas.tantargy
             << ", Terem: " << foglalas.terem_szam
             << ", Nap: " << foglalas.nap
             << ", Kezdes: " << foglalas.kezd_ido
             << ", Befejezes: " << foglalas.veg_ido << "\n";
    }
}

void torol_foglalas(vector<Foglalas>& foglalasok) {
    int deletekey;

    cout << "Adja meg a torlendo foglalas kulcsat:\n";
    cin >> deletekey;

    auto it = find_if(foglalasok.begin(), foglalasok.end(), [&](const Foglalas& foglalas) {
        return foglalas.key == deletekey;
        });

    if (it != foglalasok.end()) {
        foglalasok.erase(it);
        cout << "Foglalas sikeresen torolve.\n";
    } else {
        cout << "Nincs ilyen foglalas.\n";
    }
}


int main() {
    vector<Foglalas> foglalasok;
    int valasz;

    while (true) {
        cout << "\nTeremfoglalasi rendszer - valasszon opciot:\n";
        cout << "1. Uj teremfoglalas\n";
        cout << "2. Foglalasok megjelenitese\n";
        cout << "3. Foglalasok torlese\n";
        cout << "4. Kilepes\n";
        cout << "Valasz: ";
        cin >> valasz;

        switch (valasz) {
            case 1:
                uj_foglalas(foglalasok);
                break;
            case 2:
                mutat_foglalasok(foglalasok);
                break;
            case 3:
                torol_foglalas(foglalasok);
                break;
            case 4:
                cout << "Kilepes...\n";
                return 0;
            default:
                cout << "Hibas valasztas, probalja ujra.\n";
        }
    }
}
