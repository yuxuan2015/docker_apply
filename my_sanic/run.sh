echo "201805" | sudo -S docker stop hanlp_segment
echo "201805" | sudo -S docker rm hanlp_segment
echo "201805" | sudo -S docker build -t sanic_hanlp .
echo "201805" | sudo -S docker run --name hanlp_segment -p 8000:8000 -d sanic_hanlp:latest
echo "201805" | sudo -S docker ps
echo "201805" | sudo -S docker logs hanlp_segment