# First, install miniconda if not already installed
conda create --name rturk python
conda activate rturk
pip freeze
# Should have only one or so packages
python setup.py install
pip freeze
# Should now have raspberryturk as a package
conda install numpy
pip install opencv-python
pip install chess
pip freeze
# Should see something like this
# chess==1.9.4
# mkl-fft==1.3.1
# mkl-random @ file:///opt/concourse/worker/volumes/live/a9eca864-069c-4240-73c8-4e51b036a10d/volume/mkl_random_1639994047876/work
# mkl-service==2.4.0
# numpy @ file:///private/var/folders/sy/f16zz6x50xz3113nwtb9bvq00000gp/T/abs_cd2y6umv2d/croot/# numpy_and_numpy_base_1668593733683/work
# opencv-python==4.6.0.66
# raspberryturk==0.0.1b0
# six @ file:///tmp/build/80754af9/six_1644875935023/work