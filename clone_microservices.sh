#!/bin/bash

if [ ! -d "rtr-text-extraction-microservice" ]; then
  echo "Cloning Text Extraction Microservice..."
  git clone https://github.com/BrenoAlberto/rtr-text-extraction-microservice.git
else
  echo "Pulling latest changes for Text Extraction Microservice..."
  cd rtr-text-extraction-microservice
  git checkout master
  git pull
  cd ..
fi
if [ ! -d "rtr-text-storage-microservice" ]; then
  echo "Cloning Text Storage Microservice..."
  git clone https://github.com/BrenoAlberto/rtr-text-storage-microservice.git
else
  echo "Pulling latest changes for Text Storage Microservice..."
  cd rtr-text-storage-microservice
  git checkout master
  git pull
  cd ..
fi

echo "All microservices have been updated successfully."
