# -*- coding: utf-8 -*-
# Copyright 2017 ProjectV Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class DreamMdl:
    _table = 'dreams'
    _fields = {
        'name': {'required': True, 'length': {'min': 3}, 'typeof': 'str'},
        'due_date_at': {'typeof': 'date'},
        'completed_at': {'typeof': 'date'},
        'reward': {'typeof': 'str'},
        'reach_goal': {'typeof': 'str'}
    }

    def __init__(self):
        pass
