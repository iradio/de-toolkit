# dbt

dbt is a transformation workflow that lets teams quickly and collaboratively deploy analytics code while applying software engineering best practices such as modularity, portability, CI/CD, and documentation. Anyone who knows SQL can build production-grade data pipelines.

Overview: https://www.getdbt.com/product/what-is-dbt/

dbt Core is open source: https://docs.getdbt.com/guides/getting-started/learning-more/getting-started-dbt-core

How to install dbt: https://docs.getdbt.com/dbt-cli/install/overview

## Usage
Install dbt locally (instructions: https://docs.getdbt.com/dbt-cli/install/overview). *On Windows, WSL2 with Ubuntu has worked for me; native Windows Python executables did not.*
Initialize the repository: `git init`.  
Initialize the dbt project: `dbt init`.  
Complete the required project work. *TODO*.  
Push your project to the repository: `git push`.  
Connect your dbt transformation to `Airbyte` by configuring the Transformation step based on your repository.  
`Airbyte` runs dbt in the selected container, pulls your `dbt` project, and executes it there.  
