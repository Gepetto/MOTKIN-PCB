import xml.etree.ElementTree as ET
from pathlib import Path

from setuptools import find_packages, setup

ROOT = ET.parse("package.xml").getroot()
PACKAGE = {
    k: ROOT.find(k).text
    for k in ["name", "version", "description", "license", "author", "maintainer"]
}
MAILS = {k: ROOT.find(k).get("email") for k in ["author", "maintainer"]}
README = Path(__file__).parent / "README.md"


setup(
    name=PACKAGE["name"].replace("_", "-"),
    version=PACKAGE["version"],
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + PACKAGE["name"]]),
        ("share/" + PACKAGE["name"], ["PACKAGE.xml"]),
    ],
    package_data={"": ["py.typed"]},
    install_requires=["matplotlib", "pyserial", "setuptools"],
    zip_safe=True,
    author=PACKAGE["author"],
    author_email=MAILS["author"],
    maintainer=PACKAGE["maintainer"],
    maintainer_email=MAILS["maintainer"],
    description=PACKAGE["description"],
    long_description=README.read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    license=PACKAGE["license"],
    extras_require={
        "test": [
            "pytest",
        ],
    },
    entry_points={
        "console_scripts": [
            "demo_motor_coupling = motkin_pcb.demo_motor_coupling:main",
            "demo_motor_tone = motkin_pcb.demo_motor_tone:main",
            "demo_sine_position = motkin_pcb.demo_sine_position:main",
            "measure_host_timing = motkin_pcb.measure_host_timing:main",
            "monitor_zero_torque = motkin_pcb.monitor_zero_torque:main",
            "plot_current_step_response = motkin_pcb.plot_current_step_response:main",
        ],
    },
)
