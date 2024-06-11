# Build stage
FROM node:16-alpine AS build

# Set the working directory
WORKDIR /app

# Copy the package.json and package-lock.json
COPY package*.json ./

# Install dependencies using npm
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the React app
RUN npm run build

# Serve stage
FROM nginx:alpine

# Copy the built files from the previous stage to the nginx html directory
COPY --from=build /app/build /usr/share/nginx/html

# Expose the port that the application runs on
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]

# cd project/frontend
# Docker 이미지를 빌드합니다. (이미지명 toyproject-web로 지정)
# docker build -t toyproject-web .
# 컨테이너를 실행합니다.
# docker run -p 3000:80 toyproject-web