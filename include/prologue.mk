# Update this file from a profile with:
# curl https://raw.githubusercontent.com/open-contracting/standard_profile_template/master/include/prologue.mk -o include/prologue.mk

# See http://clarkgrubb.com/makefile-style-guide#prologue
MAKEFLAGS += --warn-undefined-variables
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := all
.DELETE_ON_ERROR:
.SUFFIXES:
