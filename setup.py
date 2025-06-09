from setuptools import setup, find_packages

setup(
    name="clip_dinoiser",
    version="0.1",
    packages=find_packages(),  # Automatically finds your Python packages
    install_requires=[
        # List dependencies here, or leave empty if you're managing them elsewhere
        "torch",
        "transformers",
        "tqdm",
        "Pillow"
    ],
    author="Seth Knoop",
    description="Custom version of CLIP-Dinoiser adapted for integration",
)
