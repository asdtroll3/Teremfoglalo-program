import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


class Foglalas:
    def __init__(self, key, tanar_neve, tantargy, terem_szam, nap, kezd_ido, veg_ido):
        self.key = key
        self.tanar_neve = tanar_neve
        self.tantargy = tantargy
        self.terem_szam = terem_szam
        self.nap = nap
        self.kezd_ido = kezd_ido
        self.veg_ido = veg_ido

class TeremFoglaloApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Terem Foglaló Rendszer")
        self.root.geometry("800x600")

        self.foglalasok = []
        self.keys = 0

        # Create notebook for tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=5)

        # Create tabs
        self.create_uj_foglalas_tab()

    def create_uj_foglalas_tab(self):
        uj_foglalas_frame = ttk.Frame(self.notebook)
        self.notebook.add(uj_foglalas_frame, text='Új Foglalás')

        # Input fields
        ttk.Label(uj_foglalas_frame, text="Tanár neve:").grid(row=0, column=0, padx=5, pady=5)
        self.tanar_entry = ttk.Entry(uj_foglalas_frame)
        self.tanar_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(uj_foglalas_frame, text="Tantárgy:").grid(row=1, column=0, padx=5, pady=5)
        self.tantargy_entry = ttk.Entry(uj_foglalas_frame)
        self.tantargy_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(uj_foglalas_frame, text="Terem szám:").grid(row=2, column=0, padx=5, pady=5)
        self.terem_entry = ttk.Entry(uj_foglalas_frame)
        self.terem_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(uj_foglalas_frame, text="Nap:").grid(row=3, column=0, padx=5, pady=5)
        self.nap_combo = ttk.Combobox(uj_foglalas_frame,
                                      values=["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"])
        self.nap_combo.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(uj_foglalas_frame, text="Kezdési idő:").grid(row=4, column=0, padx=5, pady=5)
        self.kezdes_combo = ttk.Combobox(uj_foglalas_frame, values=list(range(24)))
        self.kezdes_combo.grid(row=4, column=1, padx=5, pady=5)

        ttk.Label(uj_foglalas_frame, text="Befejezési idő:").grid(row=5, column=0, padx=5, pady=5)
        self.befejezes_combo = ttk.Combobox(uj_foglalas_frame, values=list(range(24)))
        self.befejezes_combo.grid(row=5, column=1, padx=5, pady=5)

        # Submit button
        ttk.Button(uj_foglalas_frame, text="Foglalás hozzáadása",
                   command=self.add_foglalas).grid(row=6, column=0, columnspan=2, pady=20)

    def add_foglalas(self):
        try:
            tanar = self.tanar_entry.get()
            tantargy = self.tantargy_entry.get()
            terem = int(self.terem_entry.get())
            nap = self.nap_combo.current() + 1
            kezdes = int(self.kezdes_combo.get())
            befejezes = int(self.befejezes_combo.get())

            if not all([tanar, tantargy, terem, nap, kezdes, befejezes]):
                messagebox.showerror("Hiba", "Minden mezőt ki kell tölteni!")
                return

            uj_foglalas = Foglalas(self.keys, tanar, tantargy, terem, nap, kezdes, befejezes)

            if kezdes >= befejezes:
                messagebox.showerror("Hiba", "A kezdési időpontnak kisebbnek kell lennie, mint a befejezési időpont!")
                return

            # Check for conflicts
            for foglalas in self.foglalasok:
                if (foglalas.terem_szam == terem and foglalas.nap == nap and
                        kezdes < foglalas.veg_ido and befejezes > foglalas.kezd_ido):
                    messagebox.showerror("Hiba", "Ütközés egy másik foglalással!")
                    return

            self.foglalasok.append(uj_foglalas)
            self.keys += 1

            messagebox.showinfo("Siker", "Foglalás sikeresen hozzáadva!")


            # Clear inputs
            self.tanar_entry.delete(0, tk.END)
            self.tantargy_entry.delete(0, tk.END)
            self.terem_entry.delete(0, tk.END)
            self.nap_combo.set('')
            self.kezdes_combo.set('')
            self.befejezes_combo.set('')

        except ValueError:
            messagebox.showerror("Hiba", "Érvénytelen bemenet!")

def main():
    root = tk.Tk()
    app = TeremFoglaloApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()