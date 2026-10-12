#!/bin/bash
# Pull latest code and restart MOMentum
set -e

cd /home/ubuntu/momentum
git pull origin main
source venv/bin/activate
pip install -r requirements.txt
sudo systemctl restart momentum

echo "MOMentum updated and restarted."
echo "Check: sudo systemctl status momentum"
