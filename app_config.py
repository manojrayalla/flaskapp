import os

CLIENT_ID = "609bde9b-5fd2-4622-9ea9-3636c463197b" # Application (client) ID of app registration

CLIENT_SECRET = "8mH7Q~MzzmSY~t8NYe_ArBJzDihhy0bs_gw3m" # Placeholder - for use ONLY during testing.
# In a production app, we recommend you use a more secure method of storing your secret,
# like Azure Key Vault. Or, use an environment variable as described in Flask's documentation:
# https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
# CLIENT_SECRET = os.getenv("CLIENT_SECRET")
# if not CLIENT_SECRET:
#     raise ValueError("Need to define CLIENT_SECRET environment variable")

AUTHORITY = "https://login.microsoftonline.com/2914923e-572c-4c10-b88c-2f12bf346de7"  # For multi-tenant app
# AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"


