from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
import subprocess
import yaml
import os

app = FastAPI()

class KedroParams(BaseModel):
    project_name: str
    params: Dict[str, str]

def load_project_config(config_file: str = "projects.yaml") -> Dict[str, str]:
    if not os.path.exists(config_file):
        raise FileNotFoundError("Config file not found.")
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config.get("projects", {})

def run_kedro_command(project_path: str, params: Dict[str, str]) -> str:
    # Convert params dictionary to a Kedro CLI formatted string
    params_str = ",".join([f"{key}={value}" for key, value in params.items()])
    command = ["kedro", "run", f"--params={params_str}"]

    try:
        # Running the command
        result = subprocess.run(command, cwd=project_path, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Error executing Kedro command: {e.stderr}")

@app.post("/run-kedro/")
def run_kedro(params: KedroParams):
    # Load the project configuration
    projects = load_project_config()

    # Get the project path from the config
    project_path = projects.get(params.project_name)

    if not project_path:
        raise HTTPException(status_code=404, detail="Project not found.")

    # Run the Kedro command with the provided parameters
    output = run_kedro_command(project_path, params.params)
    return {"output": output}
