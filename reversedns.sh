#!/bin/bash
for ipm in $(seq 1 254);
do
host $1.$ip
done
