source ./env/bin/activate
gen_date=$(date +"%m-%d-%y")
jupyter nbconvert --to python *.ipynb --output-dir=outputs