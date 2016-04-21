#!/bin/bash

HOME=/var/www/dfun

uwsgi --master --die-on-term --emperor $HOME/conf/uwsgi.ini
