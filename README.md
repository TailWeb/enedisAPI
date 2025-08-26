# API ENEDIS - Serveur HTTPS

## Description
Ce serveur Flask permet de faire des requêtes à l'API d'ENEDIS en HTTPS.

## Configuration

### Certificats SSL
Les certificats SSL auto-signés ont été générés automatiquement :
- `cert.pem` : Certificat public
- `key.pem` : Clé privée

### Variables d'environnement
Vous pouvez définir vos clés API ENEDIS via les variables d'environnement :
```bash
set ENEDIS_PUBLIC_KEY=votre_cle_publique
set ENEDIS_SECRET_KEY=votre_cle_secrete
```

## Utilisation

### Démarrer le serveur
```bash
python app.py
```

Le serveur sera accessible sur :
- https://127.0.0.1:5000
- https://localhost:5000

### Endpoints disponibles

1. **POST /callback** - Endpoint pour recevoir les callbacks d'ENEDIS
2. **GET /get_data** - Endpoint pour faire une requête à l'API ENEDIS

### Avertissement SSL
Comme nous utilisons un certificat auto-signé, votre navigateur affichera un avertissement de sécurité. Pour continuer :

1. Cliquez sur "Avancé" ou "Advanced"
2. Cliquez sur "Continuer vers 127.0.0.1 (non sécurisé)" ou "Proceed to 127.0.0.1 (unsafe)"

Ceci est normal en développement local.

### Test avec curl
Pour tester sans avertissement SSL :
```bash
curl -k https://127.0.0.1:5000/get_data
```

## Notes importantes
- Ce serveur est configuré pour le développement local
- En production, utilisez des certificats SSL valides
- Les clés API sont actuellement codées en dur (à modifier selon vos besoins)