#!/bin/bash
if [ "$1" = 'api' ]; then
    python -m pytest -n 10 -sv api/ --html reports/report.html
elif [ "$1" = 'web' ]; then
    python -m pytest -n 10 -sv web/ --html reports/report.html
elif [ "$1" = 'mobile' ]; then
    python -m pytest -sv mobile/ --html reports/report.html
else
    echo 'platform not found!'
fi
