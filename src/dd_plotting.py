# Import necessary libraries
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.animation as animation


class LinePlotter:
    closeToLine = False  # Initialize flag for proximity to line
    p0 = [5, 1, 1]  # Initialize point location

    hitDistance = 1.1  # Distance away from line to consider a "near hit"

    def __init__(self):
        """
        Initializes the LinePlotter object with the line and point data, creates the 3D plot and initializes the
        animation object.
        """
        # Define the points on the line
        self.a = [0, 0, -.5]
        self.b = [8.2, 0, -.5]

        # Create an array of parameter values t
        self.t = np.linspace(0, 1, 100)

        # Define the x, y, and z values for the line
        self.xline = self.a[0] + self.t*(self.b[0] - self.a[0])
        self.yline = self.a[1] + self.t*(self.b[1] - self.a[1])
        self.zline = self.a[2] + self.t*(self.b[2] - self.a[2])

        # Create a 3D plot
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')

        # Plot the line
        self.line, = self.ax.plot3D(self.xline, self.yline, self.zline, 'gray')

        # Plot the point
        self.point, = self.ax.plot3D(self.p0[0], self.p0[1], self.p0[2], 'ro')

        # Plot the blue dot at (0,0,0)
        self.ax.scatter(0, 0, 0, color='blue')

        # Set the plot limits and labels
        self.ax.set_xlim3d(0, 8.2)
        self.ax.set_ylim3d(-1, 1)
        self.ax.set_zlim3d(-2, 7)
        self.ax.set_xlabel('X axis - inches')
        self.ax.set_ylabel('Y axis - inches')
        self.ax.set_zlabel('Z axis - inches')

        # Initialize animation object
        self.animation = None

    def update_point(self, frame, event):
        """
        Updates the position of the point on the plot and sets the flag for proximity to line based on the point's
        distance from the line.

        :param frame: unused animation frame parameter
        :param event: unused event parameter
        :return: the point on the plot
        """
        # Generate a new position for the point
        p = self.p0

        # Update the position of the point
        self.point.set_data(np.array([p[0], p[1]]))
        self.point.set_3d_properties(p[2], 'z')

        # Calculate the distance between the point and the line
        dist = np.min(np.sqrt(
            (self.xline - p[0])**2 + (self.yline - p[1])**2 + (self.zline - p[2])**2))

        # Compare the distance to a threshold value
        threshold = self.hitDistance
        if dist < threshold:
            self.closeToLine = True
        else:
            self.closeToLine = False

        # Return the point for animation
        return self.point,

    def start_animation(self):
        """
        Initializes and starts the animation of the point moving on the line
        """
        # Create the animation object
        self.animation = animation.FuncAnimation(
            self.fig, self.update_point, frames=np.arange(0, 200, 1), interval=50, blit=True, fargs=(None,))

    def stop_animation(self):
        """
        Stops the animation
        """
        # If the animation is running, stop it
        if self.animation:
            self.animation.event_source.stop()
