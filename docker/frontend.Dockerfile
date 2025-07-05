# Build frontend docker file
FROM node:18-alpine

# set working directory
WORKDIR /app

# copy project files
COPY frontend/package.json frontend/package-lock.json /app/

# install dependencies
RUN npm install

# copy source code
COPY frontend /app/

# set port
EXPOSE 5000

# run the application
CMD ["npm", "start"]
