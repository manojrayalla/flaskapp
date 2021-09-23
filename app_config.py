import os

CLIENT_ID = "45d1a619-bc41-49c7-b657-2d03ae9c4463" # Application (client) ID of app registration

CLIENT_SECRET = "IlC7Q~ClVx41F2GGoMR7klTkreeYZvzxBg8y7" # Placeholder - for use ONLY during testing.
# In a production app, we recommend you use a more secure method of storing your secret,
# like Azure Key Vault. Or, use an environment variable as described in Flask's documentation:
# https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
# CLIENT_SECRET = os.getenv("CLIENT_SECRET")
# if not CLIENT_SECRET:
#     raise ValueError("Need to define CLIENT_SECRET environment variable")

AUTHORITY = "https://login.microsoftonline.com/caadbe96-024e-4f67-82ec-fb28ff53d16d"  # For multi-tenant app
# AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"


