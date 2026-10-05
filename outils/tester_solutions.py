# Outil animateur : lance chaque solution, simule des touches et des
# collisions, et signale toute erreur. Usage : python tester_solutions.py
import os, sys, types, subprocess

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.join(ICI, "..")

LANCEUR = r'''
import sys, types, turtle, traceback
sons = []
ws = types.ModuleType("winsound")
ws.SND_FILENAME, ws.SND_ASYNC = 1, 2
ws.PlaySound = lambda f, flags: sons.append(f)
sys.modules["winsound"] = ws
erreurs = []
def rapport(*a):
    erreurs.append("".join(traceback.format_exception(*a)))
import tkinter
tkinter.Tk.report_callback_exception = lambda self, *a: rapport(*a)

def scenario():
    g = sys._getframe(2).f_globals
    ecran = turtle.Screen()
    etapes = []
    def appel(nom):
        def f():
            if nom in g: g[nom]()
        return f
    for nom in ["recommencer", "aller_a_gauche", "aller_a_gauche", "aller_a_droite",
                "monter", "monter", "monter", "monter", "monter", "monter", "descendre",
                "tirer", "tirer", "tirer", "tirer"]:
        for i in range(25 if nom == "aller_a_gauche" else 1):
            etapes.append(appel(nom))
    def attraper():
        if "etoile" in g and "vaisseau" in g:
            g["etoile"].goto(g["vaisseau"].pos())
    def percuter():
        if "meteorites" in g:
            g["meteorites"][0].goto(g["vaisseau"].pos())
    def viser():
        if "lasers" in g and g["lasers"] and "meteorites" in g:
            g["meteorites"][1].goto(g["lasers"][0].pos())
    def dix_points():
        for _ in range(12):
            attraper(); ecran.ontimer(lambda: None, 1)
    etapes += [attraper, percuter, appel("tirer"), viser, attraper, percuter, percuter]
    def fin():
        try:
            s = g.get("score"); v = g.get("vies"); n = g.get("niveau"); j = g.get("en_jeu")
            print("ETAT score=%s vies=%s niveau=%s en_jeu=%s lasers=%s sons=%s" % (s, v, n, j, len(g.get("lasers", [])), sorted(set(sons))))
            if erreurs: print("ERREURS:\n" + "\n".join(erreurs))
            # 2e partie apres game over
        finally:
            turtle.bye()
    t = 300
    for e in etapes:
        ecran.ontimer(e, t); t += 60
    if "recommencer" in g:
        ecran.ontimer(appel("recommencer"), t + 400)
    ecran.ontimer(fin, t + 1500)

orig = turtle.TurtleScreen.mainloop
def faux_mainloop(self):
    scenario(); orig(self)
turtle.TurtleScreen.mainloop = faux_mainloop
def faux_done():
    g = sys._getframe(1).f_globals
    turtle.Screen().ontimer(turtle.bye, 1500); orig(turtle.Screen())
turtle.done = faux_done
import runpy
try:
    runpy.run_path(sys.argv[1], run_name="__main__")
except turtle.Terminator:
    pass
'''

ok = True
for dossier in sorted(os.listdir(RACINE)):
    if not dossier.startswith("seance-"):
        continue
    code = os.path.join(RACINE, dossier, "code")
    for fichier in ("bonjour.py", "carte_pilote_solution.py", "echauffement.py", "solution.py"):
        chemin = os.path.join(code, fichier)
        if not os.path.exists(chemin):
            continue
        reponses = "Lina\n11\nMars\nrouge\n"          # réponses aux input()
        r = subprocess.run([sys.executable, "-c", LANCEUR, chemin], input=reponses,
                           capture_output=True, text=True, timeout=60)
        sortie = (r.stdout + r.stderr).strip()
        probleme = r.returncode != 0 or "Traceback" in sortie or "ERREURS" in sortie
        ok = ok and not probleme
        print(("ECHEC " if probleme else "OK    ") + dossier + "/" + fichier + "  " + sortie.replace("\n", "\n      "))
print("\nTOUT EST BON" if ok else "\nIL Y A DES PROBLEMES")
