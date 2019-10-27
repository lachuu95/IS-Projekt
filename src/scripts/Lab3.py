#!/usr/bin/env python3
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(sys.path[0])))
from src.common.dataset import Dataset
from src.common.interface import Interface

if __name__ == "__main__":
    data = Dataset()
    interface = Interface(data)
    interface.show_gui(use_db=True)