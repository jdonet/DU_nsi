from tkinter import *

#https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/234859-creez-des-interfaces-graphiques-avec-tkinter

class Interface(Frame):
    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""

    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        self.pack(fill=BOTH)
        self.nb_clic = 0

        # Création de nos widgets
        self.message = Label(self, text="Vous n'avez pas cliqué sur le bouton.")
        self.message.pack()

        var_choix = StringVar()

        choix_rouge = Radiobutton(fenetre, text="Rouge", variable=var_choix, value="rouge")
        choix_vert = Radiobutton(fenetre, text="Vert", variable=var_choix, value="vert")
        choix_bleu = Radiobutton(fenetre, text="Bleu", variable=var_choix, value="bleu")

        choix_rouge.pack()
        choix_vert.pack()
        choix_bleu.pack()

        liste = Listbox(fenetre)
        liste.pack()

        liste.insert(END, "Pierre")
        liste.insert(END, "Feuille")
        liste.insert(END, "Ciseau")



        self.bouton_quitter = Button(self, text="Quitter", command=self.quit)
        self.bouton_quitter.pack(side="left")

        self.bouton_cliquer = Button(self, text="Cliquez ici", fg="red",
                                     command=self.cliquer)
        self.bouton_cliquer.pack(side="right")

    def cliquer(self):
        """Il y a eu un clic sur le bouton.
        On change la valeur du label message."""
        self.nb_clic += 1
        self.message["text"] = "Vous avez cliqué {} fois.".format(self.nb_clic)