# Laboration 4: Del 2

**Uppgifterna i Del 2 är övningar i att bryta ut data och funktioner och att
strukturera kod**. Ni ska omstrukturera koden för ett textbaserat äventyrsspel
så att det enkelt går att utöka/göra om det.


## Förberedelser

Filen till uppgiften finns i katalogen
`{{< coursedir >}}/kursmaterial/laboration4/del2`. Kopiera `adventure.py` från
katalogen till en egen katalog.

- **Fil att ladda ner i distansläge**: [`adventure.py`](adventure.py)

Läs igenom och testkör filen `del2/adventure.py` så att ni förstår vad som
händer i filen. För att utföra uppgifterna behöver ni framförallt förstå koden i
termer av

- *Hur används de globala konstanterna `DESCRIPTIONS` och `OPTIONS`*
- *Hur sker flödet av output och input som styr spelet*


## Uppgift 1

I uppgift 1 ska ni **strukturera den existerande koden** i `del2/adventure.py`
enligt stegen längre ner. Använd endast globala variabler för konstanter.


### Steg 1: Utöka/Ändra spelet

Utöka koden med fler `if`-satser så att användaren får ett val då hen försöker
smita förbi vakten (`"Sneak"`) att antingen gå till höger eller vänster om
vakten. I ett av fallen lyckas man och i ett av fallen misslyckas man.

Tänk på att ändra på alla ställen i `if`-satsen där `"Sneak"` förekommer.

**Testa adventure.py för att försäkra dig om att det fungerar.**

{% next %}


### Steg 2: Använd en main-funktion

Strukturera om `adventure.py` så att så gott som all kod efter funktionerna för
utskrift av figurer ligger i en ny funktion med namnet `main()`. Glöm inte bort
att anropa `main()` i slutet av filen.

**Testa adventure.py för att försäkra dig om att det fungerar.**

{% next %}


### Steg 3: Bryta ut data och funktioner i moduler

Lägg alla funktioner som skriver ut bilder i en egen fil `pictures.py` och
importera den sedan som en modul. Tänk på att ev uppdatera anrop av dessa
funktioner i `adventure.py` med rätt namnrymd/namespace (beroende på hur du gör
importen).

Lägg all data, dvs `DESCRIPTIONS` och `OPTIONS`, i en egen fil `gamedata.py` och
importera den sedan som en modul. Tänk på att ev uppdatera referenser till dessa
datastrukturer i `adventure.py` med rätt namnrymd/namespace (beroende på hur du
gör importen).

**Testa adventure.py för att försäkra dig om att det fungerar.**

{% next %}


### Steg 4: Skapa ny datastruktur för strukturen på äventyret, ADVENTURE_TREE

För att frigöra själva spelflödet från data vill vi skapa en ny datastruktur som
beskriver äventyret i som en graf av tillstånd. Denna ska koppla samman ett
tillstånd i `DESCRIPTIONS`, t ex `"Start"`, med de två valmöjligheterna i
`OPTIONS`, t ex `"Red"` och `"Blue"`.

De tillstånd som leder till att äventyret tar slut låter vi leda till
tillståndet `"End"` som får representera att spelet är slut (*Game over*) oavsett
om slutet var bra eller dåligt.

Vi representerar detta i ett dictionary som

```
{state_1: [option1, option2],
 ...,
 state_n : []}

t ex

{"Start": ["Blue", "Red"],
 ...,
 "Attack": ["End"]}
```

Gå igenom `if`-satsen och skapa en global variabel `ADVENTURE_TREE`
som ett dictionary i filen `gamedata.py` som innehåller tillstånden enligt
strukturen ovan.

Här är en bild på en del av grafen för äventyret:

![](images/partial_adventure_tree.png)

**Testa adventure.py för att försäkra dig om att det fungerar.**

Att modellera ett problem genom att se det som att det är ett system som kan
befinna sig i ett antal tillstånd och växla mellan dessa tillstånd är vanligt
inom datavetenskap och visualiseras ofta med tillståndsdiagram. Du kan läsa mer
på t.ex. Wikipedia.

