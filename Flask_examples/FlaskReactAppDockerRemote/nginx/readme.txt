#when running this application on a server it requires the following nginx configuration as seen in this directory: frontend.conf
#It should go : /etc/nginx/nginx.conf
#how to start it:
#systemctl stop nginx
#systemctl start nginx
#nginx -t
#systemctl reload nginx

#Why is is required:
#when the code is executed without the froxy it will try and access it's localhost for the machine being run on which is not correct and will not work.

Here's why your Nginx configuration works despite using localhost while seemingly accessing it via the server's IP address (192.168.1.197):
The Key is Nginx's Role as a Reverse Proxy:

Nginx in this setup acts as a reverse proxy. Here's how the request flow works:
Client Request: A client (e.g., your web browser) sends a request to your server's IP address (192.168.1.197) on port 80.

Nginx Receives the Request: Nginx, listening on port 80 of the server with the server_name matching the requested IP, intercepts this request.
Nginx Determines the Location: Nginx examines the requested URL path.

If the path starts with /api/, the request matches the location /api/ block.
Otherwise, it matches the location / block.
Nginx Proxies the Request:

For /api/: Nginx forwards the request to http://localhost:5000. Because this localhost refers to the same server where Nginx is running, it successfully connects to the application listening on port 5000 on that server.
For /: Nginx forwards the request to http://localhost:3000. Similarly, this connects to the application on port 3000 on the same server.
Why server_name is Important (and not directly related to the proxy_pass to localhost):

The server_name 192.168.1.197; directive tells Nginx to handle requests that are specifically addressed to this IP address (or a domain name you might have configured to point to this IP). It's how Nginx knows which server block to use for an incoming request.

In summary:

The client connects to the server's IP address (192.168.1.197).
Nginx intercepts this request because its server_name matches.
Nginx then internally forwards the request to the appropriate application running on the same server using localhost (or 127.0.0.1).