# BoAT-TemplateProject
## Building a BoAT application development project based on the BoAT-ProjectTemplate development template

The `BoAT-ProjectTemplate` repository is a universal development template for developing applications based on the `BoAT Infra Arch` infrastructure.

Application development based on the `BoAT Infra Arch` infrastructure is achieved through three open-source repositories.

1. `BoAT-ProjectTemplate`: provides a compilation structure, selects and clones compilation repositories to the local system, and configures the corresponding compilation environment according to the selected public repository.

2. `BoAT-SupportLayer`: is the source code repository of the `BoAT Support Layer` of the `BoAT Infra Arch` infrastructure, which provides the underlying support required by BoAT applications, including an operating system abstraction layer, a driver abstraction layer, and a BoAT general component layer, providing common underlying operation interfaces for BoAT applications.

3. `BoAT-Engine`: is the source code repository of the `BoAT Engine` layer of the `BoAT Infra Arch` infrastructure, which provides API interfaces related to blockchain access for BoAT applications, implementing BoAT application's access to different blockchains.

These three repositories and the application platform jointly constitute the development environment based on the `BoAT Infra Arch` infrastructure, where BoAT applications are born.

The following steps explain how to compile demo applications for different blockchains on the linux-default platform by combining three repositories:

### Development Environment Preparation

To build the application development environment based on the `BoAT Infra Arch` infrastructure in the Linux operating system, it is necessary to confirm that the following dependencies and software have been installed on the Linux platform.

1. curl
```
sudo apt install curl
```

2. libsubunit-dev
```
sudo apt install libsubunit-dev
```

3. python3, version >= 3.5
```
sudo apt install python3
```

4. git
```
sudo apt install git
```

### 1. Clone the BoAT-ProjectTemplate repository to local

Execute the following command in the terminal of the Linux operating system to clone the `BoAT-ProjectTemplate` repository to local:

```
git clone https://github.com/aitos-io/BoAT-ProjectTemplate.git
```

After successful execution, a `BoAT-ProjectTemplate` directory will be created in the current path, which stores the development template cloned from GitHub. The contents of the `BoAT-ProjectTemplate/` directory after cloning are as follows:

```
BoAT-ProjectTemplate
|-- BoATLibs.conf
|-- config.py
|-- README.md
|-- README_cn.md
```

You can also clone the `BoAT-ProjectTemplate` repository as the development project directory and build the `boatDevelop` development directory:

```
git clone -b dev git@github.com:aitos-io/BoAT-ProjectTemplate.git boatDevelop
```

Clone the `BoAT-SupportLayer` repository to the `boatDevelop` directory and develop in this directory.

### 2. Modify BoATLibs.conf

The `BoATLibs.conf` file is used to configure the open source repositories used in the current project. The subsequent configuration script clones the corresponding open source repositories to local by reading the configuration information in the current file.

The `BoATLibs.conf` file includes the `BoAT-SupportLayer` repository by default, and the content is as follows:

```
BoAT-SupportLayer
```

In the current sample project, the `BoAT Engine` open source repository will also be used, so add `BoAT-Engine` to the `BoATLibs.conf` file. The content after adding is as follows:

```
BoAT-SupportLayer
BoAT-Engine
```

When modifying the `BoATLibs.conf` file, please note:

```
1. Only one repository name can be written in one line.
2. The repository name must be correct, especially pay attention to case sensitivity. The cloned directory name will be the same as the name written. If the case is wrong, it will not affect the result of `git clone`, but it will cause errors in the configuration script execution.
```

### 3. Run the config.py script and complete the compilation directory construction and compilation file configuration according to the prompts.

The `config.py` script contains two main execution steps:

1. Clone the repository source code included in the `BoATLibs.conf` file.
2. Generate the `Makefile` based on the obtained source code repository.

Execute the script configuration in the `BoAT-ProjectTemplate/` directory, and there will be several interactions during the execution process. The detailed process is as follows:

```
python3 config.py
```

```
We will clone the BoAT-SupportLayer repository, which may take several minutes

Input the branch name or null:
```

Press Enter here to clone the `main` branch of the `BoAT-SupportLayer` open source repository.

```
branch name is []

git clone https://github.com/aitos-io/BoAT-SupportLayer.git

Cloning into 'BoAT-SupportLayer'...
remote: Enumerating objects: 2837, done.
remote: Counting objects: 100% (611/611), done.
remote: Compressing objects: 100% (281/281), done.
remote: Total 2837 (delta 384), reused 521 (delta 317), pack-reused 2226
Receiving objects: 100% (2837/2837), 2.41 MiB | 1.86 MiB/s, done.
Resolving deltas: 100% (1769/1769), done.
git cmd succ


We will clone the BoAT-Engine repository, which may take several minutes

Input the branch name or null:
```

Press Enter here to clone the `main` branch of the `BoAT-Engine` open source repository.

```
branch name is []

git clone https://github.com/aitos-io/BoAT-Engine.git

Cloning into 'BoAT-Engine'...
remote: Enumerating objects: 860, done.
remote: Counting objects: 100% (860/860), done.
remote: Compressing objects: 100% (400/400), done.
remote: Total 860 (delta 551), reused 752 (delta 455), pack-reused 0
Receiving objects: 100% (860/860), 513.51 KiB | 365.00 KiB/s, done.
Resolving deltas: 100% (551/551), done.
git cmd succ

overwrite the Makefile?(Y/n):
```

