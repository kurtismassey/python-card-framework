# Copyright 2022 Google Inc. All Rights Reserved.
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
from __future__ import annotations

import unittest
from dataclasses import Field, dataclass
from typing import List

from dataclasses_json import dataclass_json

from card_framework import *
from card_framework.v2.message import Message


class MessageTest(unittest.TestCase):
  def test_empty_message(self) -> None:
    m = Message()
    m.name = 'Inigo Montoya'

    self.assertDictEqual(m.render(), {'name': 'Inigo Montoya'})
