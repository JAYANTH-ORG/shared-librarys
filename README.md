# Intelligent Dependency & Vulnerability Management Bot

This project provides a reusable GitHub Action for scanning dependencies (Maven, NPM, Docker), checking for vulnerabilities, and using AI to prioritize and explain issues. Optionally, it can be extended to auto-create PRs or issues for fixes.

## Usage
- Add the workflow in `.github/workflows/dependency-vuln-bot.yml` to your repo.
- The action runs on every push or PR to `main`.
- Scans NPM, Maven, and Docker dependencies.
- Outputs a summary and AI-generated explanation.

## Extending
- Integrate with Copilot, Gemini, or other AI APIs for advanced prioritization and explanations.
- Add logic to auto-create PRs or issues for critical vulnerabilities.

## Requirements
- Python 3.10+
- `npm`, `mvn`, and `trivy` installed in the runner environment.
