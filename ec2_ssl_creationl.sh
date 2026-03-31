##SSL Certificate (Let's Encrypt)
# Since you're enabling 443, you'll need a valid certificate. If you have a domain pointed at your EC2 IP, Certbot 
# makes this a one-command process:

sudo certbot --nginx -d yourdomain.com