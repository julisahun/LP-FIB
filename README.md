# PracticaLP

*La practica consisteix en la creació d'un llenguatge musical anomenat JSBash, capaç de realitzar operacions esperables d'un llenguatge de programacio estandard i, a demes de reproduïr musica.*


### Operacions basiques:

JSBash implementa operacions de suma, resta, divisio i multiplicaio entre enters.
També implementa estructures condicionals de forma de `if` i `else` o de `while`

### Input Output

La lectura i escriputra de JSBash es realitza amb els operadors seguents:
- `<?>` per llegir del terminal
- `<!>` per escriure per terminal
- `<:> `per generar els fitxer musicals

### Funcions:

JSBash, admet la creació de metodes, per executar un metode en concret, es pot especificar com a parametre d'execusió, en cas de no especificar-se, s'executara el metode anomenat "Main".

```C++
Print |:
    x <- 2
    <!> x
:|
```

Exemple de codi d'una funcio que escriu per consola el numero 2 desde una variable *x*


### Variables:

En JSBash, l'assignació de variables es realitza amb l'operador "<-" que assigna a la variable de l'esquerra el valor de la dreta.


### Llistes:

JSBash implementa les llistes com a tipus de variable. Per assignar una llista s'han d'usar les claus *"{ }"* i els valors de la llista seperats per blancs a l'interior, que tant poden ser, valors numerics, variables, notes o acords. Les variables dins d'una llista són una referencia a elles, i no pas el seu valor.

##### Metodes de Llistes
sigui *list* una variable de tipus llista:
- tamany de la llista -> `#list`
- elemnt i-esim de la llista ->  `list[i]` on el primer element es el 1
- afegir element a la llista -> `list << x` on *x* s'afegeix al final de la llista
- treure element i-esim de la llista -> `list 8< i` on el primer element es el 1
- treure element i de la llista `llist ><((> i` on s'elimina la primera aparicio de l'element i de la llista


### Notes:

Les notes en JSBash estan compostes per 3 camps: (duracio, to, octava)

- La **duracio** especifica el tipus de la nota segons el seguent:

|  duracio  | significat  |
| ------------ | ------------ |
|  1 | rodona  |
| 2 |  blanca |
| 4 |  negre |
|  8 |  corxera |
| 16 | semicorxera



- el **to** especifica el to de la nota. El to conte el to de la nota en sistema america A -> LA ... G -> SOL i si te alguna alteració # -> sustingut (JSBash no implementa els bemolls, ja que es una versio simple i els bemolles es poden susbtituir per sustinguts)

- la **octava** especifica la octava on es troba la nota segons un teclat de piano

> els camps de duracio i octava son OPCIONALS, si no s'especifiquen, s'asumeix un 4 (negre en la octava central)

```
Main |:
    l <- { 8E 8A 8G 8D5 }
    <:> l
:|
```

Exemple de codi que generaria la seguent partitura:
![](https://image.spreadshirtmedia.net/image-server/v1/mp/compositions/T993A1MPA2181PT1X42Y48D6094478FS7259Cx000000/views/1,width=200,height=200,appearanceId=1,backgroundColor=FFFFFF,noPt=true/pentagrama-con-las-notas-alfombrilla-de-raton.jpg)


### Acords:

Els acords en JSBash poden ser de dos tipus: Modals i explicits.
- Els acords **modals** es representen per el to (C,A,G#...) i la modalitat M o m per Major o menor, els acords augmentat, disminuits, etc, es deixen per la seguent versió.

- Els acord **explicits** es representen per les notes del acord que es vol formar, per exemple C4 E4 G4 representa un acord de DO major de forma explicita.

Els acords han d'anar acompanyats de < > per obrir i tancar. En els acords explicits, la duracio del mateix serà la duracio de la primera nota, o 4 si no s'especifica


> Exemple d'acord de DO major:

- Explicita:


    Main |:
        l <- { <1C E G> }
        <:> l
    :|
- Modal 


    Main |:
        l <- { <1CM> }
        <:> l
    :|


[![DO major](https://jadebultitude.b-cdn.net/wp-content/uploads/2021/01/Screenshot-2021-01-31-at-20.44.41.jpg "DO major")](http://https://jadebultitude.b-cdn.net/wp-content/uploads/2021/01/Screenshot-2021-01-31-at-20.44.41.jpg "DO major")
