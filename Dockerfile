FROM nvidia/cuda:11.7.0-cudnn8-devel-ubuntu22.04

ENV DEBIAN_FRONTEND noninteractive

ENV PATH /opt/conda/bin:$PATH

# set bash as current shell
RUN chsh -s /bin/bash
SHELL ["/bin/bash", "-c"]

# install anaconda
RUN apt-get update --fix-missing && \
    apt-get install wget -y tcl ca-certificates libglib2.0-0 libxext6 libsm6 git -y && \
    apt-get clean


RUN wget --quiet https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh -O ~/anaconda.sh && \
        /bin/bash ~/anaconda.sh -b -p /opt/conda && \
        rm ~/anaconda.sh && \
        ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
        echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
        find /opt/conda/ -follow -type f -name '*.a' -delete && \
        find /opt/conda/ -follow -type f -name '*.js.map' -delete && \
        /opt/conda/bin/conda clean -afy

# set path to conda
ENV PATH /opt/conda/bin:$PATH


# setup conda virtual environment
#RUN conda update conda \
#    && conda create --prefix skcenv python=3.8

RUN #echo "conda activate skcenv" >> ~/.bashrc
ENV PATH /opt/conda/envs/skcenv/bin:$PATH
ENV CONDA_DEFAULT_ENV $base


#project setup
WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install awscli -y  \
#    echo "conda uninstall sypder" >> ~/.bash \
#    echo "conda uninstall numba"
    && pip install --upgrade pip && pip install -r requirements.txt

RUN python -m pip install 'git+https://github.com/facebookresearch/detectron2.git'

CMD ["python3", "app.py"]








