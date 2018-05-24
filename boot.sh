#!/usr/bin/env bash

PS1="(`basename \"$VIRTUAL_ENV\"`):/\W$ "

export _JAVA_OPTIONS=-Xmx4096m
#export ES_JAVA_OPTS="-Xms10g -Xmx10g" ./bin/elasticsearch
export ES_HEAP_SIZE=10g
