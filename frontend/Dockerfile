
FROM node:lts-alpine

WORKDIR /usr/src/

# Install app dependencies
COPY ./package.json ./
COPY ./package-lock.json ./
RUN npm ci --only=production

# Link the source
ADD . /usr/src/

EXPOSE 3000
ENTRYPOINT [ "npm", "run", "dev" ]
