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

PYTHON=python3
CALCULATOR=calculator.py
TESTSFILE=test_calcLib.py
DOXYFILE=Doxyfile
PROFILING=profiling.py

all: $(CALCULATOR)
	$(PYTHON) $<
pack:

clean:

run: $(CALCULATOR)
	$(PYTHON) $<
test: $(TESTSFILE)
	pytest $<
doc: $(DOXYFILE)
	doxygen $<
profile: $(PROFILING)
	$(PYTHON) $<
help:
