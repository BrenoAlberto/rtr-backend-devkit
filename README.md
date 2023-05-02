# RemoteTableRead (RTR)

Remote Table Read is a app designed to help directors and actors practice their scripts remotely, with or without the presence of other actors. The platform makes the process of script rehearsal easy, leveraging AI and voice generation technologies to create an interactive experience for users.

## RTR Backend DevKit

The `rtr-backend-devkit` repository serves as a centralized hub for cloning and generating a minimal documentation for the whole RTR backend project codebase.

The main features of the `rtr-backend-devkit` repository include:

1. Cloning of microservices repositories: The repository reads from a `microservices.json` file containing the list of GitHub repositories for each microservice, cloning them if they don't exist, or pulling the latest changes if they do.

2. Automatic generation of documentation: The repository generates up-to-date documentation for all microservices by extracting descriptions from the `serverless.yml` and `functions.yml` files of each microservice. This ensures that the documentation is always in sync with the latest codebase.

3. TODO: ~~Pre-commit hooks: The repository includes a pre-commit hook that runs the `generate_docs_and_clone_script.py` script before every commit, ensuring that the documentation and clone script are always up-to-date.~~

# Documentation

## Text Extraction Microservice

Repository: (https://github.com/BrenoAlberto/rtr-text-extraction-microservice)

### Handlers

- extractText: Extract text from base64 encoded files

---

## Text Storage Microservice

Repository: (https://github.com/BrenoAlberto/rtr-text-storage-microservice)

#### No handlers found

---

## Script Upload and Processing Microservice

Repository: (https://github.com/BrenoAlberto/rtr-script-upload-and-processing-microservice)

### Handlers

- processScript: Extracts key information (characters, scenes, etc.) from a play script

---

## Chat Microservice

Repository: (https://github.com/BrenoAlberto/rtr-chat-microservice)

### Handlers

- chat: Chat with a character

---

