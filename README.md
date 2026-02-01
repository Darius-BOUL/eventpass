# EventPass

**EventPass** est une application Django complète de gestion d'événements et de billetterie.
Elle permet aux utilisateurs de découvrir des événements, de réserver des places et de générer automatiquement des billets sécurisés avec QR codes après un paiement simulé.

## Fonctionnalités

- **Authentification complète** : Inscription et connexion pour les utilisateurs et les organisateurs.
- **Gestion des Événements** : Création, modification et affichage des événements avec détails (prix, date, lieu).
- **Système de Réservation** : Sélection de la quantité et calcul automatique du prix total.
- **Paiement Simulé** : Flux complet allant de la réservation à la confirmation de paiement.
- **Billetterie Automatisée** : Génération d'un QR code unique pour chaque ticket acheté (via la bibliothèque `qrcode`).
- **Interface Moderne** : Design responsive avec Bootstrap 5 et arrière-plan animé en Canvas JS.

## Technologies utilisées

- **Backend** : Django 6.0 (Python)
- **Base de données** : SQLite (par défaut)
- **Traitement d'images** : Pillow & QRcode
- **Frontend** : HTML5, CSS3, JavaScript, Bootstrap 5
- **Outils** : Environnement virtuel Python (`.venv`)

## Auteur
Darius BOULANGA

LinkedIn : Darius BOULANGA

GitHub : @Darius-BOUL

Pour faire tourner ce projet sur votre machine, suivez ces étapes :

1. **Cloner le dépôt** :
   ```bash
   git clone [https://github.com/Darius-BOUL/eventpass.git](https://github.com/Darius-BOUL/eventpass.git)
   cd eventpass
