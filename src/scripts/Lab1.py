#!/usr/bin/env python3
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(sys.path[0])))
from src.common.dataset import Dataset

if __name__ == "__main__":
    data = Dataset()
    data.read_data()
    print(data.get_console_layout())
