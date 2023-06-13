## 基于 BoAT-ProjectTemplate 开发模板构建BoAT应用开发项目
`BoAT-ProjectTemplate` 仓库，是开发基于`BoAT Infra Arch`基础架构应用程序的通用开发模板。

基于`BoAT Infra Arch`基础架构的应用开发，通过三个开源仓库实现：

1.`BoAT-ProjectTemplate` : 提供编译结构构建，完成公共源码仓库选择并克隆到本地，根据选择的公用源码仓库配置相应的编译环境，修改Makefile。

2.`BoAT-SupportLayer`：是`BoAT Infra Arch`基础架构`BoAT Support Layer` 层的公共源码仓库，提供BoAT应用所需的底层支持，包括操作系统抽象层、驱动抽象层和BoAT通用组件层，为BoAT应用提供通用的底层操作接口。

3.`BoAT-Engine`：是`BoAT Infra Arch`基础架构`BoAT Engine` 层的公共源码仓库，提供BoAT应用区块链访问相关的API接口，实现BoAT应用对不同区块链的访问。

以上三个仓库与应用平台共同构成基于`BoAT Infra Arch`基础架构的开发环境，BoAT应用就在这里诞生。

以下逐步说明如何结合三个仓库在`linux-default`平台中编译出不同区块链的demo应用程序

### 开发环境准备

在Linux操作系统中构建基于`BoAT Infra Arch`基础架构的应用开发环境，需要确认在linux平台下已经完成以下依赖库和软件的安装：
1. curl
```
sudo apt install curl
```

2. python3, version >= 3.5
```
sudo apt install python3
```

3. git
```
sudo apt install git
```

### 1. clone BoAT-ProjectTemplate 仓库到本地
在 `linux` 操作系统中执行以下指令，将`BoAT-ProjectTemplate` 仓库克隆到本地：

```
git clone https://github.com/aitos-io/BoAT-ProjectTemplate.git
```
    
执行成功后，当前路径下将创建`BoAT-ProjectTemplate`目录，存放从`github`克隆的开发模板。
克隆后`BoAT-ProjectTemplate/`目录的内容如下：
```
<BoAT-ProjectTemplate>
|-- BoATLibs.conf
|-- config.py
|-- README.md
|-- README_cn.md
```
也可以将 BoAT-ProjectTemplate 仓库克隆为开发项目目录，例如:构建 `boatDevelop` 开发目录  
```
git clone https://github.com/aitos-io/BoAT-ProjectTemplate.git boatDevelop
```  
将 `BoAT-SupportLayer`` 仓库克隆 到 `boatDevelop` 目录，并在此目录中开发  

### 2. 修改 BoATLibs.conf
`BoATLibs.conf`文件用于配置当前项目中所使用的开源仓库，后续配置脚本通过读取当前文件的配置信息，克隆相应的开源仓库到本地。

`BoATLibs.conf` 文件默认包含 `BoAT-SupportLayer` 仓库，内容如下：
```
BoAT-SupportLayer  
```

在当前示例项目中，还会使用`BoAT Engine`开源仓库，所以在`BoATLibs.conf`文件中增加`BoAT-Engine`，添加后的内容如下：
```
BoAT-SupportLayer  
BoAT-Engine
```

改写`BoATLibs.conf`文件时需要注意：
```
1.一行只能写入一个仓库名称
2.仓库名称一定要正确，尤其注意大小写一致，克隆后的目录名称将和写入的名称一致，如果大小写错误，
  虽不会影响`git clone`的结果，但会造成配置脚本执行错误。
```

### 3. 运行 config.py 脚本，根据提示完成相应操作，完成编译目录构建和编译文件配置

`config.py`脚本包含两个主要执行步骤  
1. 克隆 `BoATLibs.conf` 文件中包含的仓库源码  
2. 根据 获取的源码仓库生成 `Makefile`  

在`BoAT-ProjectTemplate/`目录下执行脚本配置，执行过程中会有数次交互输入，详细过程如下：
```
python3 config.py
```

```
We will clone the BoAT-SupportLayer repository, which may take several minutes

