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

//Foglalas torlese
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

//Foglalas szerkesztese
void szerkeszt_foglalas(vector<Foglalas>& foglalasok) {
    int editkey;

    cout << "Adja meg a szerkesztendo foglalas kulcsat:\n";
    cin >> editkey;

    auto it = find_if(foglalasok.begin(), foglalasok.end(), [&](const Foglalas& foglalas) {
        return foglalas.key == editkey;
    });

    if (it != foglalasok.end()) {
        Foglalas& foglalas = *it;
        cout << "Adja meg az uj adatokat:\n";
        cout << "Uj tanar neve: ";
        cin >> foglalas.tanar_neve;
        cout << "Uj tantargy neve: ";
        cin >> foglalas.tantargy;
        cout << "Uj terem szama: ";
        cin >> foglalas.terem_szam;
        cout << "Uj nap szama: ";
        cin >> foglalas.nap;
        cout << "Uj kezdesi ido (0-23): ";
        cin >> foglalas.kezd_ido;
        cout << "Uj befejezesi ido (0-23): ";
        cin >> foglalas.veg_ido;

        if (foglalas.kezd_ido >= foglalas.veg_ido) {
            cout << "Hiba: A kezdesi idopont nem lehet nagyobb vagy egyenlo a befejezesi idopontnal.\n";
            return;
        }

        if (utkozik(foglalas, foglalasok)) {
            cout << "Hiba: Az uj adatok utkoznek egy masik foglalassal.\n";
        } else {
            cout << "Foglalas sikeresen szerkesztve.\n";
        }
    } else {
        cout << "Nincs ilyen foglalas.\n";
    }
}

//Szures
void szures_foglalasok(const vector<Foglalas>& foglalasok) {
    int szuro_opcio;
    cout << "Szuro opcio:\n1. Tanar szerint\n2. Tantargy szerint\n3. Terem szerint\n4. Nap szerint\n5. Kezdesi ido szerint\n6. Befejezesi ido szerint\nValasztas: ";
    cin >> szuro_opcio;

    if (szuro_opcio == 1) {
        string tanar;
        cout << "Adja meg a tanar nevet: ";
        cin >> tanar;
        for (const auto& foglalas : foglalasok) {
            if (foglalas.tanar_neve == tanar) {
                cout << "Foglalas kulcs: " << foglalas.key
                     << ", Tanar: " << foglalas.tanar_neve
                     << ", Tantargy: " << foglalas.tantargy
                     << ", Terem: " << foglalas.terem_szam
                     << ", Nap: " << foglalas.nap
                     << ", Kezdes: " << foglalas.kezd_ido
                     << ", Befejezes: " << foglalas.veg_ido << "\n";
            }
        }
    }else if (szuro_opcio == 2) {
        string tantargy;
        cout << "Adja meg a tantargy nevet: ";
        cin >> tantargy;
        for (const auto& foglalas : foglalasok) {
            if (foglalas.tantargy == tantargy) {
                cout << "Foglalas kulcs: " << foglalas.key
                     << ", Tanar: " << foglalas.tanar_neve
                     << ", Tantargy: " << foglalas.tantargy
                     << ", Terem: " << foglalas.terem_szam
                     << ", Nap: " << foglalas.nap
                     << ", Kezdes: " << foglalas.kezd_ido
                     << ", Befejezes: " << foglalas.veg_ido << "\n";
            }
        }
    }else if (szuro_opcio == 3) {
        int terem;
        cout << "Adja meg a terem szamat: ";
        cin >> terem;
        for (const auto& foglalas : foglalasok) {
            if (foglalas.terem_szam == terem) {
                cout << "Foglalas kulcs: " << foglalas.key
                     << ", Tanar: " << foglalas.tanar_neve
                     << ", Tantargy: " << foglalas.tantargy
                     << ", Terem: " << foglalas.terem_szam
                     << ", Nap: " << foglalas.nap
                     << ", Kezdes: " << foglalas.kezd_ido
                     << ", Befejezes: " << foglalas.veg_ido << "\n";
            }
        }
    }else if (szuro_opcio == 4) {
        int nap;
        cout << "Adja meg a napot (1-Hetfo, ..., 7-Vasarnap): ";
        cin >> nap;
        for (const auto& foglalas : foglalasok) {
            if (foglalas.nap == nap) {
                cout << "Foglalas kulcs: " << foglalas.key
                     << ", Tanar: " << foglalas.tanar_neve
                     << ", Tantargy: " << foglalas.tantargy
                     << ", Terem: " << foglalas.terem_szam
                     << ", Nap: " << foglalas.nap
                     << ", Kezdes: " << foglalas.kezd_ido
                     << ", Befejezes: " << foglalas.veg_ido << "\n";
            }
        }
    }else if (szuro_opcio == 5) {
        int kezd_ido;
        cout << "Adja meg a kezdesi idot: ";
        cin >> kezd_ido;
        for (const auto& foglalas : foglalasok) {
            if (foglalas.kezd_ido == kezd_ido) {
                cout << "Foglalas kulcs: " << foglalas.key
                     << ", Tanar: " << foglalas.tanar_neve
                     << ", Tantargy: " << foglalas.tantargy
                     << ", Terem: " << foglalas.terem_szam
                     << ", Nap: " << foglalas.nap
                     << ", Kezdes: " << foglalas.kezd_ido
                     << ", Befejezes: " << foglalas.veg_ido << "\n";
            }
        }
    }else if (szuro_opcio == 6) {
        int veg_ido;
        cout << "Adja meg a vegzesi idot: ";
        cin >> veg_ido;
        for (const auto& foglalas : foglalasok) {
            if (foglalas.veg_ido == veg_ido) {
                cout << "Foglalas kulcs: " << foglalas.key
                     << ", Tanar: " << foglalas.tanar_neve
                     << ", Tantargy: " << foglalas.tantargy
                     << ", Terem: " << foglalas.terem_szam
                     << ", Nap: " << foglalas.nap
                     << ", Kezdes: " << foglalas.kezd_ido
                     << ", Befejezes: " << foglalas.veg_ido << "\n";
            }
        }
    }
    else {
        cout << "Hibas valasztas.\n";
    }
}

