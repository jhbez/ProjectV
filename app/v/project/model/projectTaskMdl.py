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


class ProjectTaskMdl:
    _table = 'project_tasks'
    _fields = {
        u'name': {
            'required': True,
            'length': {'min': 3},
            'typeof': 'str'
        },
        u'description': {
            'length': {'min': 3},
            'typeof': 'str'
        },
        u'project_id': {
            'required': True,
            'typeof': 'int'
        },
        # u'parent_id': {
        #     'typeof': 'int'
        # },
        u'start_date_at': {
            'typeof': 'date'
        },
        u'due_date_at': {
            'typeof': 'date'
        },
        u'completed_at': {
            'typeof': 'date'
        },
    }

    def __init__(self):
        pass

    _query_get = """
        SELECT array_to_json(array_agg(row_to_json(t) )) as collection FROM (
            SELECT id,project_id, parent_id, name, description, start_date_at, due_date_at, completed_at
            FROM project_tasks %s
            )t;
    """