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


## État Actuel du Projet
Le projet est officiellement déployé et fonctionnel.
- **Hébergement :** PythonAnywhere
- **Base de données :** SQLite (en transition vers PostgreSQL pour la production)
- **Authentification :** Système complet (Inscription, Connexion, Déconnexion)

---

## Roadmap & Évolutions Futures

Voici les prochaines étapes de développement prévues pour transformer ce projet étudiant en une solution de billetterie complète :

### 1. Sécurité et Performance (Priorité Haute)
- [ ] **Gestion des Secrets :** Migrer la `SECRET_KEY` et les accès DB vers des variables d'environnement (`python-dotenv`).
- [ ] **Optimisation Media :** Configurer un stockage externe (Cloudinary ou AWS S3) pour les QR Codes afin de garantir leur persistance.
- [ ] **Sécurisation SSL :** Forcer le HTTPS sur toutes les pages.

### 2. Nouvelles Fonctionnalités Utilisateurs
- [ ] **Profil Utilisateur :** Ajout d'un tableau de bord personnel pour voir l'historique des billets achetés.
- [ ] **Envoi de Billets par Email :** Intégration de SMTP pour envoyer le QR code directement par mail après inscription à un événement.
- [ ] **Validation sur place :** Création d'une vue "Scanner" pour permettre aux organisateurs de valider les billets via un smartphone.

### 3. Monétisation (Évolutif)
- [ ] **Paiement Stripe :** Intégration de l'API Stripe pour gérer la vente de billets payants.
- [ ] **Gestion des remises :** Système de codes promos pour les organisateurs.

---



## Auteur
Darius BOULANGA

LinkedIn : Darius BOULANGA

GitHub : @Darius-BOUL

Pour faire tourner ce projet sur votre machine, suivez ces étapes :

1. **Cloner le dépôt** :
   ```bash
   git clone [https://github.com/Darius-BOUL/eventpass.git](https://github.com/Darius-BOUL/eventpass.git)
   cd eventpass
