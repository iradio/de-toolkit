# PREFECT

Docs: https://docs.prefect.io/latest/

Prefect Server can be deployed on a single node using docker-compose.
```bash
docker-compose up -d
```

## Details
The stack consists of these services:
- `server` – Prefect Server with a UI that registers and manages flows
- `agent` – Prefect agent that runs flows deployed to the `default` queue
- `cli` – emulates a developer workstation with the `prefect` package installed for building, testing, and deploying flows to the `server`

## Write the first flow

Tutorial: https://docs.prefect.io/latest/tutorial/first-steps/


## Deploy the flow

Run these commands in the `cli` container:
```bash
bash
cd ~/flows
prefect deployment build -n marvin -p default-agent-pool -q default catfacts.py:api_flow
prefect deployment apply ./api_flow-deployment.yaml
```
After that, run the `api_flow/marvin` flow in the UI: http://localhost:4200/flows.
Paste the URL `"https://catfact.ninja/fact"` (with quotes) as the URL parameter to trigger the flow.

To run a custom `agent` directly on the `cli` container, use:
```bash
prefect agent start --pool default-agent-pool --work-queue default
```
