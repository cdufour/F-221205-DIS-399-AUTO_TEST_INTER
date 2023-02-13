FROM python:3.10.5-alpine

WORKDIR /app

COPY app.py .

# définit la variable d'env SLEEP_DURATION et sa valeur par défault
# écrasable en option de ligne commande: docker run -e SLEEP_DURATION=10
ENV SLEEP_DURATION 120

# -u, unbuffered => les outputs du processus (print) ne sont pas mis en mémoire tampon
CMD ["python", "-u", "app.py"]


