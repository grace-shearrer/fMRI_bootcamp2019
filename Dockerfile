# fMRI workshop
# Start with neurodebian image
FROM neurodebian:trusty

MAINTAINER GE Shearrer <grace.shearrer@gmail.com>
RUN echo 'welcome!'

# Run apt-get calls
RUN apt-get update && apt-get install -y wget
RUN wget -O- http://neuro.debian.net/lists/trusty.us-nh.full | sudo tee /etc/apt/sources.list.d/neurodebian.sources.list
RUN apt-key adv --recv-keys --keyserver hkp://pool.sks-keyservers.net:80 0xA5D32F012649A5A9
RUN apt-get update
RUN apt-get install -y fsl-5.0-complete

# Configure environment
ENV FSLDIR=/usr/lib/fsl/5.0
ENV FSLOUTPUTTYPE=NIFTI_GZ
ENV PATH=$PATH:$FSLDIR
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$FSLDIR

# Run configuration script for normal usage
RUN echo ". /etc/fsl/5.0/fsl.sh" >> /root/.bashrc


###################################################################################################
RUN echo 'now snake time!'

FROM continuumio/anaconda3
WORKDIR /usr/work_dir

# Run configuration script for normal usage
RUN echo ". /etc/fsl/5.0/fsl.sh" >> /root/.bashrc
#RUN conda install -c conda-forge fsleyes
###################################################################################################
EXPOSE 3000
