## 基于 BoAT-ProjectTemplate 开发模板构建项目开发目录步骤说明

### 1. clone BoAT-ProjectTemplate 仓库到本地
可以直接 clone BoAT-ProjectTemplate 仓库为开发目录  
例如：  
    构建 BoAT-SupportLayer 开发目录  
    ```
    git clone -b dev git@github.com:aitos-io/BoAT-ProjectTemplate.git boatSupportLayerDevelop
    ```  
    将 BoAT-SupportLayer 仓库 clone 到 boatSupportLayerDevelop 目录，并在此目录中开发  

### 2. 修改 BoATLibs.conf
BoATLibs.conf 文件中已经包含 BoAT-SupportLayer 仓库，可根据开发需要按格式添加项目中使用的 BoATInfraArch 相应仓库名称  
例如：  
    BoAT-SupportLayer  
注意一行只能写入一个仓库名称  
至少要保留 BoAT-SupportLayer 仓库

### 3. 创建应用项目代码目录：(可选)
1. 在 GitHub 上创建应用项目源码仓库，并包含一个基础 Makefile 文件  
2. 修改 BoATLibs.conf 文件，将应用项目源码仓库名添加到 BoATLibs.conf 文件中  
例如：  
    BoAT-SupportLayer  
    xxxApp  
        
### 4. 运行 config.py 脚本，根据提示完成相应操作，完成开发目录构建
脚本包含两个主要执行步骤  
1. 获取 BoATLibs.conf 文件中包含的仓库源码  
2. 根据 获取的源码仓库生成 Makefile  
过程中会有数次交互输入，详细过程参见 6. 实例操作说明   

### 5. 在不同平台构建项目开发目录位置说明 
1. Fibocom-L610：在 Fibocom-L610 sdk 开发环境的顶层目录下构建项目开发目录，即在 sdk 目录下按上述1~4操作执行， clone BoAT-ProjectTemplate 到本地进行开发  
2. linux: 在任意自选位置构建项目开发目录，进入开发目录按上述1~4操作执行， clone BoAT-ProjectTemplate 到本地进行开发  
    
### 6. 实例操作说明
在 Fibocom-L610 oepnCPU 开发环境下构建 smApp 项目过程
1. 前提条件
    1. 在 Linux 操作系统中包含 Fibocom-L610 oepnCPU sdk 目录，假设目录名为 core-sdk-1.0/
    2. 在 Linux 操作系统中完成 git 安装
    3. 在 Linux 操作系统中安装 python3, version >= 3.5
    4. 在 Linux 操作系统中完成 GitHub 账号配置
    5. 在 Linux 操作系统中能正常拉取 GitHub 远程仓库
    6. 在 GitHub 上已经创建了 smApp 项目仓库
        smApp 仓库至少包含一个基础 Makefile 文件，文件内容可以为：
        all:
            @echo 'this is smApp project' 

        如果没有 Makefile 文件会导致编译时产生：recipe for target 'smApp' failed 错误

2. 在 Linux 操作系统下打开Terminal终端，进入 core-sdk-1.0/目录,在目录下执行命令：
    注意，目前使用 BoAT-ProjectTemplate 仓库的 dev 分支，在 clone 时要配置 -b dev  
    ```
    $ git clone -b dev git@github.com:aitos-io/BoAT-ProjectTemplate.git boatSmAppDevelop
        Cloning into 'boatSmAppDevelop'...
        remote: Enumerating objects: 16, done.
        remote: Counting objects: 100% (16/16), done.
        remote: Compressing objects: 100% (9/9), done.
        remote: Total 16 (delta 4), reused 11 (delta 2), pack-reused 0
        Unpacking objects: 100% (16/16), done.
        Checking connectivity... done.
    ```
    将BoAT-ProjectTemplate clone 到 boatSmAppDevelop/目录

3. clone 成功后，进入 core-sdk-1.0/boatSmAppDevelop/目录，目录下包含如下文件：
    ```
    core-sdk-1.0/
    |
    +---boatSmAppDevelop/
    |---BoATLibs.conf
    |---config.py
    ```
4. 根据项目需要的 BoATInfraArch 仓库，修改 BoATLibs.conf，假设smApp 仅需要 BoAT-SupportLayer 库
   1. 由于BoATLibs.conf文件默认包含BoAT-SupportLayer 库，则不需要在BoATLibs.conf文件中增加其他
   BoATInfraArch 仓库（目前只提供 BoAT-SupportLayer 仓库）。
   2. 在 BoATLibs.conf 文件中增加 smApp项目的 GitHub 仓库名，用于执行 config.py clone smApp 仓库到本地。
   查看 BoATLibs.conf 修改后的内容如下：
    ```
    $ cat BoATLibs.conf 
    BoAT-SupportLayer
    smApp
    ```
