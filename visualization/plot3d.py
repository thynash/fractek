import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
try:
    import plotly.graph_objs as go
    from plotly.offline import plot as plotly_show
except ImportError:
    go = None

def plot_fractal_3d(points, color='green', elev=30, azim=45, size=0.3, title="Fractal 3D", save_path=None):
    fig = plt.figure(figsize=(10,9))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(points[:,0], points[:,1], points[:,2], c=color, s=size)
    ax.view_init(elev=elev, azim=azim)
    ax.set_axis_off()
    ax.set_title(title)
    if save_path:
        plt.savefig(save_path, bbox_inches='tight', dpi=300)
    plt.show()

def plot_surface_3d(Z, X=None, Y=None, cmap='plasma', azim=45, elev=30, title="Fractal Heightmap Surface", save_path=None):
    if X is None or Y is None:
        n, m = Z.shape
        X, Y = np.meshgrid(np.linspace(0,1,n), np.linspace(0,1,m))
    fig = plt.figure(figsize=(10,9))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap=cmap, edgecolor='k', linewidth=0, rstride=2, cstride=2, alpha=0.9)
    ax.view_init(elev=elev, azim=azim)
    ax.set_axis_off()
    ax.set_title(title)
    if save_path:
        plt.savefig(save_path, bbox_inches='tight', dpi=300)
    plt.show()

def plot_fractal_3d_plotly(points, color='cyan', title="Fractal 3D (Plotly)", size=2):
    if go is None:
        raise ImportError("Plotly required for this function.")
    trace = go.Scatter3d(
        x=points[:,0], y=points[:,1], z=points[:,2],
        mode='markers',
        marker=dict(size=size, color=color)
    )
    layout = go.Layout(title=title, margin=dict(l=0,r=0,b=0,t=30))
    fig = go.Figure(data=[trace], layout=layout)
    plotly_show(fig)

