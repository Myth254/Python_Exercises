import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy import integrate


def surface_function(x, y):
    """Define the surface z = x² + y²"""
    return x ** 2 + y ** 2


def analytical_solution():
    """
    Calculate the analytical solution using double integration
    ∫∫(x² + y²) dx dy over [0,1] × [0,1]
    = ∫₀¹ ∫₀¹ (x² + y²) dx dy
    = ∫₀¹ [x³/3 + xy²]₀¹ dy
    = ∫₀¹ (1/3 + y²) dy
    = [y/3 + y³/3]₀¹
    = 1/3 + 1/3 = 2/3
    """
    return 2 / 3


def numerical_integration_scipy():
    """Calculate volume using scipy's double integration"""
    result, error = integrate.dblquad(surface_function, 0, 1, 0, 1)
    return result, error


def numerical_integration_riemann(n=100):
    """Calculate volume using Riemann sum approximation"""
    dx = dy = 1.0 / n
    volume = 0

    for i in range(n):
        for j in range(n):
            x = (i + 0.5) * dx  # Midpoint rule
            y = (j + 0.5) * dy
            volume += surface_function(x, y) * dx * dy

    return volume


def monte_carlo_integration(n_points=100000):
    """Calculate volume using Monte Carlo method"""
    # Generate random points in the unit square
    x_random = np.random.uniform(0, 1, n_points)
    y_random = np.random.uniform(0, 1, n_points)

    # Calculate function values at random points
    z_values = surface_function(x_random, y_random)

    # Volume = area of base × average height
    volume = np.mean(z_values) * 1.0  # Unit square has area 1

    return volume


def visualize_surface():
    """Create 3D visualization of the surface"""
    # Create mesh grid
    x = np.linspace(0, 1, 50)
    y = np.linspace(0, 1, 50)
    X, Y = np.meshgrid(x, y)
    Z = surface_function(X, Y)

    # Create 3D plot
    fig = plt.figure(figsize=(12, 5))

    # 3D surface plot
    ax1 = fig.add_subplot(121, projection='3d')
    surf = ax1.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_zlabel('z = x² + y²')
    ax1.set_title('Surface z = x² + y²')
    plt.colorbar(surf, shrink=0.5)

    # Contour plot
    ax2 = fig.add_subplot(122)
    contour = ax2.contour(X, Y, Z, levels=20)
    ax2.clabel(contour, inline=True, fontsize=8)
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.set_title('Contour Lines of z = x² + y²')
    ax2.set_aspect('equal')

    plt.tight_layout()
    plt.show()


def main():
    print("Volume Calculation: z = x² + y² over [0,1] × [0,1]")
    print("=" * 55)

    # Analytical solution
    analytical_vol = analytical_solution()
    print(f"1. Analytical Solution:")
    print(f"   Volume = 2/3 = {analytical_vol:.10f}")
    print()

    # Numerical integration using scipy
    scipy_vol, scipy_error = numerical_integration_scipy()
    print(f"2. Numerical Integration (SciPy):")
    print(f"   Volume = {scipy_vol:.10f}")
    print(f"   Error estimate = {scipy_error:.2e}")
    print(f"   Difference from analytical = {abs(scipy_vol - analytical_vol):.2e}")
    print()

    # Riemann sum approximation
    riemann_vol = numerical_integration_riemann(100)
    print(f"3. Riemann Sum (100×100 grid):")
    print(f"   Volume = {riemann_vol:.10f}")
    print(f"   Difference from analytical = {abs(riemann_vol - analytical_vol):.2e}")
    print()

    # Monte Carlo method
    mc_vol = monte_carlo_integration(100000)
    print(f"4. Monte Carlo Method (100,000 points):")
    print(f"   Volume = {mc_vol:.10f}")
    print(f"   Difference from analytical = {abs(mc_vol - analytical_vol):.2e}")
    print()

    # Step-by-step analytical calculation
    print("Step-by-step Analytical Calculation:")
    print("-" * 35)
    print("∫₀¹ ∫₀¹ (x² + y²) dx dy")
    print("= ∫₀¹ [∫₀¹ (x² + y²) dx] dy")
    print("= ∫₀¹ [x³/3 + xy²]₀¹ dy")
    print("= ∫₀¹ (1/3 + y²) dy")
    print("= [y/3 + y³/3]₀¹")
    print("= (1/3 + 1/3) - (0)")
    print("= 2/3")
    print()

    # Convergence test for Riemann sum
    print("Riemann Sum Convergence:")
    print("-" * 25)
    grid_sizes = [10, 25, 50, 100, 200]
    for n in grid_sizes:
        vol = numerical_integration_riemann(n)
        error = abs(vol - analytical_vol)
        print(f"Grid {n:3d}×{n:3d}: Volume = {vol:.8f}, Error = {error:.2e}")

    # Create visualization
    print("\nGenerating 3D visualization...")
    visualize_surface()


if __name__ == "__main__":
    main()