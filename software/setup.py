from setuptools import find_packages, setup

package_name = "pico_dual_pmsm_bu79100g_drv8316c"

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    package_data={"": ["py.typed"]},
    install_requires=["setuptools"],
    zip_safe=True,
    author="Thomas Flayols",
    author_email="thomas.flayols@laas.fr",
    maintainer="Guilhem Saurel",
    maintainer_email="guilhem.saurel@laas.fr",
    description="usb driver for pico_dual_PMSM_BU79100G_DRV8316C",
    license="BSD-2-Clause",
    extras_require={
        "test": [
            "pytest",
        ],
    },
    entry_points={
        "console_scripts": [
            "demo_motor_coupling = motor_usb.demo_motor_coupling:main",
            "demo_motor_tone = motor_usb.demo_motor_tone:main",
            "demo_sine_position = motor_usb.demo_sine_position:main",
            "measure_host_timing = motor_usb.measure_host_timing:main",
            "monitor_zero_torque = motor_usb.monitor_zero_torque:main",
            "plot_current_step_response = motor_usb.plot_current_step_response:main",
        ],
    },
)
