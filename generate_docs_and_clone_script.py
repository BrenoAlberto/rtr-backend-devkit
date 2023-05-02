import json
import os
import subprocess
import yaml


def generate_clone_script_line(microservice_name, repository_name, repository_base_url):
    return f"""\
if [ ! -d "{repository_name}" ]; then
  echo "Cloning {microservice_name}..."
  git clone {repository_base_url}/{repository_name}.git
else
  echo "Pulling latest changes for {microservice_name}..."
  cd {repository_name}
  git checkout main
  git pull origin main
  cd ..
fi
"""

def create_clone_script(data):
    with open("clone_microservices.sh", "w") as script:
        script.write("#!/bin/bash\n\n")
        for microservice in data["microservices"]:
            script.write(
                generate_clone_script_line(
                    microservice["name"],
                    microservice["repositoryName"],
                    microservice["repositoryBaseURL"],
                )
            )
        script.write('\necho "All microservices have been updated successfully."\n')

    os.chmod("clone_microservices.sh", 0o755)
    subprocess.run("./clone_microservices.sh", shell=True)

def write_documentation(data):
    with open("documentation.md", "w") as doc:
        doc.write("## Microservices\n\n")
        for microservice in data["microservices"]:
            doc.write(f"### {microservice['name']}\n\n")
            doc.write(
                f"Repository: ({microservice['repositoryBaseURL']}/{microservice['repositoryName']})\n\n"
            )

            if not os.path.isfile(f"{microservice['repositoryName']}/functions.yml"):
                doc.write("#### No handlers found\n\n")
                continue

            doc.write("#### Handlers\n\n")

            with open(
                f"{microservice['repositoryName']}/functions.yml", "r"
            ) as functions_file:
                functions_data = yaml.safe_load(functions_file)

            for handler in functions_data:
                if "description" in functions_data[handler]:
                    doc.write(f"- {handler}: {functions_data[handler]['description']}\n")
            doc.write("\n")

def update_readme():
    with open("README.md", "r") as readme:
        readme_lines = readme.readlines()

    with open("README.md", "w") as readme:
        for line in readme_lines:
            readme.write(line)
            if line.strip() == "# Documentation":
                break

        readme.truncate()
        readme.write("\n")

        with open("documentation.md", "r") as doc:
            for line in doc.readlines():
                readme.write(line)

def main():
    with open("microservices.json") as f:
        data = json.load(f)

    create_clone_script(data)
    write_documentation(data)
    update_readme()

if __name__ == "__main__":
    main()
