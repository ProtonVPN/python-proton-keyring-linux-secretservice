#!/usr/bin/env python

from setuptools import setup, find_namespace_packages

setup(
    name="proton-keyring-linux-secretservice",
    version="0.0.2",
    description="Proton AG keyring secretservice implementation for linux",
    author="Proton AG",
    author_email="contact@protonmail.com",
    url="https://github.com/ProtonVPN/python-proton-keyring-linux-secretservice",
    install_requires=["proton-keyring-linux", "secretstorage"],
    entry_points={
        "proton_loader_keyring": [
            "secret_service = proton.keyring_linux.secretservice:KeyringBackendLinuxSecretService"
        ]
    },
    extras_require={
        "development": ["pytest", "pytest-coverage", "pylint", "flake8"]
    },
    packages=find_namespace_packages(include=['proton.keyring_linux.secretservice']),
    include_package_data=True,
    python_requires=">=3.8",
    license="GPLv3",
    platforms="OS Independent",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python",
        "Topic :: Security",
    ]
)
