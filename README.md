# EventPass

EventPass — Plateforme de promotion d’événements avec billetterie numérique

EventPass est une application web développée avec Django permettant de publier des événements, gérer les réservations de billets et générer automatiquement un QR code après paiement.
Le projet est conçu comme une base solide pour une solution de billetterie numérique simple et extensible.

## Fonctionnalités

👤 Inscription & connexion des utilisateurs
🧑‍💼 Rôle Organisateur avec permissions spécifiques
📅 Création et gestion d’événements
📋 Liste et détail des événements
🎟️ Réservation de billets
💳 Simulation de paiement
🔐 Accès restreint au tableau de bord organisateur
📊 Tableau de bord avec :
   -nombre de billets vendus
   -revenus générés
🔳 Génération automatique d’un QR code par billet payé
🖼️ Upload d’image d’événement
🎨 Interface Bootstrap + fond animé canvas


Rôles utilisateurs
   - Utilisateur simple
   - Voir les événements
   - Réserver des billets
   - Payer (simulation)
   - Organisateur
   - Créer des événements
   - Accéder au tableau de bord
   - Voir ventes & revenus
Le rôle organisateur est géré via le champ is_organizer du modèle User.

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

- [ ] PDF billet téléchargeable
- [ ] Paiement réel
- [ ] Recherche & filtres événements
- [ ] Statistiques avancées

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

2. **Créer un environnement virtuel**
   python -m venv venv
   source venv/bin/activate      # Linux/macOS
   venv\Scripts\activate         # Windows

3. **Installer les dépendances**
   pip install django qrcode pillow

4. **Migrations**
   python manage.py makemigrations
   python manage.py migrate
   
5. **Créer un superuser**
   python manage.py createsuperuser

6. **Lancer le serveur**
   python manage.py runserver
   Puis ouvrir :
   http://127.0.0.1:8000/
