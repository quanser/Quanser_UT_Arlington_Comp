# Note use this method to get your qvl libraries to ensure you're using the latest version
# in GitHub. It is inserted first in the list to take precedence over all other libraries
# in your python path.
import sys
sys.path.insert(0, "../")

from qvl.qlabs import QuanserInteractiveLabs
from qvl.free_camera import QLabsFreeCamera
from qvl.qdrone2 import QLabsQDrone2
from qvl.basic_shape import QLabsBasicShape
from qvl.real_time import QLabsRealTime
from pal.resources import rtmodels

import sys
import time
import math
import struct
import numpy as np
import cv2
import os
#import keyboard


########### Main program #################


def main():
    qlabs = QuanserInteractiveLabs()

    print("Connecting to QLabs...")
    try:
        qlabs.open("localhost")
    except:
        print("Unable to connect to QLabs")
        return

    print("Connected")

    # Stop any existing realtime models
    QLabsRealTime().terminate_all_real_time_models()

    # create some dynamic environment objects
    hShape = QLabsBasicShape(qlabs, True)
    hShape.destroy_all_actors_of_class()

    box_mass = 10.0

    location_1 = -4
    location_2 = -6
    location_3 = -8
    location_4 = -10
    location_5 = -12
    location_6 = -16
    location_7 = -2
    location_8 = -14

    hShape.spawn([location_1,0,0.3], [0,0,0], [1,3,0.6], hShape.SHAPE_CUBE, True)
    hShape.set_material_properties([0.6,0,0], roughness=1, metallic=False, waitForConfirmation=True)
    hShape.set_physics_properties(enableDynamics=True, mass=box_mass, linearDamping=0.01, angularDamping=0.0, staticFriction=0.0, dynamicFriction=0.7, frictionCombineMode=hShape.COMBINE_AVERAGE, restitution=0.3, restitutionCombineMode=hShape.COMBINE_AVERAGE, waitForConfirmation=True)
    time.sleep(0.5)
    hShape.spawn([location_1,-1,1.2], [0,0,0], [1,1,1], hShape.SHAPE_CUBE, True)
    hShape.set_material_properties([0.8,0,0], roughness=1, metallic=False, waitForConfirmation=True)
    hShape.set_physics_properties(enableDynamics=True, mass=box_mass, linearDamping=0.01, angularDamping=0.0, staticFriction=0.0, dynamicFriction=0.7, frictionCombineMode=hShape.COMBINE_AVERAGE, restitution=0.3, restitutionCombineMode=hShape.COMBINE_AVERAGE, waitForConfirmation=True)
    time.sleep(0.5)
    hShape.spawn([location_1,1,1.2], [0,0,0], [1,1,1], hShape.SHAPE_CUBE, True)
    hShape.set_material_properties([0.8,0,0], roughness=1, metallic=False, waitForConfirmation=True)
    hShape.set_physics_properties(enableDynamics=True, mass=box_mass, linearDamping=0.01, angularDamping=0.0, staticFriction=0.0, dynamicFriction=0.7, frictionCombineMode=hShape.COMBINE_AVERAGE, restitution=0.3, restitutionCombineMode=hShape.COMBINE_AVERAGE, waitForConfirmation=True)
    time.sleep(0.5)
    hShape.spawn([location_1,0,1.85], [0,0,0], [1,3,0.5], hShape.SHAPE_CUBE, True)
    hShape.set_material_properties([0.6,0,0], roughness=1, metallic=False, waitForConfirmation=True)
    hShape.set_physics_properties(enableDynamics=True, mass=box_mass, linearDamping=0.01, angularDamping=0.0, staticFriction=0.0, dynamicFriction=0.7, frictionCombineMode=hShape.COMBINE_AVERAGE, restitution=0.3, restitutionCombineMode=hShape.COMBINE_AVERAGE, waitForConfirmation=True)
    time.sleep(0.5)

    hShape.spawn([location_2,0,0.6], [0,0,0], [1,3,1.1], hShape.SHAPE_CUBE, True)
    hShape.set_material_properties([0,0.6,0], roughness=1, metallic=False, waitForConfirmation=True)
    hShape.set_physics_properties(enableDynamics=True, mass=box_mass, linearDamping=0.01, angularDamping=0.0, staticFriction=0.0, dynamicFriction=0.7, frictionCombineMode=hShape.COMBINE_AVERAGE, restitution=0.3, restitutionCombineMode=hShape.COMBINE_AVERAGE, waitForConfirmation=True)
    time.sleep(0.5)
    hShape.spawn([location_2,-1,1.7], [0,0,0], [1,1,1], hShape.SHAPE_CUBE, True)
    hShape.set_material_properties([0,0.8,0], roughness=1, metallic=False, waitForConfirmation=True)
    hShape.set_physics_properties(enableDynamics=True, mass=box_mass, linearDamping=0.01, angularDamping=0.0, staticFriction=0.0, dynamicFriction=0.7, frictionCombineMode=hShape.COMBINE_AVERAGE, restitution=0.3, restitutionCombineMode=hShape.COMBINE_AVERAGE, waitForConfirmation=True)
    time.sleep(0.5)
    hShape.spawn([location_2,1,1.7], [0,0,0], [1,1,1], hShape.SHAPE_CUBE, True)
    hShape.set_material_properties([0,0.8,0], roughness=1, metallic=False, waitForConfirmation=True)
    hShape.set_physics_properties(enableDynamics=True, mass=box_mass, linearDamping=0.01, angularDamping=0.0, staticFriction=0.0, dynamicFriction=0.7, frictionCombineMode=hShape.COMBINE_AVERAGE, restitution=0.3, restitutionCombineMode=hShape.COMBINE_AVERAGE, waitForConfirmation=True)
    time.sleep(0.5)
    hShape.spawn([location_2,0,2.2], [0,0,0], [1,3,0.1], hShape.SHAPE_CUBE, True)
    hShape.set_material_properties([0,0.6,0], roughness=1, metallic=False, waitForConfirmation=True)
    hShape.set_physics_properties(enableDynamics=True, mass=box_mass, linearDamping=0.01, angularDamping=0.0, staticFriction=0.0, dynamicFriction=0.7, frictionCombineMode=hShape.COMBINE_AVERAGE, restitution=0.3, restitutionCombineMode=hShape.COMBINE_AVERAGE, waitForConfirmation=True)
    time.sleep(0.5)

    hShape.spawn([location_3,0,0.3], [0,0,0], [1,3,0.6], hShape.SHAPE_CUBE, True)
    hShape.set_material_properties([0.6,0.6,0], roughness=1, metallic=False, waitForConfirmation=True)
    hShape.set_physics_properties(enableDynamics=True, mass=box_mass, linearDamping=0.01, angularDamping=0.0, staticFriction=0.0, dynamicFriction=0.7, frictionCombineMode=hShape.COMBINE_AVERAGE, restitution=0.3, restitutionCombineMode=hShape.COMBINE_AVERAGE, waitForConfirmation=True)
    time.sleep(0.5)
    hShape.spawn([location_3,-1,1.2], [0,0,0], [1,1,1], hShape.SHAPE_CUBE, True)
    hShape.set_material_properties([0.8,0.8,0], roughness=1, metallic=False, waitForConfirmation=True)
    hShape.set_physics_properties(enableDynamics=True, mass=box_mass, linearDamping=0.01, angularDamping=0.0, staticFriction=0.0, dynamicFriction=0.7, frictionCombineMode=hShape.COMBINE_AVERAGE, restitution=0.3, restitutionCombineMode=hShape.COMBINE_AVERAGE, waitForConfirmation=True)
    time.sleep(0.5)
    hShape.spawn([location_3,1,1.2], [0,0,0], [1,1,1], hShape.SHAPE_CUBE, True)
    hShape.set_material_properties([0.8,0.8,0], roughness=1, metallic=False, waitForConfirmation=True)
    hShape.set_physics_properties(enableDynamics=True, mass=box_mass, linearDamping=0.01, angularDamping=0.0, staticFriction=0.0, dynamicFriction=0.7, frictionCombineMode=hShape.COMBINE_AVERAGE, restitution=0.3, restitutionCombineMode=hShape.COMBINE_AVERAGE, waitForConfirmation=True)
    time.sleep(0.5)
    hShape.spawn([location_3,0,1.85], [0,0,0], [1,3,0.5], hShape.SHAPE_CUBE, True)
    hShape.set_material_properties([0.6,0.6,0], roughness=1, metallic=False, waitForConfirmation=True)
    hShape.set_physics_properties(enableDynamics=True, mass=box_mass, linearDamping=0.01, angularDamping=0.0, staticFriction=0.0, dynamicFriction=0.7, frictionCombineMode=hShape.COMBINE_AVERAGE, restitution=0.3, restitutionCombineMode=hShape.COMBINE_AVERAGE, waitForConfirmation=True)
    time.sleep(0.5)

    hShape.spawn([location_4,-1,0.5], [0,0,0], [1,1,1.0], hShape.SHAPE_CUBE, True)
    hShape.set_material_properties([0.8,0,0.8], roughness=1, metallic=False, waitForConfirmation=True)
    hShape.set_physics_properties(enableDynamics=True, mass=box_mass, linearDamping=0.01, angularDamping=0.0, staticFriction=0.0, dynamicFriction=0.7, frictionCombineMode=hShape.COMBINE_AVERAGE, restitution=0.3, restitutionCombineMode=hShape.COMBINE_AVERAGE, waitForConfirmation=True)
    time.sleep(0.5)
    hShape.spawn([location_4,1,0.5], [0,0,0], [1,1,1.0], hShape.SHAPE_CUBE, True)
    hShape.set_material_properties([0.8,0,0.8], roughness=1, metallic=False, waitForConfirmation=True)
    hShape.set_physics_properties(enableDynamics=True, mass=box_mass, linearDamping=0.01, angularDamping=0.0, staticFriction=0.0, dynamicFriction=0.7, frictionCombineMode=hShape.COMBINE_AVERAGE, restitution=0.3, restitutionCombineMode=hShape.COMBINE_AVERAGE, waitForConfirmation=True)
    time.sleep(0.5)
    hShape.spawn([location_4,0,1.6], [0,0,0], [1,3,1.1], hShape.SHAPE_CUBE, True)
    hShape.set_material_properties([0.6,0,0.6], roughness=1, metallic=False, waitForConfirmation=True)
    hShape.set_physics_properties(enableDynamics=True, mass=box_mass, linearDamping=0.01, angularDamping=0.0, staticFriction=0.0, dynamicFriction=0.7, frictionCombineMode=hShape.COMBINE_AVERAGE, restitution=0.3, restitutionCombineMode=hShape.COMBINE_AVERAGE, waitForConfirmation=True)

    hShape.spawn([location_5,0,0.3], [0,0,0], [1,3,0.6], hShape.SHAPE_CUBE, True)
    hShape.set_material_properties([0.6,0,0], roughness=1, metallic=False, waitForConfirmation=True)
    hShape.set_physics_properties(enableDynamics=True, mass=box_mass, linearDamping=0.01, angularDamping=0.0, staticFriction=0.0, dynamicFriction=0.7, frictionCombineMode=hShape.COMBINE_AVERAGE, restitution=0.3, restitutionCombineMode=hShape.COMBINE_AVERAGE, waitForConfirmation=True)
    time.sleep(0.5)
    hShape.spawn([location_5,-1,1.2], [0,0,0], [1,1,1], hShape.SHAPE_CUBE, True)
    hShape.set_material_properties([0.8,0,0], roughness=1, metallic=False, waitForConfirmation=True)
    hShape.set_physics_properties(enableDynamics=True, mass=box_mass, linearDamping=0.01, angularDamping=0.0, staticFriction=0.0, dynamicFriction=0.7, frictionCombineMode=hShape.COMBINE_AVERAGE, restitution=0.3, restitutionCombineMode=hShape.COMBINE_AVERAGE, waitForConfirmation=True)
    time.sleep(0.5)
    hShape.spawn([location_5,1,1.2], [0,0,0], [1,1,1], hShape.SHAPE_CUBE, True)
    hShape.set_material_properties([0.8,0,0], roughness=1, metallic=False, waitForConfirmation=True)
    hShape.set_physics_properties(enableDynamics=True, mass=box_mass, linearDamping=0.01, angularDamping=0.0, staticFriction=0.0, dynamicFriction=0.7, frictionCombineMode=hShape.COMBINE_AVERAGE, restitution=0.3, restitutionCombineMode=hShape.COMBINE_AVERAGE, waitForConfirmation=True)
    time.sleep(0.5)
    hShape.spawn([location_5,0,1.85], [0,0,0], [1,3,0.5], hShape.SHAPE_CUBE, True)
    hShape.set_material_properties([0.6,0,0], roughness=1, metallic=False, waitForConfirmation=True)
    hShape.set_physics_properties(enableDynamics=True, mass=box_mass, linearDamping=0.01, angularDamping=0.0, staticFriction=0.0, dynamicFriction=0.7, frictionCombineMode=hShape.COMBINE_AVERAGE, restitution=0.3, restitutionCombineMode=hShape.COMBINE_AVERAGE, waitForConfirmation=True)
    time.sleep(0.5)

    hShape.spawn([location_6,0,0.6], [0,0,0], [1,3,1.1], hShape.SHAPE_CUBE, True)
    hShape.set_material_properties([0,0.6,0], roughness=1, metallic=False, waitForConfirmation=True)
    hShape.set_physics_properties(enableDynamics=True, mass=box_mass, linearDamping=0.01, angularDamping=0.0, staticFriction=0.0, dynamicFriction=0.7, frictionCombineMode=hShape.COMBINE_AVERAGE, restitution=0.3, restitutionCombineMode=hShape.COMBINE_AVERAGE, waitForConfirmation=True)
    time.sleep(0.5)
    hShape.spawn([location_6,-1,1.7], [0,0,0], [1,1,1], hShape.SHAPE_CUBE, True)
    hShape.set_material_properties([0,0.8,0], roughness=1, metallic=False, waitForConfirmation=True)
    hShape.set_physics_properties(enableDynamics=True, mass=box_mass, linearDamping=0.01, angularDamping=0.0, staticFriction=0.0, dynamicFriction=0.7, frictionCombineMode=hShape.COMBINE_AVERAGE, restitution=0.3, restitutionCombineMode=hShape.COMBINE_AVERAGE, waitForConfirmation=True)
    time.sleep(0.5)
    hShape.spawn([location_6,1,1.7], [0,0,0], [1,1,1], hShape.SHAPE_CUBE, True)
    hShape.set_material_properties([0,0.8,0], roughness=1, metallic=False, waitForConfirmation=True)
    hShape.set_physics_properties(enableDynamics=True, mass=box_mass, linearDamping=0.01, angularDamping=0.0, staticFriction=0.0, dynamicFriction=0.7, frictionCombineMode=hShape.COMBINE_AVERAGE, restitution=0.3, restitutionCombineMode=hShape.COMBINE_AVERAGE, waitForConfirmation=True)
    time.sleep(0.5)
    hShape.spawn([location_6,0,2.2], [0,0,0], [1,3,0.1], hShape.SHAPE_CUBE, True)
    hShape.set_material_properties([0,0.6,0], roughness=1, metallic=False, waitForConfirmation=True)
    hShape.set_physics_properties(enableDynamics=True, mass=box_mass, linearDamping=0.01, angularDamping=0.0, staticFriction=0.0, dynamicFriction=0.7, frictionCombineMode=hShape.COMBINE_AVERAGE, restitution=0.3, restitutionCombineMode=hShape.COMBINE_AVERAGE, waitForConfirmation=True)
    time.sleep(0.5)

    hShape.spawn([location_7,0,0.3], [0,0,0], [1,3,0.6], hShape.SHAPE_CUBE, True)
    hShape.set_material_properties([0.6,0.6,0], roughness=1, metallic=False, waitForConfirmation=True)
    hShape.set_physics_properties(enableDynamics=True, mass=box_mass, linearDamping=0.01, angularDamping=0.0, staticFriction=0.0, dynamicFriction=0.7, frictionCombineMode=hShape.COMBINE_AVERAGE, restitution=0.3, restitutionCombineMode=hShape.COMBINE_AVERAGE, waitForConfirmation=True)
    time.sleep(0.5)
    hShape.spawn([location_7,-1,1.2], [0,0,0], [1,1,1], hShape.SHAPE_CUBE, True)
    hShape.set_material_properties([0.8,0.8,0], roughness=1, metallic=False, waitForConfirmation=True)
    hShape.set_physics_properties(enableDynamics=True, mass=box_mass, linearDamping=0.01, angularDamping=0.0, staticFriction=0.0, dynamicFriction=0.7, frictionCombineMode=hShape.COMBINE_AVERAGE, restitution=0.3, restitutionCombineMode=hShape.COMBINE_AVERAGE, waitForConfirmation=True)
    time.sleep(0.5)
    hShape.spawn([location_7,1,1.2], [0,0,0], [1,1,1], hShape.SHAPE_CUBE, True)
    hShape.set_material_properties([0.8,0.8,0], roughness=1, metallic=False, waitForConfirmation=True)
    hShape.set_physics_properties(enableDynamics=True, mass=box_mass, linearDamping=0.01, angularDamping=0.0, staticFriction=0.0, dynamicFriction=0.7, frictionCombineMode=hShape.COMBINE_AVERAGE, restitution=0.3, restitutionCombineMode=hShape.COMBINE_AVERAGE, waitForConfirmation=True)
    time.sleep(0.5)
    hShape.spawn([location_7,0,1.85], [0,0,0], [1,3,0.5], hShape.SHAPE_CUBE, True)
    hShape.set_material_properties([0.6,0.6,0], roughness=1, metallic=False, waitForConfirmation=True)
    hShape.set_physics_properties(enableDynamics=True, mass=box_mass, linearDamping=0.01, angularDamping=0.0, staticFriction=0.0, dynamicFriction=0.7, frictionCombineMode=hShape.COMBINE_AVERAGE, restitution=0.3, restitutionCombineMode=hShape.COMBINE_AVERAGE, waitForConfirmation=True)
    time.sleep(0.5)

    hShape.spawn([location_8,-1,0.5], [0,0,0], [1,1,1.0], hShape.SHAPE_CUBE, True)
    hShape.set_material_properties([0.8,0,0.8], roughness=1, metallic=False, waitForConfirmation=True)
    hShape.set_physics_properties(enableDynamics=True, mass=box_mass, linearDamping=0.01, angularDamping=0.0, staticFriction=0.0, dynamicFriction=0.7, frictionCombineMode=hShape.COMBINE_AVERAGE, restitution=0.3, restitutionCombineMode=hShape.COMBINE_AVERAGE, waitForConfirmation=True)
    time.sleep(0.5)
    hShape.spawn([location_8,1,0.5], [0,0,0], [1,1,1.0], hShape.SHAPE_CUBE, True)
    hShape.set_material_properties([0.8,0,0.8], roughness=1, metallic=False, waitForConfirmation=True)
    hShape.set_physics_properties(enableDynamics=True, mass=box_mass, linearDamping=0.01, angularDamping=0.0, staticFriction=0.0, dynamicFriction=0.7, frictionCombineMode=hShape.COMBINE_AVERAGE, restitution=0.3, restitutionCombineMode=hShape.COMBINE_AVERAGE, waitForConfirmation=True)
    time.sleep(0.5)
    hShape.spawn([location_8,0,1.6], [0,0,0], [1,3,1.1], hShape.SHAPE_CUBE, True)
    hShape.set_material_properties([0.6,0,0.6], roughness=1, metallic=False, waitForConfirmation=True)
    hShape.set_physics_properties(enableDynamics=True, mass=box_mass, linearDamping=0.01, angularDamping=0.0, staticFriction=0.0, dynamicFriction=0.7, frictionCombineMode=hShape.COMBINE_AVERAGE, restitution=0.3, restitutionCombineMode=hShape.COMBINE_AVERAGE, waitForConfirmation=True)

    # destroy the previous QDrone2 and respawn it in a starting position

    hQDrone = QLabsQDrone2(qlabs, True)
    hQDrone.actorNumber=0
    hQDrone.destroy()
    hQDrone.spawn_id_degrees(actorNumber=0, location=[0, 0, 0], rotation=[0, 0, 0], scale=[1,1,1], configuration=0)
    hQDrone.possess(hQDrone.VIEWPOINT_TRAILING)

    # Specify path to where spawn model is located; start Qdrone2 workspace model
    rtmodel_path = rtmodels.QDRONE2
    QLabsRealTime().start_real_time_model(modelName=rtmodel_path, actorNumber=0)

    qlabs.close()
    print("Done!")

main()