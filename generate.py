import urllib.parse

template = "https://raw.githubusercontent.com/serverless-guru/temp-templates/main/azure/mainTemplate.subscription.json"
ui = "https://raw.githubusercontent.com/serverless-guru/temp-templates/main/azure/uiFormDefinition.json"

print(
  "https://portal.azure.com/#create/Microsoft.Template/uri/"
  + urllib.parse.quote(template, safe="")
  + "/createUIDefinitionUri/"
  + urllib.parse.quote(ui, safe="")
)
