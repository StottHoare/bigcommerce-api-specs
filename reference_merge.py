import os
import yaml  # pip install pyyaml

base_yml = {
    'openapi': '3.0.0',
    'info': {
        'title': 'BigCommerce API',
        'version': '3.0.0',
        'termsOfService': 'https://www.bigcommerce.com/terms',
        'description': 'BigCommerce API',
        'contact': {
            'name': 'BigCommerce',
            'url': 'https://www.bigcommerce.com',
            'email': 'support@bigcommerce.com'
        }
    },
    'servers': {
        'url': 'https://api.bigcommerce.com/stores/{store_hash}/v3',
        'variables': {
            'store_hash': {
                'default': 'store_hash',
                'description': 'Permanent ID of the BigCommerce store.'
            },
            'description': 'BigCommerce API Gateway'
        }
    },
    'security': {
        'X-Auth-Token': []
    },
    'paths': {}
}

for file in os.listdir('./reference'):
    if not os.path.isfile(f'./reference/{file}'):
        continue

    if file == 'bigcommerce.yml':
        continue

    if not file.endswith('.yml') and not file.endswith('.yaml'):
        continue

    with open(f'./reference/{file}', "r", encoding="utf8") as f:
        print(file)
        f_yml = yaml.safe_load(f)

        if 'paths' in f_yml:
            for path, value in f_yml["paths"].items():
                base_yml["paths"][path] = value

with open('bigcommerce.yml', 'w', encoding='utf8') as outfile:
    yaml.dump(base_yml, outfile, default_flow_style=False, allow_unicode=True)
