import yaml

file = "The Official YAML Web Site.txt"
with open(file) as f:
    yaml_data = yaml.full_load(f)
    print(yaml_data)
