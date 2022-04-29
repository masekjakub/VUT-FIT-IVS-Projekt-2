# all (spustí progam)
# pack (zabalí projekt tak, aby mohl být odevzdán)
# clean (smaže všechny soubory, co nemají být odevzdány)
# run (spustí program)
# test (spustí testy matematické knihovny)
# doc (spustí generování dokumentace)
# profile (spustí program pro výpočet směrodatné odchylky s ukázkovým testovacím vstupem)
# help (vypíše nápovědu s popisem, co je potřeba udělat před spuštěním programu)

# This file is part of CubiCulator.
# CubiCulator is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# CubiCulator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with Foobar. If not, see <https://www.gnu.org/licenses/>.

SHELL := /bin/bash
PYTHON=python3
CALCULATOR=calculator.py
TESTSFILE=test_calcLib.py
DOXYFILE=Doxyfile
PROFILING=profiling.py
PROFILINGDATA=profilingData.txt
INSTALLATOR=CubiCulator_v1-2_setup.exe
ARCHIVE=xkucha30_xmasek19_xpolom00_xzelen27.zip

.PHONY: all pack clean run test doc profile help

all: $(CALCULATOR)
	$(PYTHON) $<
pack: $(INSTALLATOR)
#Create folders
	mkdir -p ../$(ARCHIVE)
	mkdir -p ../$(ARCHIVE)/doc ../$(ARCHIVE)/install ../$(ARCHIVE)/repo
#Copy repository
	rsync -av --progress .. ../$(ARCHIVE)/repo --exclude $(ARCHIVE)
#Generate and move documentation
	doxygen
	mv ../html ../$(ARCHIVE)/doc
#Move installator
	mv ../installer/$(INSTALLATOR) ../$(ARCHIVE)/install
#Zip archive
	zip ../$(ARCHIVE).zip ../$(ARCHIVE)
	rm -r -f ../$(ARCHIVE)

clean:
#Removes Doxygen documentation
	rm -r -f -d ../html
#Removes manual.pdf (generated from manual.tex)
	rm -r -f manual.pdf
#Removes python generated files
	rm -r -f -d __pycache__
	rm -r -f -d .pytest_cache
#Removes installer
	rm -r -f $(INSTALLATOR)
#Removes packed archive
	rm -r -f ../$(ARCHIVE).zip
run: $(CALCULATOR)
	$(PYTHON) $<
test: $(TESTSFILE)
	pytest $<
doc: $(DOXYFILE)
	doxygen $<
profile: $(PROFILING)
	$(PYTHON) $< <$(PROFILINGDATA)
help:
	$(info This Makefile is meant for linux)
	$(info all      Runs the program)
	$(info -          You need to have python3,PyQt5 and keyboard installed)
	$(info pack     Packs the project, so it can be submitted)
	$(info -          You need to have doxygen and zip installed and generated installer)
	$(info clean    Deletes all files, that are not supposed to be submitted)
	$(info run      Runs the program)
	$(info -          You need to have python3,PyQt5 and keyboard installed)
	$(info test     Runs tests for mathematical library)
	$(info -          You need to have python3 and pytest installed)
	$(info doc      Runs documentation generation)
	$(info -          You need to have doxygen installed)
	$(info profile  Runs the program for calculating standard deviation with refrence test input)
	$(info -          You need to have python3 installed)
	$(info help     Prints this message)
	@echo ""