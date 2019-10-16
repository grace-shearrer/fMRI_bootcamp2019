#!/bin/bash
docker run --rm kaczmarj/neurodocker:0.6.0 generate docker \
 --base=debian:stretch --pkg-manager=apt \
  --install git \
  --vnc passwd=graceiscool start_at_runtime=true geometry=1920x1080 \
  --install xterm \
  --fsl version=5.0.10 method=binaries \
  --miniconda create_env=neuro \
              conda_install='numpy traits' \
  --miniconda use_env=neuro \
              conda_install='jupyterhub' \
              conda_install='jupyterlab' \
              conda_install='notebook=6.0.0' \
              #conda_install='jupyter notebook --generate-config'
              miniconda_version="4.3.31" 
