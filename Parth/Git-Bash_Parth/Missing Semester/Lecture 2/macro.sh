#!/bin/sh
macro(){
    PATH_VAR=$(pwd)
    export PATH_VAR
}
polo(){
    cd "$PATH_VAR"
}