5. 运行 config.py 脚本，Linux 操作系统下运行 python 脚本指令如下：
    注意，脚本执行过程中会包含几次输入交互帮助脚本完成选择。
    ```
    $ python3 config.py 

        We will clone the BoAT-SupportLayer repository, which may take several minutes

        Input the branch name or null:
    ```
    1.仓库分支输入交互：
        脚本在这里等待输入 clone BoAT-SupportLayer 仓库的分支名称或 tag 名称，
        将 BoAT-SupportLayer 仓库 clone 到 core-sdk-1.0/boatSmAppDevelop/BoAT-SupportLayer/ 目录
        目前我们选用 dev 分支进行开发，输入:dev回车,
        ```
        Input the branch name or null:dev
        branch name is [ -b dev]

        git clone -b dev https://github.com/aitos-io/BoAT-SupportLayer.git

        Cloning into 'BoAT-SupportLayer'...
        remote: Enumerating objects: 614, done.
        remote: Counting objects: 100% (614/614), done.
        remote: Compressing objects: 100% (394/394), done.
        remote: Total 614 (delta 229), reused 581 (delta 199), pack-reused 0
        Receiving objects: 100% (614/614), 992.55 KiB | 987.00 KiB/s, done.
        Resolving deltas: 100% (229/229), done.
        Checking connectivity... done.
        git cmd succ

        We will clone the smApp repository, which may take several minutes

        Input the branch name or null:
        ```
    2.仓库分支输入交互：
        脚本在这里等待输入clone smApp 仓库的分支名称或tag名称，
        将 smApp 源码仓库 clone 到 core-sdk-1.0/boatSmAppDevelop/smApp/ 目录.
        假设我们选用 master 分支进行开发，输入:回车,
        ```
        Input the branch name or null:
        branch name is []

        git clone https://github.com/aitos-io/smApp.git

        Cloning into 'smApp'...
        remote: Enumerating objects: 4, done.
        remote: Counting objects: 100% (4/4), done.
        remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
        Unpacking objects: 100% (4/4), done.
        Checking connectivity... done.
        git cmd succ

        overwrite the Makefile?(Y/n):
        ```
    3. 重写 Makefile 交互：
        完成全部仓库 clone 后，脚本提示是否重写 Makefile，在第一次运行脚本时必须选择 Y 生成    Makefile,否则无法执行编译
        后续再次执行脚本可根据需求选择 Y 或 N
        直接输入回车，默认选择 Y
        这里直接输入:回车

        重写Makefile 将会把 BoAT-SupportLayer 和 smApp 相关编译信息添加到 Makefile 中
        执行完 config.py 脚本后，可直接编译
        ```
        overwrite the Makefile?(Y/n):
        Yes

        Choose the platform list as below:
        [1] linux-default             : Default linux platform
        [2] Fibocom-L610              : Fibocom's LTE Cat.1 module
        [3] create a new platform
        ```
    4. 选择 platform 交互：
        交互中提供了当前 BoAT-SupportLayer 库支持的 platform 进行选择。
        [3] create a new platform 功能只做提示没有实现，后续完善该功能。
        在这里输入:2，选择 Fibocom-L610 platform                        
        ```
        Choose the platform list as below:
        [1] linux-default             : Default linux platform
        [2] Fibocom-L610              : Fibocom's LTE Cat.1 module
        [3] create a new platform
        2
        platform is : Fibocom-L610

        include BoAT-SupportLayer.conf

        File 'smApp/include/smApp.conf' is not exist

        Configuration completed
        ```
    自此脚本运行结束，完成 BoAT-SupportLayer 和 smApp 源码拉取，并重写 Makefile
    注意，"File 'smApp/include/smApp.conf' is not exist"，这是因为 smApp 目录中没有提供相应的文件，不影响 Makefile 生成及后续编译

    完整的脚本执行过程如下：
    ```
    $ python3 config.py

        We will clone the BoAT-SupportLayer repository, which may take several minutes

        Input the branch name or null:dev
        branch name is [ -b dev]

        git clone -b dev https://github.com/aitos-io/BoAT-SupportLayer.git

        Cloning into 'BoAT-SupportLayer'...
        remote: Enumerating objects: 614, done.
        remote: Counting objects: 100% (614/614), done.
        remote: Compressing objects: 100% (394/394), done.
        remote: Total 614 (delta 229), reused 581 (delta 199), pack-reused 0
        Receiving objects: 100% (614/614), 992.55 KiB | 987.00 KiB/s, done.
        Resolving deltas: 100% (229/229), done.
        Checking connectivity... done.
        git cmd succ

        We will clone the smApp repository, which may take several minutes

        Input the branch name or null:
        branch name is []

        git clone https://github.com/aitos-io/smApp.git

        Cloning into 'smApp'...
        remote: Enumerating objects: 4, done.
        remote: Counting objects: 100% (4/4), done.
        remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
        Unpacking objects: 100% (4/4), done.
        Checking connectivity... done.
        git cmd succ

        overwrite the Makefile?(Y/n):
        Yes

        Choose the platform list as below:
        [1] linux-default             : Default linux platform
        [2] Fibocom-L610              : Fibocom's LTE Cat.1 module
        [3] create a new platform
        2
        platform is : Fibocom-L610

        include BoAT-SupportLayer.conf

        File 'smApp/include/smApp.conf' is not exist

        Configuration completed
    ```

    脚本执行完后的目录结构如下：
    ```
    core-sdk-1.0/
    |
    +---boatSmAppDevelop/
    |
    +---BoAT-SupportLayer/
    |    |
    |    +---include/
    |    ...
    |    |---Makefile
    |
    +---smApp/
    |    |---Makefile
    |
    |---BoATLibs.conf
    |---config.py
    |---Makefile
    ```
    在 core-sdk-1.0/boatSmAppDevelop/目录下执行 make 即可完成 BoAT-SupportLayer 和 smApp 编译

6. 代码提交注意：
    1. core-sdk-1.0/boatSmAppDevelop/ 目录下运行 configi.py 后会禁能在目录下使用 git 操作，防止向 github.com:aitos-io/BoAT-ProjectTemplate.git 仓库执行错误的提交。
    2. 各个 BoATInfraArch 仓库和应用项目仓库的提交在相应的目录下进行
       例如：
        1. BoAT-SupportLayer 仓库修改后的提交在 core-sdk-1.0/boatSmAppDevelop/BoAT-SupportLayer/ 目录下执行：
            ```
            git add .
            git commit
            git push
            ```
        2. smApp 项目文件更改后的提交在 core-sdk-1.0/boatSmAppDevelop/smApp/ 目录中执行 git 相关操作。
