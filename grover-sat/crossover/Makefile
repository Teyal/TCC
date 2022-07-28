.PHONY: run
run: 
	poetry run ket src/quant_sat.ket

.PHONY: test
test: 
	poetry run ket tests/test_crossover.ket

.PHONY: single
single: 
	poetry run ket src/quant_sat_single.ket

.PHONY: print
print: 
	poetry run ket src/print.py

.PHONY: gen
gen:
	poetry run python sats/gen_sats_ranges.py
	poetry run python sats/gen_sat.py