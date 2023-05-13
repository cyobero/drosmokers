FROM nginx:latest

# Copy custom configuration file
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Install nano editor
RUN apt-get update && apt-get install -y nano

# Expose port 80
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]
