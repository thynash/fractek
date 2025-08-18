import matplotlib.animation as animation
import matplotlib.pyplot as plt

def animate_fractal_sequence(fractal_arrays, extent=(-2,2,-2,2), cmap='hot', title="Fractal Animation", interval=80, save_path=None):
    fig, ax = plt.subplots()
    ims = []
    for arr in fractal_arrays:
        im = ax.imshow(arr, cmap=cmap, extent=extent, origin='lower', animated=True)
        ims.append([im])
    ani = animation.ArtistAnimation(fig, ims, interval=interval, blit=True)
    ax.set_title(title)
    ax.axis('off')
    if save_path:
        ani.save(save_path)
    plt.show()
    return ani

def animate_parameter_morph(frac_func, param1, param2, steps=20, fixed_kwargs=None, extent=(-2,2,-2,2), cmap='viridis', interval=120):
    """Animate morphing between two fractals changing one parameter."""
    arrs = []
    for t in np.linspace(0, 1, steps):
        p = param1 * (1-t) + param2 * t
        kwargs = dict(fixed_kwargs) if fixed_kwargs else {}
        kwargs['param'] = p
        arrs.append(frac_func(**kwargs))
    return animate_fractal_sequence(arrs, extent=extent, cmap=cmap, interval=interval)

