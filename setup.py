from setuptools import setup, find_packages

setup(
    name='ptyolov3',
    version='1.0.0',
    url='https://github.com/david-macleod/PyTorch-YOLOv3',
    description='Fork of eriklindernoren/PyTorch-YOLOv3 as an installable package',
    packages=find_packages(),    
    install_requires=[
        'numpy',
        'torch>=1.0',
        'torchvision',
        'matplotlib',
        'tensorflow',
        'tensorboard',
        'terminaltables',
        'pillow',
        'tqdm',
    ]
)