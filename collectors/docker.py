import subprocess

def get_docker_containers():
    try:
        result = subprocess.run(
            ["docker", "ps", "--format", "{{.Names}}"],
            capture_output=True,
            text=True
        )
        containers = result.stdout.strip().split("\n")
        return [c for c in containers if c]
    except Exception:
        return []
