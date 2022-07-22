.PHONY: run
run: 
	poetry run ket src/quant_sat.ket

.PHONY: test
test: 
	poetry run ket tests/test_nightly.ket

.PHONY: single
single: 
	poetry run ket src/quant_sat_single.ket

.PHONY: print
print:
	poetry run python output/print.py