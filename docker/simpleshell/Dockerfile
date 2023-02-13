FROM debian:11-slim

WORKDIR /app

# copie le fichier app.sh dans le workir "/app"
COPY app.sh .

# ajoute l'exécutabilité au fichier app.sh
RUN chmod +x app.sh

# commande démarrage
CMD ["/bin/bash", "app.sh"]