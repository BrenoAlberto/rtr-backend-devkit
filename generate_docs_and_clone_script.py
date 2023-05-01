import json
import os

def generate_clone_script_line(microservice_name, repository_name, repository_base_url):
    return f"""\
if [ ! -d "{repository_name}" ]; then
  echo "Cloning {microservice_name}..."
  git clone {repository_base_url}/{repository_name}.git
else
  echo "Pulling latest changes for {microservice_name}..."
  cd {repository_name}
  git checkout master
  git pull
  cd ..
fi
"""

with open("microservices.json") as f:
    data = json.load(f)

with open("documentation.md", "w") as doc:
    doc.write("# Microservices\n\n")
    for microservice in data["microservices"]:
        doc.write(f"## {microservice['name']}\n\n")
        doc.write(f"Repository: ({microservice['repositoryBaseURL']}/{microservice['repositoryName']})\n\n")
        doc.write("### Handlers\n\n")
        for handler in microservice["handlers"]:
            doc.write(f"- {handler['name']}: {handler['description']}\n")
        doc.write("\n")

with open("clone_microservices.sh", "w") as script:
    script.write("#!/bin/bash\n\n")
    for microservice in data["microservices"]:
        script.write(generate_clone_script_line(microservice['name'], microservice['repositoryName'], microservice['repositoryBaseURL']))
    script.write("\necho \"All microservices have been updated successfully.\"\n")

os.chmod("clone_microservices.sh", 0o755)
