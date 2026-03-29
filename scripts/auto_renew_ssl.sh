#!/bin/bash
# Temporarily free Port 80
docker stop vdpfoods_frontend

# Safely prompt Let's Encrypt for any due renewals natively
docker run --rm -v /root/vdpfoods-v2/certbot/conf:/etc/letsencrypt -p 80:80 certbot/certbot renew --standalone

# Immediately restart the frontend container to resume service
docker start vdpfoods_frontend
