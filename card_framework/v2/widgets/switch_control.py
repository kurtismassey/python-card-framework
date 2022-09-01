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
from dataclasses import dataclass, field
from typing import Optional

from dataclasses_json import LetterCase, config, dataclass_json

from ..enums import ControlType
from ..widget import Widget
from .action import Action


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SwitchControl(Widget):
  """SwitchControl
  """
  name: str = field(default='')
  value: str = field(default='')
  selected: bool = field(default=None)
  onChangeAction: Action = field(default=None)
  controlType: ControlType = field(
      default=None, metadata=config(letter_case=LetterCase.CAMEL))

  @property
  def _widget_tag(self) -> str:
    """The widget tag name.

    Returns:
        str: The key by which the widget will be rendered in the Section.
    """
    return 'switchControl'
