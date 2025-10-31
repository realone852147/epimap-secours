# Politique de confidentialité — Epita-Map

**Dernière mise à jour :** 2025-10-31

## 1. Présentation générale
Epita-Map est un outil open-source conçu pour aider les étudiants à retrouver facilement les salles et bâtiments du campus.  
Le service ne collecte **aucune donnée personnelle**, ne stocke **aucune information utilisateur** et ne réalise **aucune géolocalisation**.

## 2. Données traitées
- **Aucune géolocalisation automatique** : le site n’accède jamais à la position des utilisateurs.
- **Aucun compte / cookie de suivi** : Epita-Map ne requiert aucune inscription et n’utilise pas de cookies tiers.
- **Aucun stockage de logs sensibles** :  
  - L’infrastructure est hébergée derrière **Cloudflare**, qui agit comme reverse proxy.  
  - Les adresses IP réelles des visiteurs ne sont **pas visibles** par le serveur applicatif.  
  - Le serveur ne conserve donc **aucune donnée personnelle identifiable** dans ses journaux.  
  - Les logs techniques (erreurs, requêtes internes) sont éphémères et ne contiennent aucune donnée d’utilisateur.

## 3. Hébergement et sécurité
- Tout le trafic passe par **Cloudflare**, qui assure la protection contre les attaques (DDoS, abus, etc.) et le chiffrement HTTPS.  
- Le serveur applicatif ne dispose d’aucun accès direct aux données réseau des visiteurs.  
- Aucune base de données n’est utilisée, et le site est purement statique côté utilisateur.

## 4. Durée de conservation
Aucune donnée n’est conservée. Les logs techniques éventuels sont temporaires et ne contiennent aucune information personnelle.

## 5. Contact
Pour toute question concernant la confidentialité ou la conformité RGPD :  
📧 **contact@epita-map.fr**

---

**Remarques légales :**
- L’absence de stockage d’adresses IP, de géolocalisation et de cookies de suivi place Epita-Map hors du champ d’application du RGPD (aucun traitement de données personnelles).  
- Le service peut être validé pour un usage interne ou public selon les directives de la DSI, sous réserve de conformité au plan Vigipirate.
