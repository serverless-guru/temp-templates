# AWS => Azure Workload Identity (One-click Deploy)

This repository contains an Azure subscription-scope ARM template + a guided Portal wizard (createUiDefinition) to create:

- A new **Resource Group**
- A **User Assigned Managed Identity (UAMI)**
- An **AWS => Azure federated identity credential** (subject = AWS IAM role ARN)
- A **Reader** role assignment scoped to the created **resource group** (least privilege)

> Note: The deployment runs in the **subscription** you select in the Azure Portal.

## Deploy to Azure (Wizard)

Click the button to open the Azure Portal wizard and deploy:

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fserverless-guru%2Ftemp-templates%2Fmain%2Fazure%2FmainTemplate.subscription.json/createUIDefinitionUri/https%3A%2F%2Fraw.githubusercontent.com%2Fserverless-guru%2Ftemp-templates%2Fmain%2Fazure%2FcreateUiDefinition.json)

## Direct link

If the button doesn’t work in your environment, use this direct link:

https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fserverless-guru%2Ftemp-templates%2Fmain%2Fazure%2FmainTemplate.subscription.json/createUIDefinitionUri/https%3A%2F%2Fraw.githubusercontent.com%2Fserverless-guru%2Ftemp-templates%2Fmain%2Fazure%2FcreateUiDefinition.json

## Inputs you will provide

- **Resource group name**
- **Managed identity name (UAMI)**
- **AWS IAM role ARN** (used as the federated credential **subject**)

Issuer and audience are fixed to AWS=>Azure defaults:

- `issuer`: `https://sts.amazonaws.com`
- `audiences`: `["api://AzureADTokenExchange"]`

## Permissions required

To deploy successfully, the signed-in user must have permission to:

- Create a resource group (or manage it if it already exists)
- Create a user-assigned managed identity in that resource group
- Create a role assignment **within that resource group**

## Files

- `azure/mainTemplate.subscription.json` — ARM template (subscription-scope)
- `azure/createUiDefinition.json` — Portal wizard definition (createUiDefinition)
