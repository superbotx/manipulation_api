from botX.components import BaseComponent
from botX.applications import external_command_pool
from botX.utils.install_util import maybe_download_git
from socketIO_client import SocketIO, BaseNamespace
from threading import Thread
import numpy as np

import rospy
from rosgraph_msgs.msg import Clock
from sensor_msgs.msg import Image, PointCloud2, CameraInfo

import matplotlib.pyplot as plt
import matplotlib.pyplot as pyplot

import sys
sys.path.append('external_modules')

import time
import os

from .path_planner import PathPlanner

class ManipulationAPI(BaseComponent):

    def setup(self):
        path_playnner = PathPlanner()
        pass
  

    def shutdown(self):
        pass

