# phpMyAdminDetector

> **Avertissement légal** Utilisez ce script uniquement sur des cibles que vous possédez ou pour lesquelles vous avez une autorisation écrite. L’attaque non autorisée de systèmes informatiques est illégale.

---

## Présentation

Ce script Python réalise un scan des machines d'un réseau et cherche si l'une d'entre elles prend en charge le service phpMyAdmin :
il prend seulement en compte le nom par défaut du service pour l'instant et ne cherche pas de variante.

## Prérequis

| Outil / Librairie | Version conseillée |
| ----------------- | ------------------ |
| **Python**        | 3.8+               |
| **requests**      | >=2.31             |


Installation rapide:

```bash
python -m venv venv
source venv/bin/activate        # sous Windows : venv\Scripts\activate
pip install requests socket
```

(ou)

```bash
pip install -r requirements.txt
```


## Utilisation

```bash
python phpMyAdminDetector.py <domaine>/<masque>
```

Exemple:

```bash
python phpMyAdminDetector.py 192.168.1.0/24
```

## Author

**Corentin Mahieu** – [@Fir3n0x](https://github.com/Fir3n0x)
