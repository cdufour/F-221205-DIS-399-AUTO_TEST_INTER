FROM node:14.15.5-alpine

WORKDIR /app

# installation des dépendances
COPY package.json .

# création et alimentation d'un dossier node_modules contenant les dépendances
RUN npm install

COPY server.js .

CMD ["node", "server.js"]