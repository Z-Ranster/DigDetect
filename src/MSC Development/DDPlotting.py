import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.animation as animation


class LinePlotter:
    def __init__(self):
        # Define the points on the line
        self.a = [0, 0, 0]
        self.b = [10, 0, 0]

        # Create an array of parameter values t
        self.t = np.linspace(0, 1, 100)

        # Define the x, y, and z values for the line
        self.xline = self.a[0] + self.t*(self.b[0] - self.a[0])
        self.yline = self.a[1] + self.t*(self.b[1] - self.a[1])
        self.zline = self.a[2] + self.t*(self.b[2] - self.a[2])

        # Define the initial position of the point
        self.p0 = [5, 1, 1]

        # Create a 3D plot
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')

        # Plot the line
        self.line, = self.ax.plot3D(self.xline, self.yline, self.zline, 'gray')

        # Plot the point
        self.point, = self.ax.plot3D(self.p0[0], self.p0[1], self.p0[2], 'ro')

        # Set the plot limits
        self.ax.set_xlim3d(0, 10)
        self.ax.set_ylim3d(0, 10)
        self.ax.set_zlim3d(0, 10)

        # Set the plot labels
        self.ax.set_xlabel('X axis')
        self.ax.set_ylabel('Y axis')
        self.ax.set_zlabel('Z axis')

        # Initialize animation object
        self.animation = None

    def update_point(self, i):
        # Generate a new position for the point
        p = [5 + 3*np.sin(i/10), 1 + np.cos(i/10), 1 + np.sin(i/10)]

        # Update the position of the point
        self.point.set_data(np.array([p[0], p[1]]))
        self.point.set_3d_properties(p[2], 'z')

        # Calculate the distance between the point and the line
        dist = np.min(np.sqrt(
            (self.xline - p[0])**2 + (self.yline - p[1])**2 + (self.zline - p[2])**2))

        # Compare the distance to a threshold value
        threshold = 1.0
        if dist < threshold:
            print("The point is close to the line.")
        else:
            print("The point is not close to the line.")

        # Return the point
        return self.point,

    def start_animation(self):
        # Create an animation
        self.animation = animation.FuncAnimation(
            self.fig, self.update_point, frames=np.arange(0, 200, 1), interval=50, blit=True)

    def stop_animation(self):
        # Stop the animation
        if self.animation:
            self.animation.event_source.stop()


# if __name__ == '__main__':
#     # Create a LinePlotter object
#     plotter = LinePlotter()

#     # Start the animation
#     plotter.start_animation()
