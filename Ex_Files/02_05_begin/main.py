import os

DEVELOPMENT = "development"
PRODUCTION = "production"
STAGING = "staging"
CODE_SPACE = "code_space"
LOCAL = "local"

# this allows me to access the environment
# that I'm running on and grab things from there.
# You can use this for keys, you can use this for modes
# that your application is running on like in this example.
# And the second argument is the default argument.
# So basically, I have the environment name,
# and if there's no environment name,
# I'm going to use development.
current_env = os.environ.get("ENV_NAME", DEVELOPMENT)

if current_env == DEVELOPMENT:
    print("Development environment")
elif current_env == PRODUCTION:
    print("Production environment")
elif current_env == STAGING:
    print("Staging environment")
elif current_env in [CODE_SPACE, LOCAL]:
    print("Codespace or local environment")
else:
    print("Unknown environment")
