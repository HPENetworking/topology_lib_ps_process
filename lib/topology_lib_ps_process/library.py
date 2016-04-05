# -*- coding: utf-8 -*-
#
# Copyright (C) 2016 maria alas
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""
topology_lib_ps_process communication library implementation.
"""

from __future__ import unicode_literals, absolute_import
from __future__ import print_function, division
import re


def get_pid_ps_efa_command(enode, grep=None, shell='bash'):
    """
    This command will execute PS command into the switch
    ****IT IS CREATED FOR PS -FEA| GREP 'XXX' SO THE OUTPUT IS
                    NOT CREATED FOR EVERY OPTION****
    ******************                               ******************
    -grep search by this parameter

    """
    pass

    # This function will send ps command to bash
    #
    # command = 'ps -fea'
    # enode('ps -fea | grep 'filter', shell=shell)

    ps_command = 'ps -fea'
    if grep:
        ps_command = '{0} | grep \'{1}\''.format(ps_command, grep)

    ps_response = enode(ps_command, shell=shell)
    ps_re = (
      r'\s+(?P<pid>\d+)\s+\d+\s+\d+'
    )
    re_result = re.findall(ps_re, ps_response)
    assert re_result
    return re_result


__all__ = [
   'get_pid_ps_efa_command'
]
