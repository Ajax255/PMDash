FROM node:current-alpine as build-stage

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

RUN npm run build

FROM nginx:stable-alpine as production-stage

COPY --from=build-stage /app/docker-nginx.conf /etc/nginx/con.d/default.conf
COPY --from=build-stage /app/dist /usr/share/nginx/html

EXPOSE 4040

CMD ["/bin/sh", "-c", "exec nginx -g 'daemon off;';"]

WORKDIR /usr/share/nginx/html