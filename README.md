# pyflite Python Module

Python API for flite

This provides basic Python API to perform text-to-speech using Flite.

## Build Instructions (Uses VirtualEnv)

```
git clone https://github.com/happyalu/pyflite.git
cd pyflite

git clone https://github.com/happyalu/flite.git
cd flite
./configure --enable-shared
make

cd ..
virtualenv -p /usr/bin/python3 venv
. venv/bin/activate

python3 setup.py build
python3 setup.py install

# Test that it works.
wget http://www.festvox.org/flite/packed/flite-2.0/voices/cmu_us_rms.flitevox
python3 test.py
```
