import sys

try:
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    from matplotlib.animation import FuncAnimation
    from IPython.display import HTML, display
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    from matplotlib.animation import FuncAnimation
    from IPython.display import HTML, display

# Função para calcular as coordenadas da esfera
def calculate_sphere_coordinates(radius, num_points):
    phi = np.linspace(0, np.pi, num_points)
    theta = np.linspace(0, 2 * np.pi, num_points)
    phi, theta = np.meshgrid(phi, theta)

    x = radius * np.sin(phi) * np.cos(theta)
    y = radius * np.sin(phi) * np.sin(theta)
    z = radius * np.cos(phi)

    return x, y, z

# Função para criar a animação da esfera
def animate_sphere(num_spectrums):
    fig = plt.figure(figsize=(12, 6))

    # Adicionando a esfera
    ax_sphere = fig.add_subplot(121, projection='3d')
    ax_sphere.set_xlim([-1.5, 1.5])
    ax_sphere.set_ylim([-1.5, 1.5])
    ax_sphere.set_zlim([-1.5, 1.5])
    ax_sphere.set_xlabel('X')
    ax_sphere.set_ylabel('Y')
    ax_sphere.set_zlabel('Z')
    ax_sphere.set_title('Esfera de Cores')

    # Adicionando a equação
    ax_equation = fig.add_subplot(122)
    ax_equation.set_xlim([0, 10])
    ax_equation.set_ylim([0, 10])
    ax_equation.axis('off')

    sphere = ax_sphere.plot_surface([], [], [], color='white', antialiased=False)

    # Função de animação
    def update(frame):
        nonlocal sphere
        ax_sphere.cla()
        ax_equation.cla()

        ax_sphere.set_xlim([-1.5, 1.5])
        ax_sphere.set_ylim([-1.5, 1.5])
        ax_sphere.set_zlim([-1.5, 1.5])
        ax_sphere.set_xlabel('X')
        ax_sphere.set_ylabel('Y')
        ax_sphere.set_zlabel('Z')
        ax_sphere.set_title('Esfera de Cores')

        ax_equation.set_xlim([0, 10])
        ax_equation.set_ylim([0, 10])
        ax_equation.axis('off')

        x, y, z = calculate_sphere_coordinates(1, frame)
        sphere = ax_sphere.plot_surface(x, y, z, color='white', antialiased=False)

        equation_text = f'Número de Faixas: {frame}'
        ax_equation.text(0.5, 0.5, equation_text, fontsize=12, ha='center', va='center')

    # Criando a animação
    animation = FuncAnimation(fig, update, frames=np.arange(1, num_spectrums + 1), interval=500, repeat=False)

    # Exibindo a animação no Jupyter Notebook
    display(HTML(animation.to_jshtml()))

animate_sphere(num_spectrums=7)
