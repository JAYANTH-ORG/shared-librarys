import subprocess
import json

# Scan NPM dependencies

def scan_npm():
    try:
        result = subprocess.run(['npm', 'audit', '--json'], capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except Exception as e:
        return {'error': str(e)}

# Scan Maven dependencies

def scan_maven():
    try:
        result = subprocess.run(['mvn', 'org.owasp:dependency-check-maven:check', '-Dformat=JSON'], capture_output=True, text=True, check=True)
        # Parse the output file if generated
        # For demo, just return command output
        return {'output': result.stdout}
    except Exception as e:
        return {'error': str(e)}

# Scan Docker image with Trivy

def scan_docker(image_name='myapp:latest'):
    try:
        result = subprocess.run(['trivy', 'image', '--format', 'json', image_name], capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except Exception as e:
        return {'error': str(e)}

# AI-powered prioritization and explanation (placeholder)
def ai_prioritize_and_explain(vulns):
    # In real implementation, call AI model (e.g., Copilot, Gemini) here
    # For demo, just return a summary
    summary = []
    for tool, result in vulns.items():
        if 'error' in result:
            summary.append(f"{tool}: Error - {result['error']}")
        else:
            summary.append(f"{tool}: {len(result.get('vulnerabilities', []))} vulnerabilities found.")
    return '\n'.join(summary)

if __name__ == "__main__":
    results = {
        'npm': scan_npm(),
        'maven': scan_maven(),
        'docker': scan_docker()
    }
    print("Dependency & Vulnerability Scan Results:")
    print(json.dumps(results, indent=2))
    print("\nAI Prioritization & Explanation:")
    print(ai_prioritize_and_explain(results))
