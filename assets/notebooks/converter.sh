for notebook in "$@" 
do
    jupyter nbconvert --to html $notebook --output-dir ../;
done