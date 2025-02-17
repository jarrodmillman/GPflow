# Copyright 2016-2020 The GPflow Contributors. All Rights Reserved.
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
"""
This package contains code that is still experimental. This means:

* Expect breaking changes.
* Expect poor documentation.
* Expect bugs.

When the code is considered mature it will be moved out of this package.
"""
from . import check_shapes, utils

__all__ = [
    "check_shapes",
    "utils",
]
