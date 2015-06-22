"""
stream wiki-dumps to our data folder 
in various languages.
"""

import os
import progressbar
import requests

def download_file(url, prefix=None):
    local_filename = url.split('/')[-1]
    if prefix:
        local_filename = os.path.join(prefix, local_filename)
    # NOTE the stream=True parameter
    s = requests.Session()
    r = s.get(url, stream=True)
    response_length = int(r.headers.get('content-length'))
    pbar = progressbar.ProgressBar(widgets=[progressbar.Percentage(), progressbar.Bar()], maxval=response_length).start()
    current_chunk = 0
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            # TODO status reporting
            if chunk: # filter out keep-alive new chunks
                current_chunk += len(chunk)
                pbar.update(current_chunk)
                f.write(chunk)
                f.flush()
    pbar.finish()
    return local_filename

DOLPHIN_SOUNDS_URLS = [
    'https://swfsc.noaa.gov/uploadedFiles/Divisions/PRD/Sounds/BlueWhale.wav',
    'https://swfsc.noaa.gov/uploadedFiles/Divisions/PRD/Sounds/botNoseDolRisDol.wav',
    'https://swfsc.noaa.gov/uploadedFiles/Divisions/PRD/Sounds/BoNoDoFaKiWh.wav',
    'https://swfsc.noaa.gov/uploadedFiles/Divisions/PRD/Sounds/CommDol.wav',
    'https://swfsc.noaa.gov/uploadedFiles/Divisions/PRD/Sounds/FrasDolMelonHeadWha.wav',
    'https://swfsc.noaa.gov/uploadedFiles/Divisions/PRD/Sounds/FrasDolMelonHeadWha.wav',
    'https://swfsc.noaa.gov/uploadedFiles/Divisions/PRD/Sounds/HumpWhal.wav',
    'https://swfsc.noaa.gov/uploadedFiles/Divisions/PRD/Sounds/KillerWhales.wav',
    'https://swfsc.noaa.gov/uploadedFiles/Divisions/PRD/Sounds/MinkWhaBoin.wav',
    'https://swfsc.noaa.gov/uploadedFiles/Divisions/PRD/Sounds/PacWhSiDo.wav',
    'https://swfsc.noaa.gov/uploadedFiles/Divisions/PRD/Sounds/pacwhNorRwhd.wav',
    'https://swfsc.noaa.gov/uploadedFiles/Divisions/PRD/Sounds/PilotWhales.wav',
    'https://swfsc.noaa.gov/uploadedFiles/Divisions/PRD/Sounds/PygmyKillerWhale.wav',
    'https://swfsc.noaa.gov/uploadedFiles/Divisions/PRD/Sounds/RissDol.wav',
    'https://swfsc.noaa.gov/uploadedFiles/Divisions/PRD/Sounds/RouTooDol.wav',
    'https://swfsc.noaa.gov/uploadedFiles/Divisions/PRD/Sounds/SpermWhaleNormalClicks.wav',
    'https://swfsc.noaa.gov/uploadedFiles/Divisions/PRD/Sounds/SperWhaRapClik.wav',
    'https://swfsc.noaa.gov/uploadedFiles/Divisions/PRD/Sounds/SperWhalSloCli.wav',
    'https://swfsc.noaa.gov/uploadedFiles/Divisions/PRD/Sounds/SperWhaRapidandCoda.wav',
    'https://swfsc.noaa.gov/uploadedFiles/Divisions/PRD/Sounds/s132%20spinner%20dolphins.wav',
    'https://swfsc.noaa.gov/uploadedFiles/Divisions/PRD/Sounds/SpottedDolphins.wav',
    'https://swfsc.noaa.gov/uploadedFiles/Divisions/PRD/Sounds/StripedDolphins.wav'
]
prefix = os.path.join('data', 'dolphin')
if not os.path.exists(prefix):
    os.mkdir(prefix)
for url in DOLPHIN_SOUNDS_URLS:
    filename = os.path.join(prefix, url.split('/')[-1])
    if not os.path.exists(filename):
        print 'Downloading %s' % filename
        download_file(url, prefix)

for lang in ['en']:
    url = "https://dumps.wikimedia.org/{0}wiki/latest/{0}wiki-latest-pages-articles.xml.bz2".format(lang)
    prefix = os.path.join('data', lang)
    filename = os.path.join(prefix, url.split('/')[-1])
    if not os.path.exists(prefix):
        os.mkdir(prefix)
    if not os.path.exists(filename):
        print 'Downloading %s' % filename
        download_file(url, prefix)