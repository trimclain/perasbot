SHELL := /bin/bash

all:
	@# Make sure pip and venv are installed
	sudo apt install -y python3-pip python3-venv

help:
	@echo "Run 'make' install missing packages"
	@echo "Run 'make venv' to create the venv"
	@echo "Run 'make install' after sourcing the venv" \
			"to install modules from requirements.txt"

venv:
	@# Create venv
	@if [[ ! -d "venv" ]]; then echo "Creating venv..." && \
		python3 -m venv venv && echo "Done"; \
		else echo "venv already exists"; fi

install_reqs:
	@# Install required modules
	@# pip install requests beautifulsoup4 python-telegram-bot
	pip install -r requirements.txt


.PHONY: all help venv install_reqs
