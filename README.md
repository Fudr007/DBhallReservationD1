# DBhallReservationD1

Systém pro správu a rezervaci sálů s vrstvenou architekturou a integrací databáze.

## Základní informace
Aplikace slouží k evidenci zákazníků, sportovních hal a správě jejich rezervací včetně doplňkových služeb. Je postavena na principech objektově orientovaného návrhu databáze s využitím architektonických vzorů **Table Gateway**.

### Klíčové funkcionality
* **Správa rezervací**: Vytváření nových rezervací s automatickým výpočtem ceny.
* **Evidence hal a služeb**: Správa dostupných prostor a doplňkových služeb přes M:N vazby.
* **Evidence zákaníků**: Správa zákazníků a jejich účtů
* **Import dat**: Modul pro hromadný import dat zákazníků, hal a služeb.
* **Validace**: Kontrola dostupnosti hal a validace vstupních dat před zápisem do DB.

---

## Konfigurace, Instalace a spuštění
### Konfigurace
Aplikace se dá konfigurovat pomocí ini konfiguračního souboru. Do něj se ukládají údaje pro připojení k databázi a cesty k důležitým souborům, které databáze používá.
#### Struktura souboru 
Soubor je rozdělen do dvou částí, tou první je sekce pro připojení pojmenovaná “database“. V té je jsou potřebné informace pro připojení k databázi.
* user = označuje username uživatele, na kterého chcete, aby se aplikace připojila
* password = doplňte heslo pro daného uživatele
* host = označuje ip adresu kde se nachází Oracle XE server databáze
* port = je označení portu, na kterém server běží
* service = typ Oracle databázového serveru
* encoding = jak je zakódování SQL příkazů

Druhou částí jsou cesty k důležitým souborům, které jsou potřebné pro běh databáze. Tato část je pojmenovaná “path“.

### Instalace a spuštění
Aplikaci lze nainstalovat a následně spustit dvěma způsoby přes GitHub na tomto odkaze: https://github.com/Fudr007/DBhallReservationD1, přes Releases a přes naklonování/stažení source kódu.
#### Releases
První způsob před Releases na GitHub stránce tohoto projektu.
Postup:
* Na GitHub stránce tohoto projektu klikněte na nejnovější release tohoto projektu, označený Latest.
*	Zde klikněte na HallReservationDB.zip a tím tento zip soubor stáhněte.
*	Po stažení rozbalte tento soubor do zvoleného místa na disku.
*	Po otevření složky s rozbaleným zip souborem uvidíte exe soubor pro spuštění aplikace a konfigurační ini soubor pro konfiguraci
*	Nejprve nakonfigurujte konfigurační soubor podle kapitoly 7.1
*	Poté stačí spustit main.exe soubor, pokud se vše provede správně tak by se aplikace měla spustit a zobrazit výchozí menu, pokud ne aplikace by měla sdělit co se stalo špatně
#### Klonování/Stažení source kódu
Druhým způsobem, jak tento projekt stáhnout a následně spustit je přes naklonování nebo stažení source kódu
Postup:
*	Na GitHub stránce tohoto projektu klikněte na zelené tlačítko Code.
*	Dále stiskněte Download ZIP tím stáhnete zip soubor se source kódem.
*	Rozbalte zip soubor do vámi vybraného místa na disku.
*	Poté otevřete rozbalenou složku ve vašem oblíbeném IDE
*	Nakonfigurujte konfigurační soubor config.ini podle kapitoly 7.1
*	Dále doinstalujte knihovnu pro práci s Oracle databází přes příkazovou řádku, spusťte toto: pip install cx_Oracle
*	Vyberte Python interpreter, ideálně Python 3.13 nebo kompatibilní
*	Následně stačí spustit kód v souboru main.py, pokud se vše provede správně tak by se aplikace měla spustit a zobrazit výchozí menu, pokud ne aplikace by měla sdělit co se stalo špatně
