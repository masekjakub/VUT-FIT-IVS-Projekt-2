#	This file is part of CubiCulator.
#	CubiCulator is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#	CubiCulator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#	You should have received a copy of the GNU General Public License along with Foobar. If not, see https://www.gnu.org/licenses/.
#
#    CubiCulator is a desktop program, made by team EXPECT\_EQ(oznuk, false) as a second and final IVS project. It can calculate basic mathematical expressions.
#    Copyright (C) 2022 EXPECT\_EQ(oznuk, false) xkucha30 xzelen27 xpolom00 xmasek19
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#    
#    Contact mail: xkucha30@vutbr.cz
#
#    CubiCulator  Copyright (C) 2022  Kuchař Vojtěch, Zelenák Martin, Polomski Filip, Mašek Jakub
#    This program comes with ABSOLUTELY NO WARRANTY;
#    This is free software, and you are welcome to redistribute it
#    under certain conditions; type `show c' for details.

SHELL := /bin/bash
PYTHON=python3
CALCULATOR=calculator.py
TESTSFILE=test_calcLib.py
DOXYFILE=Doxyfile
PROFILING=profiling.py
PROFILINGDATA=profilingData.txt
INSTALLATOR=../installer/CubiCulator_v1-2_setup.exe
ARCHIVE=xkucha30_xmasek19_xpolom00_xzelen27

.PHONY: all pack clean run test doc profile help

all: $(CALCULATOR)
	$(PYTHON) $<
pack: $(INSTALLATOR)
#Generate documentation
	doxygen
#Create folders
	mkdir -p ../$(ARCHIVE)
	mkdir -p ../$(ARCHIVE)/doc ../$(ARCHIVE)/install ../$(ARCHIVE)/repo
#Move documentation
	mv ../html ../$(ARCHIVE)/doc
#Copy repository
	rsync -av --progress .. ../$(ARCHIVE)/repo --exclude $(ARCHIVE) --exclude .vscode --exclude .pytest_cache --exclude src/__pycache__ --exclude html
#Move installator
	cp ../installer/$(INSTALLATOR) ../$(ARCHIVE)/install
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
	rm -r -f -d ../.pytest_cache
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