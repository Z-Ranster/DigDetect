import tinyik as ik
import numpy as np

# Kinematic Chain
# Units in inches
excavator = ik.Actuator(
    [[0, 0, 0.2], "z", [0.0, 0.5, 0.0], "y", [0.0, 0.0, 1],
        "y", [0.0, 0.0, 1], "y", [0.0, 0.0, 0.5]]
)

# End Effector Location
efLocation = [0, 0, 0]


def calculateAngle(deg):
    excavator.angles = np.deg2rad(deg)
    efLocation = excavator.fk.solve(np.deg2rad(deg))
    print(efLocation)


def visualizeKM():
    ik.visualize(excavator)