Press Enter here to be judged as `Y: Yes`; if you do not want to overwrite the `Makefile`, you can enter `n`, and the compilation configuration will end immediately.
```
Yes

 Select blockchain list as below:
 [1] ETHEREUM          : 
 [2] PLATON            : 
 [3] PLATONE           : 
 [4] FISCOBCOS         : 
 [5] HLFABRIC          : 
 [6] HWBCS             : 
 [7] CHAINMAKER_V1     : 
 [8] CHAINMAKER_V2     : 
 [9] VENACHAIN         : 
 [a] QUORUM            : 
 [b] CITA              : 
 [0] All block chains
 Example:
  Select blockchain list as below:
  input:1a
  Blockchain selected:
   [1] ETHEREUM
   [a] QUORUM

input:
```

Enter the blockchain that needs to be supported in the application here. Enter `9` to select the `venachain` blockchain. 

```
input:9
Blockchain selected:
 [9] VENACHAIN

Select the platform list as below:
[1] linux-default             : Default linux platform
[2] Fibocom-L610              : Fibocom's LTE Cat.1 module
[3] create a new platform
```

Enter `1` here to select the target platform of the application as `linux-default`. After the selection, the script will automatically generate the `Makefile`.

```
1
platform is : linux-default

include BoAT-SupportLayer.conf

include BoAT-Engine.conf

./BoAT-SupportLayer/demo/ False
./BoAT-Engine/demo/ True
Configuration completed
```

After the configuration is completed, the development directory will contain:

```
BoAT-ProjectTemplate
|-- <BoAT-SupportLayer>
|-- <BoAT-Engine>
|-- BoATLibs.conf
|-- config.py
|-- Makfile
|-- README.md
|-- README_en.md
```
### 5. Compilation

Execute the compilation command in the `BoAT-ProjectTemplate/` directory:

```
make demo VENACHAIN_DEMO_IP="127.0.0.1"
```

Among them, `VENACHAIN_DEMO_IP="127.0.0.1"` provides a macro for the IP address of a `venachain` access node. This requires the correct node IP macro provided by the user. Otherwise, the `demo` program of `venachain` cannot access the node correctly. Incorrect macros do not affect compilation.

During the compilation process, you may encounter the following errors. Follow the given processing method to solve the corresponding problem.

Common Error 1:

```
curlport.c:33:23: fatal error: curl/curl.h: No such file or directory
```

Install the `libcurl4-gnutls-dev` dependency library:

```
sudo apt-get install libcurl4-gnutls-dev
```

Common Error 2:

```
boatssl.c:26:25: fatal error: openssl/evp.h: No such file or directory
```

Install the `libssl-dev` dependency library:

```
sudo apt-get install libssl-dev
```

After the compilation is completed, the `BoAT-ProjectTemplate` directory contains the following contents:

```
<BoAT-ProjectTemplate>
|-- <BoAT-SupportLayer>
|-- <BoAT-Engine>
|-- BoATLibs.conf
|-- <build>
    |-- <BoAT-Engine>
        |-- <demo>
            |-- <demo_venachain>
                |-- demo_venachain_mycontract_create_internalGen
                |-- demo_venachain_mycontract_create_native
                |-- demo_venachain_mycontract_create_pkcs
                |-- demo_venachain_mycontract_onetime_internalGen
                |-- demo_venachain_mycontract_onetime_native
                |-- demo_venachain_mycontract_onetime_pkcs
|-- config.py
|-- <lib>
    |-- libboatengine.a
    |-- libboatvendor.a
|-- Makfile
|-- README.md
|-- README_en.md
```

### 6. Output directory after compilation:

After the compilation is completed in the `BoAT-ProjectTemplate/` directory, two new directories are added:

`build` and `lib`

`build:`

Output the intermediate files produced during the compilation process and the executable files of the demos produced in each source code library. In this example, the executable files of `demo` of `venachain` are output. In this example, the `demo` output of `venachain` is in the `BoAT-ProjectTemplate/build/BoAT-Engine/demo/demo_venachain/` directory, which contains six executable files:

```
demo_venachain_mycontract_create_internalGen
demo_venachain_mycontract_create_native
demo_venachain_mycontract_create_pkcs
demo_venachain_mycontract_onetime_internalGen
demo_venachain_mycontract_onetime_native
demo_venachain_mycontract_onetime_pkcs
```

`lib:`

Output the static library file generated by each open source repository. Two static libraries are generated in this project:

```
libboatengine.a: BoAT-Engine static library
libboatvendor.a: BoAT-SupportLayer static library
```
### 7. Running the demo:

Execute each demo in the `BoAT-ProjectTemplate/` directory:

```
./build/BoAT-Engine/demo/demo_venachain/demo_venachain_mycontract_create_internalGen
./build/BoAT-Engine/demo/demo_venachain/demo_venachain_mycontract_create_native
./build/BoAT-Engine/demo/demo_venachain/demo_venachain_mycontract_create_pkcs
./build/BoAT-Engine/demo/demo_venachain/demo_venachain_mycontract_onetime_internalGen
./build/BoAT-Engine/demo/demo_venachain/demo_venachain_mycontract_onetime_native
./build/BoAT-Engine/demo/demo_venachain/demo_venachain_mycontract_onetime_pkcs
```
