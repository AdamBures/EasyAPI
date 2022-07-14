# EasyAPI

EasyAPI je jednoduché API vytvořené za pomocí Django Rest Framework.

## Instalace

Použijeme PIP k nainstalování potřebných modulů ze souboru requirements.txt

```bash
pip install -r /path/to/requirements.txt
```

## Spuštění

Aplikaci spustíme za pomocí příkazu:

```bash
pip /path/to/manage.py runserver
```

Po přesměrování na http://127.0.0.1:8000/ uvidíme 404 Error a pod ním výpis možných cest v našem API.

### /import
Tato cesta nás odkáže na POST metodu díky které můžeme do našeho API přidávat další JSON obsah.

### /detail 
Tato cesta nám vypíše za pomocí GET metody celý obsah našeho API

### detail/<str:model>
Tato cesta nám vypíše všechen obsah spojený s daným modelem v našem JSON API
Například: 
```bash
http://127.0.0.1:8000/detail/AttributeValue
```
Vypíše:
```json
[
    {
        "AttributeValue": {
            "id": 1,
            "hodnota": "modrá"
        }
    },
    {
        "AttributeValue": {
            "id": 2,
            "hodnota": "zelená"
        }
    },
    {
        "AttributeValue": {
            "id": 3,
            "hodnota": "žlutá"
        }
    }]
```
### detail/<str:model>/<int:model_id>
Tato cesta nám vypíše všechen obsah spojený s modelem s daným indexem v našem JSON API
Například: 
```bash
http://127.0.0.1:8000/detail/AttributeValue/1
```
Vypíše:
```json
[
    {
        "AttributeValue": {
            "id": 1,
            "hodnota": "modrá"
        }
    }
]
```
## Licence 
[MIT](https://choosealicense.com/licenses/mit/)
