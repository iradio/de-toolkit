# PREFECT

Docs https://docs.prefect.io/latest/

Prefect Server can be deployed on a single node using docker-compose.
```bash
docker-compose up -d
```

## Details
Consist of these services
- `server` - Prefect server with UI witch register and manage flows
- `agent` - Prefect agent which runs flows deployed to queue `default`
- `cli` - emulation of developer's machine with `prefect` package installed to run develop and test flows, also used to deploy flows to the `server`

# Write the first flow

Tutorial https://docs.prefect.io/latest/tutorial/first-steps/


# Deploy flow

Run it on the `cli` container:
```bash
bash
cd ~/flows
prefect deployment build -n marvin -p default-agent-pool -q default catfacts.py:api_flow
prefect deployment apply ./api_flow-deployment.yaml
```
After that, you should run `api_flow/marvin` flow in the UI: http://localhost:4200/flows .
Paste URL `"https://catfact.ninja/fact"`(with quotas) as a URL parameter to run this flow.

To run a custom `agent` directly on `cli` container you could use this command 
prefect agent start --pool default-agent-pool --work-queue default