- [Finite state machine](https://en.wikipedia.org/wiki/Finite-state_machine)
- [State diagram](https://en.wikipedia.org/wiki/State_diagram)

{% next %}


### Steg 5: Använd ny datastruktur `ADVENTURE_TREE`

Nu är det dags att använda `ADVENTURE_TREE` i `adventure.py`. Vår nya datastruktur
`ADVENTURE_TREE` beskriver vilka tillstånd som finns och hur dessa kan nås.
Tanken med Steg 5 är lägga till kod som explicit håller koll på vilket tillstånd
vi befinner oss i. I Steg 6 kommer vi sedan försöka korta ner koden vi
får efter Steg 5.

I `main()` under den första print-satsen lägg till:

```python
# Vi börjar äventyret i tillståndet "Start"
current_state = "Start"

# Ta fram list över möjliga nästa tillstånd givet nuvarande tillstånd från
# ADVENTURE_TREE
succ_states = ADVENTURE_TREE[current_state]
```

Uppdatera koden så att den i varje villkorsgren ändrar på `current_state` och
`succ_states`. Samt använder `succ_states` för att ta fram alternativen som
presenteras för användaren. Ändra också tilldelnigen av `text_box` så att den
använder `current_state` och `options` istället för text-strängar i
`.format()`-anropet. Första villkoret bör blir något i stil med:

{% spoiler %}
```python
if inp == "1":
    # nästa tillstånd är det första tillståndet i succ_states
    current_state = succ_states[int(inp)-1]
    # uppdatera succ_states baserat på det nya current_state
    succ_states = ADVENTURE_TREE[current_state]
    text_box = "{}\n{}  {}\n{}  {}".format(DESCRIPTIONS[current_state],
                                           "1", OPTIONS[succ_states[0]],
                                           "2", OPTIONS[succ_states[1]])
    print(text_box)
    inp = input(">> ")
```
{% endspoiler %}

Gör dessa ändring genomgående i alla `if`-satser, där `current_state` uppdateras
utifrån `inp`.

**Testa adventure.py för att försäkra dig om att det fungerar.**

{% next %}


### Steg 6: Funktion för att byta tillstånd

Ni har säkert sett att nu när vi har en tillståndsmodell för äventyret, så
framträder ett tydligt mönster för hur programmet egentligen bara tranporterar
oss mellan olika tillstånd, och att det som görs i ett tillstånd i stort sätt
är samma sak varje gång.


#### get_next_state

Vi ska i Steg 6 skriva koden för detta mönster som funktionen
`get_next_state(state)` som får in ett tillstånd som sträng och ska returnera
nästa tillstånd. Om det finns flera alternativ för vilket som ska bli nästa
tillstånd ska användaren tillfrågas.

Om ni tittar på `ADVENTURE_TREE` så ser ni att vi måste hantera två fall:

{% spoiler %}
1. om det endast finns ett möjligt nästa tillstånd (t.ex. `"Attack" -> "End"`),
   *returnera det enda möjliga tillståndet direkt*
2. om det finns flera alternativ, presentera dessa för användaren och *returnera
   det alternativ som användaren valt*. Använd `gamedata.OPTIONS` för att
   beskriva alternativen för användaren. 
{% endspoiler %}

Strukturen för `get_next_state(state)` kan se ut så här:

{% spoilerbox %}
- Hämta möjliga nästa tillstånd för `state` från `ADVENTURE_TREE`
- Om det bara finns ett möjligt nästa tillstånd, returnera detta.
- Om det finns fler, presentera dessa för användaren, fråga efter ett val
  och returnera det tillstånd som användaren valt.
{% endspoiler %}

**Vi har inte integrerat denna funktion i själva skriptet så att den anropas
från `main()`, men du kan testa (och ev. felsöka funktionen) genom att testa den
i det interaktiva läget.**

Kommentera anropet till `main()` så att det inte körs när du bara vill testa. Om
du lagt anropet till `main()` "bakom" en `if __name__ == "__main__"` kan du
alternativt starta python-tolken utan att ange fil och sedan importera
`adventure` (se nedan)

```
$ python3
>>> from adventure import
>>> get_next_state("Start")
1 Blue
2 Red
>> 1
'Blue'
>>>
```

Ovan svarar jag `1` när funktionen ber mig välja mellan de två alternativen och
så ser vi att funktionen returnerar `'Blue'`. Detta är lite tydligare om man
använder `ipython3` istället:

```
$ ipython3
In [1]: from adventure import *

In [2]: get_next_state("Start")
1 Blue
2 Red
>> 1
Out[2]: 'Blue'

In [3]:
```


#### Koppla ihop tillstånd med bild

Vi behöver också koppla bilderna till de olika tillstånden. Gör detta genom att
skriva funktionen `print_pic(state)` som får in ett tillstånd och sedan anropar
rätt utskriftsfunktion. T.ex. om `state` är `"Start"` ska `print_doors()`
anropas. Lägg `print_pic()` i `pictures.py`. Se också till att om `state` är
`"End"` så ska `print_game_over()` anropas.

Vi kommer använda `print_pic()` i Steg 7 när vi kopplar ihop allt. 

**Vi kan även testa `print_pic()` på samma sätt som vi testade
`get_next_state()`.**

```
$ ipython3
In [1]: from adventure import *

In [2]: print_pic("End")

   _____          __  __ ______    ______      ________ _____
  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \
 | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |
 | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  /
 | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \
  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\


In [3]: print_pic("Red")

            |                     |
         \     /               \     /
        -= .'> =-             -= <'. =-
           '.'.                 .'.'
             '.'.             .'.'
               '.'.----^----.'.'
                /'==========='\
            .  /  .-.     .-.  \  .
            :'.\ '.O.') ('.O.' /.':
            '. |               | .'
              '|      / \      |'
               \     (o'o)     /
               |\             /|
               \('._________.')/
                '. \/|_|_|\/ .'
                 /'._______.'\ lc


In [4]:
```

{% next %}


### Steg 7: En ny main-funktion

Döp om er `main()`-funktion till `main_old()`. Vi behåller den för tillfället
så att vi kan titta på den, eller köra den för komma ihåg vad det var som hände
i spelet. 

Vi ska nu skriva en ny `main()`-funktion som använder `get_next_state()`. Vi
låter den börja med att fråga efter användarens namn och sätta nuvarande
tillstånd till `"Start"`:

```python
def main():
    name = input("What's your name?\n>> ")
    print("Welcome {} to the adventure of your life. Try to survive and find \
    the treasure!".format(name.upper()))
    
    current_state = "Start"
```

Lägg sedan till en loop som fortsätter så länge som `current_state` inte är
`"End"`. I loopen behöver du lägga till kod som tar hand om visning av bild och
beskrivning baserat på nuvarande tillstånd och till sist anropar
`get_next_state()` för att uppdatera `current_state`.

Se till att "gameover"-bilden visas när spelet är slut.

**Testa adventure.py för att försäkra dig om att det fungerar.**

{% next %}


### Steg 8 Städa ev upp kod

Se till att koden i skriptet är prydligt disponerad, dvs att ordningen importer,
funktioner, övrig kod följs.

{% next %}


### Steg 9 Utöka/Ändra spelet

Ändra/Utöka koden så att användaren får ett val då hen pratar med vakten
("Talk"), ett med positiv utgång och ett med negativ utgång.

Tänk på att ni behöver lägga till/ändra information i alla datastrukturer:
`ADVENTURE_TREE`, `DESCRIPTIONS` och `OPTIONS`

Jämför hur lätt/svårt det är att göra denna ändring jämfört med det första
steget i denna uppgift.

{% next %}


## Uppgift 2 (frivillig)

Nu bör koden i `adventure.py` vara frikopplad från själva dialogen och figurer
som skrivs ut.

Bygg ett nytt spel genom att skapa ny(a) fil(er). Ni kan t.ex. döpa dem till
`gamedata2.py` och `pictures2.py`). Dela gärna med er av dessa filer med
andra som läser kursen och provkör andra kursdeltagares spel.


## Uppgift 3: Ytterligare möjliga förbättringar (frivilliga)

- Förbättra `get_next_state()` så att den kan hantera godtyckligt många
  alternativ, dvs så att man i `ADVENTURE_TREE` kan ha tillstånd med t.ex. tre
  eller fyra alternativ.
- Lägg till ett tillstånd `"Win"` (och byt ev. ut `"End"` mot `"Lose"`) så att
  det går att skilja på slut där man vinner på något sätt och slut där man
  förlorar på något sätt.
- Förbättra datastrukturen för äventyret så att allt ryms i ett
  dictionary.
- Spara data för äventyret i en JSON-fil och gör så man kan anropa spelet
  med namn på äventyrsfil som ska läsas in och köras.
- Spara textgrafiken till filer och lägg till information i speldatastrukturen
  om vilka bilder som ska visas när.
