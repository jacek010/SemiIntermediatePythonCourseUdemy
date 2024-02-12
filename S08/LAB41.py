import requests
import os
import shutil


def save_url_to_file(url, file_path):

    r = requests.get(url, stream = True)
    with open(file_path, "wb") as f:
        f.write(r.content)


url = 'http://www.mobilo24.eu/spis/'
dir = 'LAB41_files'
tmpfile = 'download.tmp'
file = 'spis.html'

tmpfile_path = os.path.join(dir, tmpfile)
file_path = os.path.join(dir, file)

try:
    if os.path.exists(tmpfile_path):
        print(f'Removing {tmpfile_path}')
        os.remove(tmpfile_path)

    print(f'Downloading {url}')
    save_url_to_file(url, tmpfile_path)

    print(f'Copying {tmpfile_path} to {file_path}')
    shutil.copy(tmpfile_path, file_path)

except Exception as e:
    print(f'Error downloading the URL {url}')
    print(f'Error details: {e}')

else:
    print(f'Successfully downloaded to {file}')

finally:
    if os.path.exists(tmpfile_path):
        print(f'Final removal of {tmpfile_path}')
        os.remove(tmpfile_path)
    print('DONE')
