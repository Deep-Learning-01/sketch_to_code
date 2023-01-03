# Sketch To Code


1. Create Conda env and activate it 

```
conda create --prefix ./env python=3.8
```

2. Check whether NVIDIA Driver is available or not

``` 
nvidia-smi 
```
3. Download Cuda toolkit with maching the CUDA version you see by doing `nvidia-smi`

> For our project we will continue with CUDA 11.7
```
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin
sudo mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/11.7.0/local_installers/cuda-repo-ubuntu2204-11-7-local_11.7.0-515.43.04-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu2204-11-7-local_11.7.0-515.43.04-1_amd64.deb
sudo cp /var/cuda-repo-ubuntu2204-11-7-local/cuda-*-keyring.gpg /usr/share/keyrings/
sudo apt-get update
sudo apt-get -y install cuda

```

4. Set CUDA env variables

    > Open .bashrc file of system
    ```
    nano /home/$USER/.bashrc
    ```
    > Inside there add the following: (replace cuda-11.7 with your version)

    ```
    export PATH="/usr/local/cuda-11.7/bin:$PATH"
    export LD_LIBRARY_PATH="/usr/local/cuda-11.7/lib64:$LD_LIBRARY_PATH"
    ```

    >Then do the following to save and close the editor:
    ```
    On you keyboard press the following: 

    ctrl + o             --> save 
    enter or return key  --> accept changes
    ctrl + x             --> close editor
    ```

    Close the terminal and open a new one. 
    Now check if cuda is properly setup or not

    run:
    ``` 
    nvcc --version
    ```

> If previous steps are completed

5. Install requirements

``` 
pip install -r requirements.txt 
```

6. . Download Detectron 2 

```
python -m pip install 'git+https://github.com/facebookresearch/detectron2.git'
```
