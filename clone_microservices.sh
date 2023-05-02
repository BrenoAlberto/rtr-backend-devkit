#!/bin/bash

if [ ! -d "rtr-text-extraction-microservice" ]; then
  echo "Cloning Text Extraction Microservice..."
  git clone https://github.com/BrenoAlberto/rtr-text-extraction-microservice.git
else
  echo "Pulling latest changes for Text Extraction Microservice..."
  cd rtr-text-extraction-microservice
  git checkout main
  git pull origin main
  cd ..
fi
if [ ! -d "rtr-text-storage-microservice" ]; then
  echo "Cloning Text Storage Microservice..."
  git clone https://github.com/BrenoAlberto/rtr-text-storage-microservice.git
else
  echo "Pulling latest changes for Text Storage Microservice..."
  cd rtr-text-storage-microservice
  git checkout main
  git pull origin main
  cd ..
fi
if [ ! -d "rtr-script-upload-and-processing-microservice" ]; then
  echo "Cloning Script Upload and Processing Microservice..."
  git clone https://github.com/BrenoAlberto/rtr-script-upload-and-processing-microservice.git
else
  echo "Pulling latest changes for Script Upload and Processing Microservice..."
  cd rtr-script-upload-and-processing-microservice
  git checkout main
  git pull origin main
  cd ..
fi

echo "All microservices have been updated successfully."
