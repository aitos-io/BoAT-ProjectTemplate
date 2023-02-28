#!/usr/bin/python


# Copyright (C) 2018-2021 aitos.io
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# This python script generates configure macros of specific platform.


import sys
import os.path
import string
import shutil

#from git import Repo
import os
#from git.repo import Repo

import subprocess
#from goto import with_goto




# rorepo is a Repo instance pointing to the git-python repository.
# For all you know, the first argument to Repo is a path to the repository
# you want to work with


license =  '/******************************************************************************\n' + \
 '* Copyright (C) 2018-2021 aitos.io\n'                                                        + \
 '*\n'                                                                                         + \
 '* Licensed under the Apache License, Version 2.0 (the "License");\n'                         + \
 '* you may not use this file except in compliance with the License.\n'                        + \
 '* You may obtain a copy of the License at\n'                                                 + \
 '*\n'                                                                                         + \
 '*     http://www.apache.org/licenses/LICENSE-2.0\n'                                          + \
 '*\n'                                                                                         + \
 '* Unless required by applicable law or agreed to in writing, software\n'                     + \
 '* distributed under the License is distributed on an "AS IS" BASIS,\n'                       + \
 '* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n'                + \
 '* See the License for the specific language governing permissions and\n'                     + \
 '* limitations under the License.\n'                                                          + \
 '*****************************************************************************/\n'            + \
'\n\n'

infoBoatSupportLayer = 'We will clone/pull the BoATSupportLayer repository!\n'

infoBoatEngine = 'Clone/pull the BoATEnigne repository, y/n?(y)'

infoBlockchain = ' Select blockchain list as below:\n' + \
        ' [1] ETHEREUM          : \n' + \
        ' [2] PLATON            : \n' + \
        ' [3] PLATONE           : \n' + \
        ' [4] FISCOBCOS         : \n' + \
        ' [5] HLFABRIC          : \n' + \
        ' [6] HWBCS             : \n' + \
        ' [7] CHAINMAKER_V1     : \n' + \
        ' [8] CHAINMAKER_V2     : \n' + \
        ' [9] VENACHAIN         : \n' + \
        ' [a] QUORUM            : \n' + \
        ' [b] CITA              : \n' + \
        ' [0] All block chains\n' 

infoBlockchainExample = ' Example:\n' + \
            '  Select blockchain list as below:\n' + \
            '  input:1a\n' + \
            '  Blockchain selected:\n' + \
            '   [1] ETHEREUM\n' + \
            '   [a] QUORUM\n\n'

'''
exportBlockchain = 'export BOAT_PROTOCOL_USE_ETHEREUM\n' + \ 
                   'export BOAT_PROTOCOL_USE_PLATON\n' + \
                   'export BOAT_PROTOCOL_USE_PLATONE\n' + \
                   'export BOAT_PROTOCOL_USE_FISCOBCOS\n' + \
                   'export BOAT_PROTOCOL_USE_HLFABRIC\n' + \
                   'export BOAT_PROTOCOL_USE_HWBCS\n' + \
                   'export BOAT_PROTOCOL_USE_CHAINMAKER_V1\n' + \
                   'export BOAT_PROTOCOL_USE_CHAINMAKER_V2\n' + \
                   'export BOAT_PROTOCOL_USE_VENACHAIN\n' + \
                   'export BOAT_PROTOCOL_USE_QUORUM\n' + \
                   'export BOAT_PROTOCOL_USE_CITA\n' + \
                   'export BOAT_DISCOVERY_PEER_QUERY\n' + \
                   'export BOAT_USE_DEFAULT_CJSON\n'
'''

