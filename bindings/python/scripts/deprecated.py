#
# Copyright (c) 2018 CNRS
#
# This file is part of Pinocchio
# Pinocchio is free software: you can redistribute it
# and/or modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation, either version
# 3 of the License, or (at your option) any later version.
# Pinocchio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Lesser Public License for more details. You should have
# received a copy of the GNU Lesser General Public License along with
# Pinocchio If not, see
# <http://www.gnu.org/licenses/>.

## In this file, are reported some depracated functions that are still maintain until the next important release 1.4.0 ##

from __future__ import print_function

from . import libpinocchio_pywrap as se3 
from .deprecation import deprecated

@deprecated("This function has been renamed computeJointJacobians and will be removed in release 1.4.0 of Pinocchio. Please change for new computeJacobians.")
def computeJacobians(model,data,q=None):
  if q is None:
    return computeJointJacobians(model,data)
  else:
    return computeJointJacobians(model,data,q)

@deprecated("This function has been renamed jointJacobian and will be removed in release 1.4.0 of Pinocchio. Please change for new jointJacobian.")
def jacobian(model,data,q,jointId,local,update_kinematics):
  if local:
    return jointJacobian(model,data,q,jointId,se3.ReferenceFrame.LOCAL,update_kinematics)
  else:
    return jointJacobian(model,data,q,jointId,se3.ReferenceFrame.WORLD,update_kinematics)

@deprecated("This function has been renamed getJointJacobian and will be removed in release 1.4.0 of Pinocchio. Please change for new getJointJacobian.")
def getJointJacobian(model,data,jointId,local):
  if local:
    return getJointJacobian(model,data,jointId,se3.ReferenceFrame.LOCAL)
  else:
    return getJointJacobian(model,data,jointId,se3.ReferenceFrame.WORLD)

@deprecated("This function has been renamed computeJacobiansTimeVariation and will be removed in release 1.4.0 of Pinocchio. Please change for new computeJacobiansTimeVariation.")
def computeJacobiansTimeVariation(model,data,q,v):
  return computeJointJacobiansTimeVariation(model,data,q,v)

@deprecated("This function has been renamed getJointJacobianTimeVariation and will be removed in release 1.4.0 of Pinocchio. Please change for new getJointJacobianTimeVariation.")
def getJacobianTimeVariation(model,data,jointId,local):
  if local:
    return getJointJacobianTimeVariation(model,data,jointId,se3.ReferenceFrame.LOCAL)
  else:
    return getJointJacobianTimeVariation(model,data,jointId,se3.ReferenceFrame.WORLD)

