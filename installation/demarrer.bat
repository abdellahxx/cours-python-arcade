@echo off
chcp 65001 > nul
title Chasseur d'etoiles - demarrage
REM ==================================================
REM   Installe Python (si besoin) puis ouvre le jeu
REM   dans l'editeur IDLE. A placer dans le dossier du kit,
REM   a cote de python-installer.exe et de depart.py.
REM ==================================================

set "PYEXE="
for /d %%D in ("%LOCALAPPDATA%\Programs\Python\Python3*") do if exist "%%D\pythonw.exe" set "PYEXE=%%D\pythonw.exe"
if defined PYEXE goto lancer

echo.
echo   ==============================================
echo     Installation de Python en cours...
echo     Patiente 1 a 2 minutes, ne ferme pas cette fenetre.
echo   ==============================================
echo.
"%~dp0python-installer.exe" /quiet InstallAllUsers=0 PrependPath=1 Include_tcltk=1 Include_test=0 Include_launcher=0 Shortcuts=0

for /d %%D in ("%LOCALAPPDATA%\Programs\Python\Python3*") do if exist "%%D\pythonw.exe" set "PYEXE=%%D\pythonw.exe"
if not defined PYEXE (
    echo.
    echo   Oups ! Python ne s'est pas installe.
    echo   Leve la main pour appeler l'animateur.
    echo.
    pause
    exit /b 1
)

:lancer
echo   Python est pret ! Ouverture du jeu...
if exist "%~dp0depart.py" (
    start "" "%PYEXE%" -m idlelib "%~dp0depart.py"
) else (
    start "" "%PYEXE%" -m idlelib
)