class ConfigContentGen():
    def __init__(self):
        self.config_content = ''
        self.usinglibs = ''
        self.exportblockchain = ''

    def save_config_file(self):
            #config_file_name = './vendor/platform/include/boatconfig.h'
            config_file_name = './Makefile'
            #config_file_name = './boatconfig.h'
            with open(config_file_name, 'w') as config_file_handle:
                config_file_handle.write(self.config_content)
    
    def gen_config_content(self):
        self.config_content += '\n'
        self.config_content += '#define  RPC_USE_LIBCURL     1'
        self.config_content += '\n'

    def gen_config_tips(self, platform):
        self.config_content +=license
        self.config_content += \
            '/****************************************************************************\n' +\
            ' THIS FILE IS AUTO GENERATED FOR SPECIAL PLATFORM ' + platform + '\n'            +\
            ' DO NOT MODIFY THIS FILE MANUALLY\n'                                             +\
            ' ****************************************************************************/\n\n' 
    
    def gen_condHead(self):  
        self.config_content += '#ifndef __BOATCONFIG_H__\n'
        self.config_content += '#define __BOATCONFIG_H__\n'
        self.config_content += '\n\n'

    def gen_condTail(self):  
        self.config_content += '\n\n'
        self.config_content += '#endif\n'

    # head
    def gen_Head(self):  
        self.config_content += '# Directories\n'
        self.config_content += 'BOAT_BASE_DIR  := $(CURDIR)\n'
        self.config_content += 'BOAT_LIB_DIR   := $(BOAT_BASE_DIR)/lib\n'
        self.config_content += 'BOAT_BUILD_DIR := $(BOAT_BASE_DIR)/build\n'
        self.config_content += '\n\n'
    
    # blockchain
    def gen_blockchain(self,pf):  
        self.config_content += '# Blockchains:\n'
        self.config_content += pf +'\n\n'
        self.config_content += '# Chain config check\n'
        self.config_content += 'ifeq ($(BOAT_PROTOCOL_USE_ETHEREUM)_$(BOAT_PROTOCOL_USE_PLATON)_$(BOAT_PROTOCOL_USE_PLATONE)_$(BOAT_PROTOCOL_USE_FISCOBCOS)_$(BOAT_PROTOCOL_USE_HLFABRIC)_$(BOAT_PROTOCOL_USE_HWBCS)_$(BOAT_PROTOCOL_USE_CHAINMAKER_V1)_$(BOAT_PROTOCOL_USE_CHAINMAKER_V2)_$(BOAT_PROTOCOL_USE_VENACHAIN)_$(BOAT_PROTOCOL_USE_QUORUM)_$(BOAT_PROTOCOL_USE_CITA), 0_0_0_0_0_0_0_0_0_0_0)\n'
        self.config_content += '    $(error Select at least one chain)\n'
        self.config_content += 'endif\n'
        self.config_content += '\n'
        self.config_content += 'ifeq ($(BOAT_PROTOCOL_USE_CHAINMAKER_V1)_$(BOAT_PROTOCOL_USE_CHAINMAKER_V2), 1_1)\n'
        self.config_content += '    $(error Select only one chainmaker version)\n'
        self.config_content += 'endif\n'

    # platform
    def gen_platform(self,pf):  
        self.config_content += '# Platform target\n'
        self.config_content += '# The valid option value of PLATFORM_TARGET list as below:\n'
        self.config_content += '# - linux-default             : Default linux platform\n'
        self.config_content += '# - Fibocom-L610              : Fibocom\'s LTE Cat.1 module\n'
        self.config_content += 'PLATFORM_TARGET ?= ' + pf +'\n'
        self.config_content += '\n'
    # env
    def gen_env(self):
        self.config_content += '# Environment-specific Settings\n'
        self.config_content += 'include $(BOAT_BASE_DIR)/BoAT-SupportLayer/platform/$(PLATFORM_TARGET)/external.env\n'
        self.config_content += '\n\n'
    
    # gcc version
    def gen_gccversion(self):
        self.config_content += '# Check gcc version\n'
        self.config_content += 'ifneq (,$(CC))\n'
        self.config_content += '    GCCVERSION := $(shell $(CC) -v 2>&1)\n'
        self.config_content += 'else\n'
        self.config_content += '    GCCVERSION := "NONE"\n'
        self.config_content += 'endif\n'
        self.config_content += '\n'
        self.config_content += 'ifneq (,$(findstring arm,$(GCCVERSION)))         # Target: arm-oe-linux-gnueabi\n'
        self.config_content += '    COMPILER_TYPE = "ARM"\n'
        self.config_content += 'else ifneq (,$(findstring linux,$(GCCVERSION)))  # Target: x86_64-redhat-linux\n'
        self.config_content += '    COMPILER_TYPE = "LINUX"\n'
        self.config_content += 'else ifneq (,$(findstring cygwin,$(GCCVERSION))) # Target: x86_64-pc-cygwin\n'
        self.config_content += '    COMPILER_TYPE = "CYGWIN"\n'
        self.config_content += 'else\n'
        self.config_content += '    COMPILER_TYPE = "NOTSUPPORT"                 # Not supported\n'
        self.config_content += 'endif\n'
        self.config_content += '\n'
        self.config_content += '\n'
        self.config_content += '# Environment Language\n'
        self.config_content += 'LANG := en_US  # zh_CN.UTF-8\n'
        self.config_content += '\n'
    
    # include path
    def gen_includepath(self):
        self.config_content += '# Compiling Flags\n'
        self.config_content += '\n'
        self.config_content += '# Target-independent Flags\n'
        self.config_content += 'BOAT_INCLUDE := $(EXTERNAL_INC)\n'
        self.config_content += '\n'
        # libs 
        for curlib in self.usinglibs.split("\n"):
            #curlib = line.decode()
            if curlib == '':
                continue
            #print('file :' + '$(BOAT_BASE_DIR)/' + curlib + '/include/'+curlib+'.conf')
            isExists = os.path.exists('./' + curlib + '/include/'+curlib+'.conf')
            if isExists: 
                print('include '+curlib+'.conf\n')
                self.config_content += 'include $(BOAT_BASE_DIR)/' + curlib + '/include/'+curlib+'.conf\n'
            else:
                print('File \'' + curlib + '/include/'+curlib+'.conf\' is not exist\n')
        
    
    # other Flags
    def gen_otherFlags(self):
        self.config_content += 'BOAT_CSTD_FLAGS := -std=gnu99\n'
        self.config_content += '#BOAT_OPTIMIZATION_FLAGS := -g #-Os \n'
        self.config_content += 'BOAT_OPTIMIZATION_FLAGS := -Os\n'
        self.config_content += 'BOAT_WARNING_FLAGS := -Wall\n'
        self.config_content += 'BOAT_DEFINED_MACROS := #-DDEBUG_LOG\n'
        self.config_content += '\n'
        self.config_content += '# BOAT_COMMON_LINK_FLAGS := -Wl,-Map,$(BOAT_BUILD_DIR)/boat.map\n'
        self.config_content += '\n'
        self.config_content += '\n'
        self.config_content += '# Target-specific Flags\n'
        self.config_content += 'ifeq ($(COMPILER_TYPE), "ARM")\n'
        self.config_content += '    TARGET_SPEC_CFLAGS := -mthumb -ffunction-sections -fdata-sections\n'
        self.config_content += '    TARGET_SPEC_LIBS := \n'
        self.config_content += '    TARGET_SPEC_LINK_FLAGS :=\n'
        self.config_content += 'else ifeq ($(COMPILER_TYPE), "LINUX")\n'
        self.config_content += '    TARGET_SPEC_CFLAGS := -ffunction-sections -fdata-sections \n'
        self.config_content += '    TARGET_SPEC_LIBS := \n'
        self.config_content += '    TARGET_SPEC_LINK_FLAGS := -Wl,-gc-sections\n'
        self.config_content += 'else ifeq ($(COMPILER_TYPE), "CYGWIN")\n'
        self.config_content += '    TARGET_SPEC_CFLAGS :=\n'
        self.config_content += '    TARGET_SPEC_LIBS := \n'
        self.config_content += '    TARGET_SPEC_LINK_FLAGS :=\n'
        self.config_content += 'else\n'
        self.config_content += '    TARGET_SPEC_CFLAGS :=\n'
        self.config_content += '    TARGET_SPEC_LIBS :=\n'
        self.config_content += '    TARGET_SPEC_LINK_FLAGS :=\n'
        self.config_content += 'endif\n'
        self.config_content += '\n'           
    
    # crypto
    def gen_crypto(self):
        self.config_content += '# Soft-crypto Dependencies\n'
        self.config_content += '# The valid option value of SOFT_CRYPTO list as below:\n'
        self.config_content += '# - CRYPTO_DEFAULT      : default soft crypto algorithm\n'
        self.config_content += '# - CRYPTO_MBEDTLS      : mbedtls crypto algorithm\n'
        self.config_content += '# SOFT_CRYPTO ?= CRYPTO_MBEDTLS\n'
        #self.config_content += '\n'
        #self.config_content += 'SOFT_CRYPTO ?= CRYPTO_DEFAULT\n'
        #self.config_content += '# ifeq ($(PLATFORM_TARGET), linux-default)\n'
        #self.config_content += '#     SOFT_CRYPTO ?= CRYPTO_DEFAULT\n'
        #self.config_content += '# else ifeq ($(PLATFORM_TARGET), mobiletek-L503C-6S) \n'
        #self.config_content += '#     SOFT_CRYPTO ?= CRYPTO_DEFAULT\n'
        #self.config_content += '# else\n'
        #self.config_content += '#     $(error not support this platform : $(PLATFORM_TARGET))\n'
        #self.config_content += '# endif\n'
        #self.config_content += '\n'
        #self.config_content += '\n'
        #self.config_content += 'ifeq ($(SOFT_CRYPTO), CRYPTO_DEFAULT)\n'
        #self.config_content += '    BOAT_INCLUDE += -I$(BOAT_BASE_DIR)/BoAT-SupportLayer/crypto/crypto_default \\\n'
        #self.config_content += '	                -I$(BOAT_BASE_DIR)/BoAT-SupportLayer/crypto/crypto_default/aes \\\n'
        #self.config_content += '                    -I$(BOAT_BASE_DIR)/BoAT-SupportLayer/storage\n'
        #self.config_content += 'else\n'
        #self.config_content += '    BOAT_INCLUDE +=\n'
        #self.config_content += 'endif\n'
        #self.config_content += '\n'
    
    # cJSON
    def gen_cJSON(self):
        self.config_content += '# cJSON Dependencies\n'
        self.config_content += '#\n'
        self.config_content += '# - CJSON_DEFAULT : default cJSON library\n'
        self.config_content += '# - CJSON_OUTTER  : externally provided by users\n'
        #self.config_content += 'CJSON_LIBRARY ?= CJSON_DEFAULT\n'
        #self.config_content += '\n'
        #self.config_content += 'ifeq ($(CJSON_LIBRARY), CJSON_DEFAULT)\n'
        #self.config_content += '    BOAT_INCLUDE += -I$(BOAT_BASE_DIR)/sdk/third-party/cJSON\n'
        #self.config_content += 'endif\n'
        #self.config_content += '\n'
    
    # Combine FLAGS
    def gen_CombineFLAGS(self):
        self.config_content += 'ifeq ($(BOAT_TEST), TEST_MODE)\n'
        self.config_content += 'BOAT_TEST_FLAG = -fprofile-arcs\\\n'
        self.config_content += '                 -ftest-coverage\n'
        self.config_content += '\n'
        self.config_content += 'ifeq ($(BOAT_NODES_DISCOVER), OPEN)\n'
        self.config_content += 'BOAT_DISCOVERY_PEER_QUERY    = 1\n'
        self.config_content += 'else\n'
        self.config_content += 'BOAT_DISCOVERY_PEER_QUERY    = 0\n'
        self.config_content += 'endif\n'
        self.config_content += 'endif\n'
        self.config_content += '\n\n'
        self.config_content += '# Combine FLAGS\n'
        self.config_content += 'BOAT_CFLAGS := $(TARGET_SPEC_CFLAGS) \\\n'
        self.config_content += '               $(BOAT_INCLUDE) \\\n'
        self.config_content += '               $(BOAT_CSTD_FLAGS) \\\n'
        self.config_content += '               $(BOAT_OPTIMIZATION_FLAGS) \\\n'
        self.config_content += '               $(BOAT_WARNING_FLAGS) \\\n'
        self.config_content += '               $(BOAT_DEFINED_MACROS) \\\n'
        self.config_content += '               $(EXTERNAL_CFLAGS) \\\n'
        self.config_content += '               $(BOAT_TEST_FLAG) \\\n'
        self.config_content += '               $(BOAT_CHAINMAKER_VERSION_CFLAGS)\n'
        self.config_content += '\n'
        self.config_content += 'BOAT_LFLAGS := $(BOAT_COMMON_LINK_FLAGS) $(TARGET_SPEC_LINK_FLAGS) $(EXTERNAL_LFLAGS)\n'
        self.config_content += 'LINK_LIBS := $(EXTERNAL_LIBS) $(TARGET_SPEC_LIBS)\n'
        self.config_content += '\n'

    # export
    def gen_export(self):

        if self.usinglibs.find('BoAT-Engine') != -1:
            self.config_content += 'export BOAT_PROTOCOL_USE_ETHEREUM\n'
            self.config_content += 'export BOAT_PROTOCOL_USE_PLATON\n'
            self.config_content += 'export BOAT_PROTOCOL_USE_PLATONE\n'
            self.config_content += 'export BOAT_PROTOCOL_USE_FISCOBCOS\n'
            self.config_content += 'export BOAT_PROTOCOL_USE_HLFABRIC\n'
            self.config_content += 'export BOAT_PROTOCOL_USE_HWBCS\n'
            self.config_content += 'export BOAT_PROTOCOL_USE_CHAINMAKER_V1\n'
            self.config_content += 'export BOAT_PROTOCOL_USE_CHAINMAKER_V2\n'
            self.config_content += 'export BOAT_PROTOCOL_USE_VENACHAIN\n'
            self.config_content += 'export BOAT_PROTOCOL_USE_QUORUM\n'
            self.config_content += 'export BOAT_PROTOCOL_USE_CITA\n\n'
            #self.config_content += exportBlockchain
        
        self.config_content += 'export BOAT_DISCOVERY_PEER_QUERY\n'
        self.config_content += 'export BOAT_USE_DEFAULT_CJSON\n'
        self.config_content += '\n'
        self.config_content += '\n'
        self.config_content += 'export SOFT_CRYPTO\n'
        self.config_content += 'export CJSON_LIBRARY\n'
        self.config_content += 'export PLATFORM_TARGET\n'
        self.config_content += 'export BOAT_BASE_DIR\n'
        self.config_content += 'export BOAT_LIB_DIR\n'
        self.config_content += 'export BOAT_BUILD_DIR\n'
        self.config_content += 'export BOAT_CFLAGS\n'
        self.config_content += 'export BOAT_LFLAGS\n'
        self.config_content += 'export LINK_LIBS\n'
        self.config_content += '\n'
    
    # .PHONY
    def gen_PHONY(self):
        self.config_content += '.PHONY: all' #all boatlibs createdir boatwalletlib vendorlib demo tests clean cleanboatwallet cleanvendor cleantests\n'
        for addobj in self.usinglibs.split("\n"):
            #curlib = line.decode()
            if addobj == '':
                continue
            #print('target: '+addobj+':\n')
            self.config_content += ' ' + addobj+'_obj'
            self.config_content += ' clean' + addobj
        self.config_content += '\n'
    
    # all:
    def gen_all(self):
        self.config_content += '#all:\n'
        self.config_content += 'all: createdir'
        for addobj in self.usinglibs.split("\n"):
            #curlib = line.decode()
            if addobj == '':
                continue
            #print('target: '+addobj+':\n')
            self.config_content += ' ' + addobj+'_obj'
        self.config_content += '\n\n'
    
    # gen.py
    def gen_genpy(self):  

        self.config_content += '\n\n'
    
    # targets
    def gen_targets(self):
        
        for addobj in self.usinglibs.split("\n"):
            #curlib = line.decode()
            if addobj == '':
                continue
            #print('target: '+addobj+':\n')
            self.config_content += addobj+'_obj:\n'
            self.config_content += '	make -C $(BOAT_BASE_DIR)/'+addobj+' all\n'
            self.config_content += '\n'
        self.config_content += '\n'        
    
        self.config_content += 'createdir:\n'
        self.config_content += '#	@echo generate header file boatconfig.h...\n'
        self.config_content += '#	python ./vendor/platform/$(PLATFORM_TARGET)/scripts/gen.py $(PLATFORM_TARGET) $(SCRIPTS_PARAM)\n'
        self.config_content += '#	@echo generate done.\n'
        self.config_content += '# boatconfig is no longer used\n'
        self.config_content += '	$(BOAT_MKDIR) -p $(BOAT_LIB_DIR)\n'
        self.config_content += '	$(BOAT_MKDIR) -p $(BOAT_BUILD_DIR)\n'
        self.config_content += '\n'
        self.config_content += 'boatwalletlib:\n'
        self.config_content += '	make -C $(BOAT_BASE_DIR)/sdk all\n'
        self.config_content += '\n'
        self.config_content += 'vendorlib:\n'
        self.config_content += '	make -C $(BOAT_BASE_DIR)/BoAT-SupportLayer all\n'
        self.config_content += '\n'
        self.config_content += 'demo: boatlibs\n'
        self.config_content += '	make -C $(BOAT_BASE_DIR)/demo all\n'
        self.config_content += '\n'
        self.config_content += 'rulecheck: \n'
        self.config_content += '	cppcheck  --enable=all -i$(BOAT_BASE_DIR)/sdk/third-party/ -i$(BOAT_BASE_DIR)/BoAT-SupportLayer/vendor/crypto/  -i$(BOAT_BASE_DIR)/sdk/protocol/boathlfabric/protos  --force $(BOAT_BASE_DIR) \n'
        self.config_content += '\n'
        self.config_content += 'tests: boatlibs\n'
        self.config_content += '	make -C $(BOAT_BASE_DIR)/tests all\n'
        self.config_content += '\n'
    
    # clean:
    def gen_clean(self):
        self.config_content += 'clean:' # cleanboatwallet cleanvendor cleandemo cleantests\n'
        for addobj in self.usinglibs.split("\n"):
            #curlib = line.decode()
            if addobj == '':
                continue
            #print('target: '+addobj+':\n')
            self.config_content += ' clean' + addobj
        self.config_content += '\n'
        self.config_content += '	-$(BOAT_RM) $(BOAT_BUILD_DIR)\n'
        self.config_content += '\n'
        
    # targets clean
    def gen_targetsclean(self):
        for addobj in self.usinglibs.split("\n"):
            #curlib = line.decode()
            if addobj == '':
                continue
            #print('target: '+addobj+':\n')
            self.config_content += 'clean'+addobj+':\n'
            self.config_content += '	make -C $(BOAT_BASE_DIR)/'+addobj+' clean\n'
            self.config_content += '\n'

    
        self.config_content += 'cleanboatwallet:\n'
        self.config_content += '	make -C $(BOAT_BASE_DIR)/sdk clean\n'
        self.config_content += '\n'
        self.config_content += 'cleanvendor:\n'
        self.config_content += '	make -C $(BOAT_BASE_DIR)/BoAT-SupportLayer clean\n'
        self.config_content += '\n'
        self.config_content += 'cleandemo:\n'
        self.config_content += '	make -C $(BOAT_BASE_DIR)/demo clean\n'
        self.config_content += '\n'
        self.config_content += 'cleantests:\n'
        self.config_content += '	make -C $(BOAT_BASE_DIR)/tests clean\n'

    def getEnterAsYes(self,content):
        yon = input(content+'(Y/n):')
        if (yon == '' ):
            print("Yes\n")
            return True
        elif ((yon == 'y') or (yon == 'Y')):
            print('Yes\n')
            return True
        elif ((yon == 'n') or (yon == 'N')):
            print('No\n')
            return False
        else:
            print('No\n')
            return False
        
    def getEnterAsNo(self,content):
        yon = input(content+'(N/y):')
        if (yon == '' ):
            print("No\n")
            return False
        elif ((yon == 'y') or (yon == 'Y')):
            print('Yes\n')
            return True
        elif ((yon == 'n') or (yon == 'N')):
            print('No\n')
            return False
        else:
            print('No\n')
            return False

    def selectblockchain(self):
        ppf = infoBlockchain + \
              infoBlockchainExample + \
              'input:'

        chos = input(ppf)
        retBlockchain = ''
        
        blockchainSelected = ''
        blockchainShow = ''

        if chos.find('0') != -1:
            blockchainShow = ('Select all blockchains!\n')
            chos = infoBlockchain
        else:
            blockchainShow = 'Blockchain selected:\n'
            
        
        if chos.find('1') != -1:
            blockchainSelected += (' [1] ETHEREUM\n')
            retBlockchain += 'BOAT_PROTOCOL_USE_ETHEREUM           ?= 1\n'
        else:
            retBlockchain += 'BOAT_PROTOCOL_USE_ETHEREUM           ?= 0\n'

        if chos.find('2') != -1:
            blockchainSelected += (' [2] PLATON\n')
            retBlockchain += 'BOAT_PROTOCOL_USE_PLATON             ?= 1\n'
        else:
            retBlockchain += 'BOAT_PROTOCOL_USE_PLATON             ?= 0\n'

        if chos.find('3') != -1:
            blockchainSelected += (' [3] PLATONE\n')
            retBlockchain += 'BOAT_PROTOCOL_USE_PLATONE            ?= 1\n'
        else:
            retBlockchain += 'BOAT_PROTOCOL_USE_PLATONE            ?= 0\n'

        if chos.find('4') != -1:
            blockchainSelected += (' [4] FISCOBCOS\n')
            retBlockchain += 'BOAT_PROTOCOL_USE_FISCOBCOS          ?= 1\n'
        else:
            retBlockchain += 'BOAT_PROTOCOL_USE_FISCOBCOS          ?= 0\n'

        if chos.find('5') != -1:
            blockchainSelected += (' [5] HLFABRIC\n')
            retBlockchain += 'BOAT_PROTOCOL_USE_HLFABRIC           ?= 1\n'
        else:
            retBlockchain += 'BOAT_PROTOCOL_USE_HLFABRIC           ?= 0\n'

        if chos.find('6') != -1:
            blockchainSelected += (' [6] HWBCS\n')
            retBlockchain += 'BOAT_PROTOCOL_USE_HWBCS              ?= 1\n'
        else:
            retBlockchain += 'BOAT_PROTOCOL_USE_HWBCS              ?= 0\n'

        if chos.find('7') != -1:
            blockchainSelected += (' [7] CHAINMAKER_V1\n')
            retBlockchain += 'BOAT_PROTOCOL_USE_CHAINMAKER_V1      ?= 1\n'
        else:
            retBlockchain += 'BOAT_PROTOCOL_USE_CHAINMAKER_V1      ?= 0\n'

        if chos.find('8') != -1:
            blockchainSelected += (' [8] CHAINMAKER_V2\n')
            retBlockchain += 'BOAT_PROTOCOL_USE_CHAINMAKER_V2      ?= 1\n'
        else:
            retBlockchain += 'BOAT_PROTOCOL_USE_CHAINMAKER_V2      ?= 0\n'

        if chos.find('9') != -1:
            blockchainSelected += (' [9] VENACHAIN\n')
            retBlockchain += 'BOAT_PROTOCOL_USE_VENACHAIN          ?= 1\n'
        else:
            retBlockchain += 'BOAT_PROTOCOL_USE_VENACHAIN          ?= 0\n'

        if chos.find('a') != -1:
            blockchainSelected += (' [a] QUORUM\n')
            retBlockchain += 'BOAT_PROTOCOL_USE_QUORUM             ?= 1\n'
        else:
            retBlockchain += 'BOAT_PROTOCOL_USE_QUORUM             ?= 0\n'

        if chos.find('b') != -1:
            blockchainSelected += (' [b] CITA\n')
            retBlockchain += 'BOAT_PROTOCOL_USE_CITA               ?= 1\n'
        else:
            retBlockchain += 'BOAT_PROTOCOL_USE_CITA               ?= 0\n' 

        if blockchainSelected == '':
            blockchainSelected = '    Selected NULL!\n'
        print(blockchainShow + blockchainSelected)
        return retBlockchain

    def selectplatform(self):
        ppf = 'Select the platform list as below:\n' + \
            '[1] linux-default             : Default linux platform\n' +\
            '[2] Fibocom-L610              : Fibocom\'s LTE Cat.1 module\n' +\
            '[3] create a new platform\n'
        chos = input(ppf)
        if chos == '1':
            print('platform is : linux-default\n')
            return 'linux-default'
        if chos == '2':
            print('platform is : Fibocom-L610\n')
            return 'Fibocom-L610'
        if chos == '3':
            print('default platfomr : linux-default\n')
            return input('input the platform name:')
        return 'linux-default'

    def boatlog(self,lname,log):
        print(lname + ' is [' + log + ']\n')
    
    def isgit(self):
        cmd = 'git pull'
    
    def rungitcmd(self,cmd):
        while(1):
            print(cmd+'\n')
            #self.boatlog('current path:',os.getcwd())
            try:
                subp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            
            except AssertionError as err:
                print('assert error');
            #else:
            #    print(' no error')
            retry = False

            while subp.poll() is None:
                if subp.wait() != 0:
                    print("cmd failed \n")
                    retry = True
                    break;
                
            if retry:
                if not self.getEnterAsNo('git cmd failed, try again?'):
                    print('failed ,but no retry\n')
                    return False
                print('retry')
            else:
                print('git cmd succ\n')
                return True

    def pullrepo(self,reponame):
        self.rungitcmd('git pull')
        
    def clonerepo(self,reponame):
        print('\nWe will clone the '+reponame +' repository, which may take several minutes\n')
       
       # choose the tag / branch
        branch_name = input('Input the branch name or null:')
        if branch_name != '':
            branch_name = ' -b ' + branch_name
        print('branch name is [' + branch_name + ']\n')
        cmd = 'git clone' + branch_name + ' https://github.com/aitos-io/' + reponame + '.git'

        if self.rungitcmd(cmd):
            #git pull succ, record the repo name
            self.usinglibs += reponame+'\n' 
            return True
        return False
    
    def checkRepo(self,reponame):
        if reponame == '':
            return True
        isExists = os.path.exists(reponame) 
        # If the folder exists, the repository is considered to have been downloaded
        if not isExists:
            # If clone failed, no Makefime creating
            return self.clonerepo(reponame)
        
        # pull the newest code?
        else:
            #the folder is existed , record the repo name
            self.usinglibs += reponame+'\n'
            needpull = self.getEnterAsNo('\npull the repository ' + reponame +'?')
            if needpull:
                os.chdir( './'+reponame )
                #self.boatlog('path',os.getcwd())
                self.pullrepo(reponame)
                os.chdir( '../' )
                #self.boatlog('path',os.getcwd())
        return True

