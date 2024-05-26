"""
This script is what keeps the react-game-icons-auto package up to date.
When it's run, we download the game-icons.net full package from their site.
We then unzip it and walk the full directory structure, generating custom typescript react files
to be used in a project.

We also crawl the https://game-icons.net/tags.html page so that we can keep note of which icons belong to
which tags, and expose that in the package as well.

The index entry point is reserved for last.
"""

# Get all the tags and what's in each tag.
import argparse
import requests
import re
import time
import zipfile
from lxml import html, etree
import urllib.request
import os.path

parser = argparse.ArgumentParser(description="Generate react-game-icons-auto")
parser.add_argument('--skip-tags', action='store_true')
parser.add_argument('--skip-download', action='store_true')
parser.add_argument('--skip-unzip', action='store_true')
args = parser.parse_args()

icons_to_tags = {}

if not args.skip_tags:
    r = requests.get('https://game-icons.net/tags.html')

    if r.status_code != 200:
        raise Exception('Game-icons.net returned non 200 status')

    tree = html.fromstring(r.text)

    all_links = tree.xpath("//a[contains(@href,'tags')]")
    index = 0
    for link in all_links:
        print(f"Processing {index} of {len(all_links)} ({index/len(all_links)*100:.2f}%)")
        url = link.get('href')
        text_content = link.text_content()
        parts = re.split('[^a-zA-Z& ]', text_content)

        tag_label = parts[0].strip()

        r2 = requests.get('https://game-icons.net/' + url)
        if r2.status_code != 200:
            raise Exception(f'Game-icons.net returned non 200 status on category {tag_label}')

        child_tree = html.fromstring(r2.text)
        all_icons = child_tree.xpath("//img[@class='icon']")
        for icon in all_icons:
            icon_src = icon.get('src')
            name = icon_src[icon_src.rfind('/') + 1:]
            if name in icons_to_tags:
                icons_to_tags[name].append(tag_label)
            else:
                icons_to_tags[name] = [tag_label]
        time.sleep(0.1)
        index += 1
else:
    print('Skipping tags....')

# Now that we have all of the tags, let's go on to the download stage and do generation
if not args.skip_download:
    urllib.request.urlretrieve("https://game-icons.net/archives/svg/zip/ffffff/transparent/game-icons.net.svg.zip", 'game-icons.net.svg.zip')
else:
    print('Skipping download...')

if not args.skip_unzip:
    if not os.path.isfile('game-icons.net.svg.zip'):
        raise Exception('Game-icons.net zip file missing')

    with zipfile.ZipFile('game-icons.net.svg.zip', 'r') as zip_ref:
        zip_ref.extractall('raw')
else:
    print('Skipping unzipping...')

path = os.path.join('raw', 'icons', 'ffffff', 'transparent', '1x1')

if not os.path.isdir(path):
    raise Exception('Game-icons.net file structure has changed')

template_path = os.path.join('npm', 'Template.js')

if not os.path.isfile(template_path):
    raise Exception('Template file not found?')

with open(template_path, 'r') as template:
    template = template.read()

    for root, dirs, files in os.walk(path):
        for file in files:
            with open(os.path.join(root, file), 'r') as fd:
                creator = root[root.rfind(os.path.sep) + 1:]
                icon_name = file
                if icon_name.endswith('.svg'):
                    icon_name = icon_name[:-4]
                icon_name = icon_name.title()
                icon_name = re.sub('[^a-zA-Z]', '', icon_name)

                data = fd.read()
                icon_parsed = html.fromstring(data)
                building_paths = ''
                for part in icon_parsed:
                    building_paths += etree.tostring(part, pretty_print=True).decode()

                my_data = template.replace('TEMPLATE', icon_name)
                my_data = my_data.replace('PATH', building_paths)
                my_data = my_data.replace('fill="#fff"', 'fill={color}')


                dir_path = os.path.join('npm', 'icons', creator)
                if not os.path.isdir(dir_path):
                    os.mkdir(dir_path)

                with open(os.path.join(dir_path, f'{icon_name}.js'), 'w+') as fd:
                    fd.write(my_data)

                exit(0)