"""Kolorowa nauka klawiatury dla dzieci. Uruchom: python mistrz_klawiatury.py."""

import random
import tkinter as tk
from tkinter import font, simpledialog


BACKGROUND = "#FFF7E8"
INK = "#34405C"
PURPLE = "#7655BC"
GREEN = "#23846B"
WORDS = (
    "KOT", "DOM", "MAMA", "TATA", "LAS", "OSA", "SOK", "OKO", "NOS", "ALA",
    "KREDKA", "KLOCKI", "LALKA", "FARBY", "ZABAWA", "GRUPA",
    "PIERNIK", "KOPERNIK", "RATUSZ", "MOST",
    "KURA", "KROWA", "SIANO", "POLE", "SAD", "TRAKTOR",
    "PRZEDSZKOLE", "DZIECI", "PANI", "PAN", "SALA", "KREDKI", "PUZZLE",
    "PLASTELINA", "RYSUNEK", "PIOSENKA", "BULWAR", "RZEKA", "GOTYK",
    "FLISAK", "KATEDRA", "PLANETA", "TEATR", "MUZEUM", "MIASTO",
    "WYCIECZKA", "ROLNIK", "MLEKO", "KACZKA", "KOZA", "OWCA", "KOGUT",
    "STAW", "DOMEK", "OBORA", "STAJNIA",
)
PRAISE = ("Brawo!", "Wspaniale!", "Super!", "Pięknie!", "Świetnie Ci idzie!")


