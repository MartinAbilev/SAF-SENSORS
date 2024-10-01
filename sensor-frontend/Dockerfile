# Dockerfile for Vue.js
FROM node:16

WORKDIR /app

COPY package.json .
RUN npm install -g @vue/cli
RUN npm install

COPY . .

RUN npm run build

CMD ["npm", "run", "serve"]
