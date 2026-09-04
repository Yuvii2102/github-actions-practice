import os

app_name = os.getenv("APP_NAME")
environment = os.getenv("ENVIRONMENT")

print(f"Application: {app_name}")
print(f"Environment: {environment}")
