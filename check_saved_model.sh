#!/bin/sh

version=$1
saved_model_cli show --dir ./saved_model_twice_plus_three/$version --all
