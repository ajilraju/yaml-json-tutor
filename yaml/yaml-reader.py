import yaml

# Open the YAML file and load its content
with open('mutli-line-strings.yaml', 'r') as stream:
    try:
        yaml_data = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

# Print the YAML data
print(yaml_data)

