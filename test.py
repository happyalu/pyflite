# Copyright (2016) Alok Parlikar <alok@parlikar.com>

import pyflite
import os
import sys

if not os.path.exists("cmu_us_rms.flitevox"):
    print("You need to download a voice to test this.  See the README")
    sys.exit(1)

pyflite.init()

x = pyflite.select_voice("cmu_us_rms.flitevox")
y = pyflite.text_to_wave("A whole joy was reaping, but they've gone south.", x);

from array import array
samples = array('h', y['samples'])
with open("test.raw", 'wb') as f:
    samples.tofile(f)


