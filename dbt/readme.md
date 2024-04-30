# dbt
dbt is a transformation workflow that lets teams quickly and collaboratively deploy analytics code following software engineering best practices like modularity, portability, CI/CD, and documentation. Now anyone who knows SQL can build production-grade data pipelines.

About https://www.getdbt.com/product/what-is-dbt/

dbtCore is Open Source https://docs.getdbt.com/guides/getting-started/learning-more/getting-started-dbt-core

Howto install dbt https://docs.getdbt.com/dbt-cli/install/overview

## Usage
Install dbt locally. [instructions](https://docs.getdbt.com/dbt-cli/install/overview). *It works on Win only using WSL2 with Ubuntu for me. Not for windows python executives*
Init repository `git init`.   
Init dbp project `dbt init`.  
Do something *TODO*.  
Push your project to repository `git push`.   
Connect your dbt transoframtion to `Airbyte` by configuring Transformation step based on your repository. 
`Airbyte` will run dbt into selected container, pull your `dbt project` and run it inside container.  
