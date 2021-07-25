for notebook in "$@" 
do
    jupyter nbconvert --to html "ipynb/"$notebook --output-dir ../pages;
done