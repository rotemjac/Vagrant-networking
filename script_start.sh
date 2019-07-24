#!/usr/bin/env bash

python3.6 main.py
cd ./vagrantfile_builder/ && vagrant up
# mv ./vagrantfile_builder/outputs/ .