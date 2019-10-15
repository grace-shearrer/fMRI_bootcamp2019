docker run --rm kaczmarj/neurodocker:0.6.0 generate docker \
 --base=debian:stretch --pkg-manager=apt \
  --add-to-entrypoint "source /etc/fsl/fsl.sh" \
  --install git \
  --vnc passwd=hunter2 start_at_runtime=true geometry=1920x1080 \
  --install xterm \
  --fsl version=5.0.10 method=binaries \
  --miniconda create_env=neuro \
              conda_install='numpy traits' \
  --miniconda use_env=neuro \
              conda_install='jupyter' \
  -o Dockerfile \
  >> Dockerfile
