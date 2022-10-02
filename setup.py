import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="tongliao",
    version="0.0.1",
    license="GPLv3+",
    author="Nemo2011",
    description="通辽转换器！",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=[
        "tongliao"
    ],
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    package_data={"": ["data/**/*.*", "requirements.txt", "data/*.*", "html/*.*"]},
    url="https://github.com/nemo2011/bilibili-api",
    python_requires=">=3.6"
)
