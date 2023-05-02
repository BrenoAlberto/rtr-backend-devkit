#!/bin/bash

if [ ! -d "rtr-text-extraction-microservice" ]; then
  echo "Cloning Text Extraction Microservice..."
  git clone https://github.com/BrenoAlberto/rtr-text-extraction-microservice.git
else
  echo "Pulling latest changes for Text Extraction Microservice..."
  cd rtr-text-extraction-microservice
  git fetch origin 
  cd ..
fi
if [ ! -d "rtr-text-storage-microservice" ]; then
  echo "Cloning Text Storage Microservice..."
  git clone https://github.com/BrenoAlberto/rtr-text-storage-microservice.git
else
  echo "Pulling latest changes for Text Storage Microservice..."
  cd rtr-text-storage-microservice
  git fetch origin 
  cd ..
fi
if [ ! -d "rtr-script-upload-and-processing-microservice" ]; then
  echo "Cloning Script Upload and Processing Microservice..."
  git clone https://github.com/BrenoAlberto/rtr-script-upload-and-processing-microservice.git
else
  echo "Pulling latest changes for Script Upload and Processing Microservice..."
  cd rtr-script-upload-and-processing-microservice
  git fetch origin 
  cd ..
fi
if [ ! -d "rtr-chat-microservice" ]; then
  echo "Cloning Chat Microservice..."
  git clone https://github.com/BrenoAlberto/rtr-chat-microservice.git
else
  echo "Pulling latest changes for Chat Microservice..."
  cd rtr-chat-microservice
  git fetch origin 
  cd ..
fi

echo "All microservices have been updated successfully."
