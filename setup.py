"""
Setup script for Daily Dashboard & API Testing Suite
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="daily-dashboard",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A comprehensive Python project for REST API interactions and daily dashboard",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/RestApis",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Utilities",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "daily-dashboard=daily_dashboard:main",
            "dashboard-auto=daily_dashboard_auto:main",
            "test-apis=test_api_client:main",
        ],
    },
    keywords="api, dashboard, weather, jokes, quotes, rest, http",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/RestApis/issues",
        "Source": "https://github.com/yourusername/RestApis",
        "Documentation": "https://github.com/yourusername/RestApis#readme",
    },
) 