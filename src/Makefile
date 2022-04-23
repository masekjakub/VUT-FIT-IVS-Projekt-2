# all (spustí progam)
# pack (zabalí projekt tak, aby mohl být odevzdán)
# clean (smaže všechny soubory, co nemají být odevzdány)
# run (spustí program)
# test (spustí testy matematické knihovny)
# doc (spustí generování dokumentace)
# profile (spustí program pro výpočet směrodatné odchylky s ukázkovým testovacím vstupem)
# help (vypíše nápovědu s popisem, co je potřeba udělat před spuštěním programu)

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