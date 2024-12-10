import tkinter as tk
from tkinter import ttk, messagebox


class Foglalas:
    def __init__(self, key, tanar_neve, tantargy, terem_szam, nap, kezd_ido, veg_ido):
        self.key = key
        self.tanar_neve = tanar_neve
        self.tantargy = tantargy
        self.terem_szam = terem_szam
        self.nap = nap
        self.kezd_ido = kezd_ido
        self.veg_ido = veg_ido


class SzerkesztDialog:
    def __init__(self, parent, foglalas):
        self.result = None
        self.top = tk.Toplevel(parent)
        self.top.title("Foglalás Szerkesztése")
        self.top.grab_set()  # Make the dialog modal

        # Create and fill the entry fields
        ttk.Label(self.top, text="Tanár neve:").grid(row=0, column=0, padx=5, pady=5)
        self.tanar_entry = ttk.Entry(self.top)
        self.tanar_entry.insert(0, foglalas.tanar_neve)
        self.tanar_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.top, text="Tantárgy:").grid(row=1, column=0, padx=5, pady=5)
        self.tantargy_entry = ttk.Entry(self.top)
        self.tantargy_entry.insert(0, foglalas.tantargy)
        self.tantargy_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.top, text="Terem szám:").grid(row=2, column=0, padx=5, pady=5)
        self.terem_entry = ttk.Entry(self.top)
        self.terem_entry.insert(0, str(foglalas.terem_szam))
        self.terem_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(self.top, text="Nap:").grid(row=3, column=0, padx=5, pady=5)
        self.nap_combo = ttk.Combobox(self.top,
                                      values=["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"])
        self.nap_combo.current(foglalas.nap - 1)
        self.nap_combo.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(self.top, text="Kezdési idő:").grid(row=4, column=0, padx=5, pady=5)
        self.kezdes_combo = ttk.Combobox(self.top, values=[str(i) for i in range(24)])
        self.kezdes_combo.set(str(foglalas.kezd_ido))
        self.kezdes_combo.grid(row=4, column=1, padx=5, pady=5)

        ttk.Label(self.top, text="Befejezési idő:").grid(row=5, column=0, padx=5, pady=5)
        self.befejezes_combo = ttk.Combobox(self.top, values=[str(i) for i in range(24)])
        self.befejezes_combo.set(str(foglalas.veg_ido))
        self.befejezes_combo.grid(row=5, column=1, padx=5, pady=5)

        # Save button
        ttk.Button(self.top, text="Mentés",
                   command=self.save).grid(row=6, column=0, columnspan=2, pady=20)

    def save(self):
        try:
            self.result = {
                'tanar_neve': self.tanar_entry.get(),
                'tantargy': self.tantargy_entry.get(),
                'terem_szam': int(self.terem_entry.get()),
                'nap': self.nap_combo.current() + 1,
                'kezd_ido': int(self.kezdes_combo.get()),
                'veg_ido': int(self.befejezes_combo.get())
            }
            self.top.destroy()
        except ValueError:
            messagebox.showerror("Hiba", "Érvénytelen bemenet!")


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
        self.create_listazas_tab()

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
        self.kezdes_combo = ttk.Combobox(uj_foglalas_frame, values=[str(i) for i in range(24)])
        self.kezdes_combo.grid(row=4, column=1, padx=5, pady=5)

        ttk.Label(uj_foglalas_frame, text="Befejezési idő:").grid(row=5, column=0, padx=5, pady=5)
        self.befejezes_combo = ttk.Combobox(uj_foglalas_frame, values=[str(i) for i in range(24)])
        self.befejezes_combo.grid(row=5, column=1, padx=5, pady=5)

        # Submit button
        ttk.Button(uj_foglalas_frame, text="Foglalás hozzáadása",
                   command=self.add_foglalas).grid(row=6, column=0, columnspan=2, pady=20)

    def create_listazas_tab(self):
        listazas_frame = ttk.Frame(self.notebook)
        self.notebook.add(listazas_frame, text='Foglalások')

        # Treeview for listings
        self.tree = ttk.Treeview(listazas_frame,
                                 columns=('Key', 'Tanár', 'Tantárgy', 'Terem', 'Nap', 'Kezdés', 'Befejezés'),
                                 show='headings')

        # Define headings
        self.tree.heading('Key', text='Azonosító')
        self.tree.heading('Tanár', text='Tanár')
        self.tree.heading('Tantárgy', text='Tantárgy')
        self.tree.heading('Terem', text='Terem')
        self.tree.heading('Nap', text='Nap')
        self.tree.heading('Kezdés', text='Kezdés')
        self.tree.heading('Befejezés', text='Befejezés')

        # Column widths
        for col in ('Key', 'Tanár', 'Tantárgy', 'Terem', 'Nap', 'Kezdés', 'Befejezés'):
            self.tree.column(col, width=100)

        self.tree.pack(expand=True, fill='both')

        # Buttons frame
        button_frame = ttk.Frame(listazas_frame)
        button_frame.pack(fill='x', padx=5, pady=5)

        ttk.Button(button_frame, text="Szerkesztés",
                   command=self.edit_foglalas).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Törlés",
                   command=self.delete_foglalas).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Frissítés",
                   command=self.refresh_lista).pack(side='left', padx=5)

    def edit_foglalas(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Figyelmeztetés", "Válassz ki egy foglalást a szerkesztéshez!")
            return

        key = int(self.tree.item(selected_item)['values'][0])
        foglalas = next((f for f in self.foglalasok if f.key == key), None)

        if foglalas:
            dialog = SzerkesztDialog(self.root, foglalas)
            self.root.wait_window(dialog.top)

            if dialog.result:
                # Check for conflicts with other bookings
                if dialog.result['kezd_ido'] >= dialog.result['veg_ido']:
                    messagebox.showerror("Hiba",
                                         "A kezdési időpontnak kisebbnek kell lennie, mint a befejezési időpont!")
                    return
                for f in self.foglalasok:
                    if (f.key != key and  # Don't check against itself
                            f.terem_szam == dialog.result['terem_szam'] and
                            f.nap == dialog.result['nap'] and
                            dialog.result['kezd_ido'] < f.veg_ido and
                            dialog.result['veg_ido'] > f.kezd_ido):
                        messagebox.showerror("Hiba", "Ütközés egy másik foglalással!")
                        return

                # Update the booking
                foglalas.tanar_neve = dialog.result['tanar_neve']
                foglalas.tantargy = dialog.result['tantargy']
                foglalas.terem_szam = dialog.result['terem_szam']
                foglalas.nap = dialog.result['nap']
                foglalas.kezd_ido = dialog.result['kezd_ido']
                foglalas.veg_ido = dialog.result['veg_ido']

                self.refresh_lista()
                messagebox.showinfo("Siker", "Foglalás sikeresen módosítva!")

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
            self.refresh_lista()

            # Clear inputs
            self.tanar_entry.delete(0, tk.END)
            self.tantargy_entry.delete(0, tk.END)
            self.terem_entry.delete(0, tk.END)
            self.nap_combo.set('')
            self.kezdes_combo.set('')
            self.befejezes_combo.set('')

        except ValueError:
            messagebox.showerror("Hiba", "Érvénytelen bemenet!")

    def delete_foglalas(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Figyelmeztetés", "Válassz ki egy foglalást!")
            return

        if messagebox.askyesno("Törlés", "Biztosan törölni szeretnéd ezt a foglalást?"):
            key = int(self.tree.item(selected_item)['values'][0])
            self.foglalasok = [f for f in self.foglalasok if f.key != key]
            self.refresh_lista()

    def refresh_lista(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for foglalas in self.foglalasok:
            napok = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"]
            self.tree.insert('', 'end', values=(
                foglalas.key,
                foglalas.tanar_neve,
                foglalas.tantargy,
                foglalas.terem_szam,
                napok[foglalas.nap - 1],
                f"{foglalas.kezd_ido}:00",
                f"{foglalas.veg_ido}:00"
            ))

def main():
    root = tk.Tk()
    TeremFoglaloApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
