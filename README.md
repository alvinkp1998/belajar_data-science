# Intro to Machine Learning Workshop for Beginners in 4 Days by JakartaLabs

## Overview
Learn the basic of Machine Learning and Deploy your own simple Natural Language Processing app!


## Workshop Preparation

### Step 1: Download Code
- Click here to [Download as ZIP ](https://github.com/satriawadhipurusa/machine_learning_workshop/archive/master.zip)
- Use git clone for those who are familiar  
  `$ git clone https://github.com/nplaybook/machine_learning_workshop.git`

### Step 2:  Miniconda Installation

#### **Windows user**
- Download miniconda for Python 3.7
    - Click this link to download: [Miniconda Windows 64-bit](https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe)
    - **Warning: skip this step if you have downloaded anaconda or miniconda previously!**

- Install miniconda
    - When theres option `install for`, chose `Just Me (recommended)`
    - For `Advanced Options`, please checklist `Register Anaconda as my default Python 3.7`
    - Wait until installation finished

- Run `Anaconda Prompt`

### **Mac user**
- Download miniconda untuk Python 3.7
    - Click this link to download: [Miniconda Mac OS X 64-bit](https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.pkg)
    - **Warning: skip this step if you have downloaded anaconda or miniconda previously!**

- Install miniconda
    - Install without changing any options
    - Wait until installation finished

- Run the terminal

#### **Linux user**
- Download miniconda untuk Python 3.7
    - Click this link to download: [Miniconda Linux 64-bit](https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh)
    - **Warning: skip this step if you have downloaded anaconda or miniconda previously!**
    
- Install miniconda
    - Run the terminal
    - Install miniconda using this command
        ```
        bash Miniconda3-latest-Linux-x86_64.sh
        ```
    - Type `yes` for license agreement, then `yes` again for `prepend miniconda install location to PATH`
    - Wait until installation finished
    
- Close and reopen the terminal again

### Step 3: Jupyter Installation
- The jupyter will be installed in the **base** environment
    ```
    conda install --name base jupyter nb_conda_kernels
    ```

### Step 4: Environment Installation
- Change directory (`cd` in command line) to your working directory
    ```
    cd machine_learning_workshop
    ```
- Run this command to install the environment `jl_ml`
    ```
    conda env create -f environment.yml
    ```