class KeyboardGame:
    def __init__(self, root, player_name=""):
        self.root = root
        self.player_name = player_name
        self.root.title("Mistrzyni klawiatury — zabawa w pisanie")
        self.root.geometry("1000x800")
        self.root.minsize(820, 720)
        self.root.configure(bg=BACKGROUND)
        self.mode = "Litery"
        self.target = ""
        self.position = 0
        self.score = 0
        self.pending = None
        self.waiting = False
        self.last_target = None
        self.used_words = set()
        self.key_labels = {}
        self.mode_buttons = {}
        self.big_font = font.Font(family="Arial", size=76, weight="bold")

        tk.Label(root, text="Mistrzyni klawiatury", font=("Arial", 27, "bold"),
                 bg=BACKGROUND, fg=PURPLE).pack(pady=(16, 3))
        tk.Label(root, text="Znajdź klawisz i naciśnij go. Bawimy się bez pośpiechu!",
                 font=("Arial", 15), bg=BACKGROUND, fg=INK).pack()

        modes = tk.Frame(root, bg=BACKGROUND)
        modes.pack(pady=12)
        for mode in ("Litery", "Cyferki", "Słowa"):
            button = tk.Button(modes, text=mode, font=("Arial", 16, "bold"),
                               width=12, bd=0, padx=8, pady=9, takefocus=False,
                               command=lambda choice=mode: self.change_mode(choice))
            button.pack(side=tk.LEFT, padx=5)
            self.mode_buttons[mode] = button

        self.canvas = tk.Canvas(root, width=200, height=105, bg=BACKGROUND,
                                highlightthickness=0)
        self.canvas.pack()
        self.draw_cat()

        self.instruction = tk.Label(root, font=("Arial", 18), bg=BACKGROUND, fg=INK)
        self.instruction.pack(pady=(4, 0))
        self.target_label = tk.Label(root, font=self.big_font, bg=BACKGROUND,
                                     fg=PURPLE, height=1)
        self.target_label.pack()
        self.word_progress = tk.Label(root, font=("Arial", 18, "bold"),
                                      bg=BACKGROUND, fg=GREEN)
        self.word_progress.pack()
        self.message = tk.Label(root, text="Dasz radę!", font=("Arial", 20, "bold"),
                                bg=BACKGROUND, fg=GREEN)
        self.message.pack(pady=6)
        self.stars = tk.Label(root, font=("Arial", 21), bg=BACKGROUND, fg="#AC7100")
        self.stars.pack()

        keyboard = tk.Frame(root, bg=BACKGROUND)
        keyboard.pack(pady=12)
        for row in ("1234567890", "QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"):
            frame = tk.Frame(keyboard, bg=BACKGROUND)
            frame.pack(pady=3)
            for letter in row:
                label = tk.Label(frame, text=letter, width=4, height=1,
                                 font=("Arial", 17, "bold"), bg="#E7E0F4", fg=INK,
                                 relief=tk.RAISED, bd=2, padx=3, pady=5)
                label.pack(side=tk.LEFT, padx=3)
                self.key_labels[letter] = label

        controls = tk.Frame(root, bg=BACKGROUND)
        controls.pack(pady=(0, 6))
        tk.Button(controls, text="Od początku", font=("Arial", 12),
                  command=self.reset, takefocus=False).pack(side=tk.LEFT, padx=8)
        tk.Button(controls, text="Pełny ekran (F11)", font=("Arial", 12),
                  command=self.toggle_fullscreen, takefocus=False).pack(side=tk.LEFT, padx=8)
        tk.Label(root, text="Podświetlony klawisz to podpowiedź.   •   Esc: wyjście z pełnego ekranu",
                 font=("Arial", 11), bg=BACKGROUND, fg=INK).pack(pady=(0, 8))

        root.bind("<KeyPress>", self.on_key)
        root.bind("<F11>", self.toggle_fullscreen)
        root.bind("<Escape>", self.exit_fullscreen)
        self.change_mode("Litery")

    def draw_cat(self, happy=False):
        c = self.canvas
        c.delete("all")
        c.create_polygon(45, 45, 48, 8, 80, 30, fill="#F7B85C", outline=INK, width=2)
        c.create_polygon(120, 30, 152, 8, 155, 45, fill="#F7B85C", outline=INK, width=2)
        c.create_oval(40, 22, 160, 102, fill="#F7B85C", outline=INK, width=2)
        for x in (76, 124):
            if happy:
                c.create_arc(x - 8, 44, x + 8, 62, start=0, extent=180,
                             style=tk.ARC, outline=INK, width=3)
            else:
                c.create_oval(x - 4, 48, x + 4, 59, fill=INK, outline=INK)
        c.create_polygon(94, 65, 106, 65, 100, 72, fill="#CB6682")
        c.create_arc(84, 65, 116, 87, start=180, extent=180, style=tk.ARC,
                     outline=INK, width=2)
        for y in (67, 77):
            c.create_line(30, y - 5, 68, y, fill=INK, width=2)
            c.create_line(132, y, 170, y - 5, fill=INK, width=2)

    def cancel_pending(self):
        if self.pending is not None:
            self.root.after_cancel(self.pending)
            self.pending = None

    def change_mode(self, mode):
        self.cancel_pending()
        self.mode = mode
        self.score = 0
        self.last_target = None
        self.used_words.clear()
        for name, button in self.mode_buttons.items():
            button.configure(bg=PURPLE if name == mode else "#E7E0F4",
                             fg="white" if name == mode else INK)
        self.update_stars()
        self.next_task()
        self.root.focus_set()

    def reset(self):
        self.change_mode(self.mode)

    def next_task(self):
        self.pending = None
        if self.score == 10:
            self.score = 0
            self.last_target = None
            self.used_words.clear()
            self.update_stars()
        choices = {"Litery": tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
                   "Cyferki": tuple("0123456789"), "Słowa": WORDS}[self.mode]
        if self.mode == "Słowa":
            choices = tuple(word for word in choices if word not in self.used_words)
        self.target = random.choice([item for item in choices if item != self.last_target])
        self.last_target = self.target
        if self.mode == "Słowa":
            self.used_words.add(self.target)
        self.position = 0
        self.waiting = False
        self.draw_cat()
        self.message.configure(text="Dasz radę!", fg=GREEN)
        self.update_task()

    def update_task(self):
        expected = self.target[self.position]
        if self.mode == "Słowa":
            self.instruction.configure(text=f'Napisz słowo. Teraz szukamy: {expected}')
            self.word_progress.configure(text=" ".join(self.target[:self.position]) or " ")
        else:
            self.instruction.configure(text="Znajdź taką literę:" if self.mode == "Litery"
                                       else "Znajdź taką cyferkę:")
            self.word_progress.configure(text=" ")
        self.target_label.configure(text=self.target)
        for character, label in self.key_labels.items():
            label.configure(bg="#FFE082" if character == expected else "#E7E0F4",
                            relief=tk.RAISED)

    def update_stars(self):
        filled = self.score % 10
        if self.score and not filled:
            filled = 10
        self.stars.configure(text="★" * filled + "☆" * (10 - filled)
                             + f"   Brawo: {self.score}")

    def on_key(self, event):
        # Pomijamy skróty, klawisze specjalne i automatyczne powtórki po sukcesie.
        if self.waiting or event.state & (0x4 | 0x8 | 0x20000):
            return
        character = event.char.upper()
        if len(character) != 1 or character not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
            return
        if character != self.target[self.position]:
            self.message.configure(text="Spróbuj podświetlonego klawisza.", fg=PURPLE)
            return
        self.position += 1
        if self.position < len(self.target):
            self.update_task()
            self.message.configure(text="Tak! Teraz następna literka.", fg=GREEN)
            return
        self.score += 1
        self.waiting = True
        self.draw_cat(happy=True)
        self.update_stars()
        if self.mode == "Słowa":
            self.word_progress.configure(text=" ".join(self.target))
        celebration = self.score % 10 == 0
        praise = (
            "10 sukcesów! Kotek jest z Ciebie dumny!"
            if celebration
            else random.choice(PRAISE)
        )

        if self.player_name:
            praise = f"{self.player_name}, {praise}"

        self.message.configure(text=praise, fg=GREEN)
        self.pending = self.root.after(2400 if celebration else 1200, self.next_task)

    def toggle_fullscreen(self, event=None):
        self.root.attributes("-fullscreen", not self.root.attributes("-fullscreen"))
        self.root.focus_set()
        return "break"

    def exit_fullscreen(self, event=None):
        self.root.attributes("-fullscreen", False)
        return "break"


def main():
    root = tk.Tk()
    root.withdraw()  # Hide the game window while asking.

    name = simpledialog.askstring(
        "Witaj!",
        "Podaj swoje imię:",
        parent=root,
    )
    player_name = (name or "").strip()

    KeyboardGame(root, player_name)
    root.deiconify()  # Show the game.
    root.mainloop()


if __name__ == "__main__":
    main()
