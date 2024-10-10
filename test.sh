#!/usr/bin/env bash

cd src
python -m unittest discover -s ../tests
cd -
