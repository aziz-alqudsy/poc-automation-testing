#!/bin/bash
python -m pytest -sv --html reports/report.html
tail -f /dev/null
