README.txt > uppfært 04.09.09
Leiðbeiningar

1. Til þess að geta keyrt client forritin þarf að setja PYTHONPATH á src möppuna í verkefninu, 
    ath skipta þarf "Directory" í möppunna sem verkefnið er geymt í
    
    Windows:
        set PYTHONPATH=%PYTHONPATH%;C:\Directory\src
    Linux:
        export PYTHONPATH=/home/user/Directory/src:$PATH

2. Forrit keyrt í skel:
    Til þess að keyra forritið í skel þarf fara í client möppu frá src möppu og skrifa : python console.py

3. Forrit keyrt í gluggaumhverfi
    Nauðsynlegt er að setja upp wxPython til þess að geta keyrt gluggakerfisútgáfuna, 
    hana er hægt að sækja hér: http://www.wxpython.org/download.php#binaries.
    Til þess að keyra forritið í gluggaumhverfi þarf að fara í client möppu frá src möppu og skrifa: pyton gui.py
    
4. Til þess að sjá secret code:
    Ef línur 77 og 78 í mastermind.py eru uncommentaðar er hægt að sjá lausnarliti eða secret code