Input the branch name or null:
```
这里直接回车，将`clone`开源仓库`BoAT-SupportLayer`的`main`分支
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
这里输入回车，将`clone`开源仓库`BoAT-Engine`的`main`分支。
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
这里输入回车，被判定为`Y：Yes`；如果你不希望重写`Makefile`，则可以输入`n`，编译配置将立即结束。
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
这里输入应用程序中需要支持的区块链，输入`9`，选择`VENACHAIN`区块链。
```
input:9
Blockchain selected:
 [9] VENACHAIN

Select the platform list as below:
[1] linux-default             : Default linux platform
[2] Fibocom-L610              : Fibocom's LTE Cat.1 module
[3] create a new platform
```
这里输入`1`，选择应用目标平台为`linux-default`，选择后脚本将自动完成Makefile的生成。
```
1
platform is : linux-default

include BoAT-SupportLayer.conf

include BoAT-Engine.conf

./BoAT-SupportLayer/demo/ False
./BoAT-Engine/demo/ True
Configuration completed
```

执行完配置后，开发目录将包含以下内容：
```
<BoAT-ProjectTemplate>
|-- <BoAT-SupportLayer>
|-- <BoAT-Engine>
|-- BoATLibs.conf
|-- config.py
|-- Makfile
|-- README.md
|-- README_en.md
```

### 5. 编译

在`BoAT-ProjectTemplate/`目录下执行编译指令：
```
make demo VENACHAIN_DEMO_IP="127.0.0.1"
```
其中`VENACHAIN_DEMO_IP="127.0.0.1"`，由开发者提供一个`VENACHAIN`访问节点的IP地址宏`VENACHAIN_DEMO_IP`，其中`"127.0.0.1"`仅是一个示例。在实际应用中，需要开发者提供正确的节点IP宏，否则`VENACHAIN`的 `demo`程序无法正确访问节点，错误的宏虽不影响编译，但会导致区块链节点访问失败。

编译过程中可能会遇到以下错误，按照给出的处理方法可解决相应问题。

常见错误错误1：
```
curlport.c:33:23: fatal error: curl/curl.h: No such file or directory
```
安装`libcurl4-gnutls-dev`依赖库：
```
sudo apt install libcurl4-gnutls-dev
```

常见错误错误2：
```
boatssl.c:26:25: fatal error: openssl/evp.h: No such file or directory
```
安装`libssl-dev`依赖库
```
sudo apt install libssl-dev
```

完成编译后`BoAT-ProjectTemplate`路径下的目录包含如下内容：
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
### 6. 编译输出目录说明：
在`BoAT-ProjectTemplate/`目录下完成编译后，新增加两个目录：

`build` 和 `lib`

`build:`

输出编译过程中产生的中间文件以及各个源码库中产生的demo的可执行文件，本例中输出了`VENACHAIN`的`demo`可执行文件
在本例中 `VENACHAIN` 的`demo`输出在`BoAT-ProjectTemplate/build/BoAT-Engine/demo/demo_venachain/`目录，包含六个可执行文件：
```
demo_venachain_mycontract_create_internalGen
demo_venachain_mycontract_create_native
demo_venachain_mycontract_create_pkcs
demo_venachain_mycontract_onetime_internalGen
demo_venachain_mycontract_onetime_native
demo_venachain_mycontract_onetime_pkcs
```

`lib：`

输出各个开源仓库生成的静态库问文件，在这个项目中生成两个静态库:

```
libboatengine.a : BoAT-Engine 静态库
libboatvendor.a ：BoAT-SupportLayer 静态库
```
### 7. 执行demo：

在`BoAT-ProjectTemplate/`目录下执行各个demo：

```
./build/BoAT-Engine/demo/demo_venachain/demo_venachain_mycontract_create_internalGen
./build/BoAT-Engine/demo/demo_venachain/demo_venachain_mycontract_create_native
./build/BoAT-Engine/demo/demo_venachain/demo_venachain_mycontract_create_pkcs
./build/BoAT-Engine/demo/demo_venachain/demo_venachain_mycontract_onetime_internalGen
./build/BoAT-Engine/demo/demo_venachain/demo_venachain_mycontract_onetime_native
./build/BoAT-Engine/demo/demo_venachain/demo_venachain_mycontract_onetime_pkcs
```