def main():
    #Rename .git/HEAD to disable git operation of BoAT-ProjectTemplate 
    isExists = os.path.exists('./.git/HEAD')
    if isExists:
    	os.rename('./.git/HEAD','./.git/HEAD-bak')

    configContent_obj = ConfigContentGen()

    f = open('./BoATLibs.conf')
    for name in f.readlines():
        if configContent_obj.checkRepo(name.strip('\r\n *<>:	\\\/')) == False:
            print('Repositery cloning failed: ',name.strip('\n'),'\n')
            return

    # overwrite Makefile
    if configContent_obj.usinglibs == '':
        print("No lib is used\n")
        return
        
    owMakefile = configContent_obj.getEnterAsYes('overwrite the Makefile?')
    if owMakefile:
        
        # head
        configContent_obj.gen_Head()

        # block chain
        if configContent_obj.usinglibs.find('BoAT-Engine') != -1:
            myblockchain = configContent_obj.selectblockchain()        
            configContent_obj.gen_blockchain(myblockchain)

        # platform
        myplatform = configContent_obj.selectplatform()        
        configContent_obj.gen_platform(myplatform)
 
        # env
        configContent_obj.gen_env()

        # gcc version
        configContent_obj.gen_gccversion()

        # include path
        configContent_obj.gen_includepath()

        # other Flags
        configContent_obj.gen_otherFlags()
        
        # crypto
        configContent_obj.gen_crypto()

        # cJSON
        configContent_obj.gen_cJSON()

        # Combine FLAGS
        configContent_obj.gen_CombineFLAGS()

        # export
        configContent_obj.gen_export()

        # .PHONY
        configContent_obj.gen_PHONY()

        # all:
        configContent_obj.gen_all()

        # gen.py
        #configContent_obj.gen_genpy()  

        # targets
        configContent_obj.gen_targets()

        # clean:
        configContent_obj.gen_clean()
        
        # targets clean
        configContent_obj.gen_targetsclean()

        configContent_obj.save_config_file()

    print("Configuration completed\n")

if __name__ == '__main__':
    main()