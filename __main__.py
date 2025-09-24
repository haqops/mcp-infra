"""A Python Pulumi program"""

import pulumi
import pulumi_github as github
import pulumi_cloudflare as cloudflare


docker_template = {
    "owner": "haqops",
    "repository": "secure-mcp-server",
    "include_all_branches": False,
}

mcps = {
    "yahoofinance2": {
        "description": "Yahoo Finance MCP",
        "github_template": docker_template,
    }
}


for key, value in mcps.items():
    name = f"{key}-mcp"
    # https://www.pulumi.com/registry/packages/github/api-docs/repository/
    repo = github.Repository(key,
        name=name,
        description=value["description"],
        visibility="public",
        template=value["github_template"]
    )
    worker = cloudflare.Worker(key, 
        name=name,
        account_id=pulumi.Config().require("cloudflare_accountId"),
    )