//Naptari nezet
void naptari_nezet(const vector<Foglalas>& foglalasok) {
    const vector<string> napok = {"Hetfo", "Kedd", "Szerda", "Csutortok", "Pentek", "Szombat", "Vasarnap"};

    cout << "\n*** Heti naptari nezet ***\n";

    for (int nap = 1; nap <= 7; ++nap) {
        cout << "\n" << napok[nap - 1] << ":\n";

        // Óránkénti bontás
        for (int ora = 0; ora < 24; ++ora) {
            bool foglalt = false;
            for (const auto& foglalas : foglalasok) {
                if (foglalas.nap == nap && foglalas.kezd_ido <= ora && foglalas.veg_ido > ora) {
                    cout << ora << ":00 - " << (ora + 1) << ":00: "
                         << foglalas.tantargy << " (" << foglalas.tanar_neve << ", Terem: " << foglalas.terem_szam << ")\n";
                    foglalt = true;
                    break;
                }
            }
            if (!foglalt) {
                cout << ora << ":00 - " << (ora + 1) << ":00: SZABAD\n";
            }
        }
    }
}


int main() {
    vector<Foglalas> foglalasok;
    int valasz;

    while (true) {
        cout << "\nTeremfoglalasi rendszer - valasszon opciot:\n";
        cout << "1. Uj teremfoglalas\n";
        cout << "2. Foglalasok megjelenitese\n";
        cout << "3. Foglalas torlese\n";
        cout << "4. Foglalas szerkesztese\n";
        cout << "5. Szures\n";
        cout << "6. Naptari nezet\n";
        cout << "7. Kilepes\n";
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
                szerkeszt_foglalas(foglalasok);
                break;
            case 5:
                szures_foglalasok(foglalasok);
                break;
            case 6:
                naptari_nezet(foglalasok);
                break;
            case 7:
                cout << "Kilepes...\n";
                return 0;
            default:
                cout << "Hibas valasztas, probalja ujra.\n";
        }
    }
}
