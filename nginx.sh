sudo ln -s /etc/nginx/sites-available/stock_app /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx