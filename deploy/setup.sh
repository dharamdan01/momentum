#!/bin/bash
# MOMentum — AWS EC2/Lightsail deployment script
# Run on a fresh Ubuntu 22.04+ instance:
#   curl -sSL https://raw.githubusercontent.com/gitswagata1/momentum/main/deploy/setup.sh | bash

set -e

echo "========================================"
echo "  MOMentum — Server Setup"
echo "========================================"

# System updates
echo "[1/7] Updating system..."
sudo apt-get update -y
sudo apt-get upgrade -y

# Install dependencies
echo "[2/7] Installing Python, Nginx, Git..."
sudo apt-get install -y python3.12 python3.12-venv python3-pip nginx git curl

# Clone repo
echo "[3/7] Cloning MOMentum..."
cd /home/ubuntu
if [ -d "momentum" ]; then
    cd momentum && git pull origin main
else
    git clone https://github.com/gitswagata1/momentum.git
    cd momentum
fi

# Python environment
echo "[4/7] Setting up Python environment..."
python3.12 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install gunicorn

# Environment file
echo "[5/7] Setting up environment..."
if [ ! -f .env ]; then
    cp .env.example .env
    echo ""
    echo "  *** IMPORTANT: Edit /home/ubuntu/momentum/.env with your API keys ***"
    echo ""
fi

# Nginx
echo "[6/7] Configuring Nginx..."
sudo cp deploy/nginx.conf /etc/nginx/sites-available/momentum
sudo ln -sf /etc/nginx/sites-available/momentum /etc/nginx/sites-enabled/momentum
sudo rm -f /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl restart nginx
sudo systemctl enable nginx

# Systemd service
echo "[7/7] Setting up MOMentum service..."
sudo cp deploy/momentum.service /etc/systemd/system/momentum.service
sudo systemctl daemon-reload
sudo systemctl enable momentum
sudo systemctl start momentum

echo ""
echo "========================================"
echo "  MOMentum is deployed!"
echo "========================================"
echo ""
echo "  URL: http://$(curl -s ifconfig.me)"
echo ""
echo "  Commands:"
echo "    sudo systemctl status momentum    # check status"
echo "    sudo systemctl restart momentum   # restart"
echo "    sudo journalctl -u momentum -f    # view logs"
echo ""
echo "  Next steps:"
echo "    1. Edit /home/ubuntu/momentum/.env with your API keys"
echo "    2. sudo systemctl restart momentum"
echo "    3. Open the URL above in your browser"
echo ""
