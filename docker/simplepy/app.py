import time
import os

# durée de sommeil par défaut (en secondes)
duration = 5

# prise en compte d'une éventuelle variable d'environnement
if "SLEEP_DURATION" in os.environ:
    duration = int(os.environ["SLEEP_DURATION"])

while True:
    print("Simple app Python en boucle infinie...")
    time.sleep(duration)