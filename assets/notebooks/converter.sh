for notebook in "$@" 
do
    jupyter nbconvert --to html "ipynb/"$notebook".ipynb" --output-dir ./pages;
    python3 add_button.py "pages/"$notebook".html" "ipynb/"$notebook".ipynb"
done