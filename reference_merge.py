import os
import yaml  # pip install pyyaml


def base_yml(url, title):
    return {
        'openapi': '3.0.0',
        'info': {
            'title': title,
            'version': '3.0.0',
            'termsOfService': 'https://www.bigcommerce.com/terms',
            'description': title,
            'contact': {
                'name': 'BigCommerce',
                'url': 'https://www.bigcommerce.com',
                'email': 'support@bigcommerce.com'
            }
        },
        'servers': {
            'url': url,
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


ymls = {
    'https://api.bigcommerce.com/stores/{store_hash}/v3': base_yml('https://api.bigcommerce.com/stores/{store_hash}/v3', 'BigCommerce API Management V3'),
    'https://{store_domain}/api/storefront': base_yml('https://{store_domain}/api/storefront', 'BigCommerce API Storefront'),
    'https://api.bigcommerce.com/stores/{store_hash}/v2': base_yml('https://api.bigcommerce.com/stores/{store_hash}/v2', 'BigCommerce API Management V2')
}

serverset = {}

for file in os.listdir('./reference'):
    if not os.path.isfile(f'./reference/{file}'):
        continue

    if file == 'bigcommerce.yml':
        continue

    if not file.endswith('.yml') and not file.endswith('.yaml'):
        continue

    with open(f'./reference/{file}', 'r', encoding='utf8') as f:
        print(file)
        f_yml = yaml.safe_load(f)

        if 'servers' in f_yml and 'paths' in f_yml:
            for server in f_yml['servers']:
                url = server['url']
                if server['url'] in ymls:
                    for path, value in f_yml['paths'].items():
                        ymls[server['url']]['paths'][path] = value

for collection in ymls.values():
    if len(collection["paths"]) > 0:
        with open(f'{collection["info"]["title"]}.yml', 'w', encoding='utf8') as outfile:
            yaml.dump(collection, outfile, default_flow_style=False,
                      allow_unicode=True)
