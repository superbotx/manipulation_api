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

from moveit_msgs.msg import MotionPlanRequest
from moveit_msgs.srv import GetMotionPlan

from haptica_manipulation.srv import PathFromPose


import time
import os


class ManipulationAPI(BaseComponent):

    def setup(self):
        # use a different check to confirm the robot is up
        rospy.wait_for_service("/plan_kinematic_path")
        
        command = "roslaunch haptica_manipulation path_planner.launch"
        self.proc_id = external_command_pool.start_command(command)

        rospy.wait_for_service("/plan_path")
        self.plan = rospy.ServiceProxy("/plan_path", PathFromPose)

        pass
  

    def plan_path(self, pose):
        path = self.plan(pose)
        print(path)
        return path
        # pass

    def shutdown(self):
        external_command_pool.end_command(self.proc_id)
        pass

