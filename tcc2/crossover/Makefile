.PHONY: run
run: 
	poetry run ket src/quant_sat.ket

.PHONY: gen
gen:
	poetry run python src/gen_sats_ranges.py
	poetry run python src/gen_sat.py