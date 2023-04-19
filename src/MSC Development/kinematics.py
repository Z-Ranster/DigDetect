import tinyik as ik
import numpy as np

# Kinematic Chain
# Units in inches
excavator = ik.Actuator(
    [[0, 0, 2.19], "z", [0.0, 0.001, 0.0], "y", [0.0, 0.0, 7.5],
        "y", [0.0, 0.0, 3.5], "y", [0.0, 0.0, 2.4]]
)

# End Effector Location
efLocation = [0, 0, 0]


def calculateAngle(deg):
    excavator.angles = np.deg2rad(deg)
    efLocation = excavator.fk.solve(np.deg2rad(deg))
    print(efLocation)
    return efLocation


def visualizeKM():
    ik.visualize(excavator)
