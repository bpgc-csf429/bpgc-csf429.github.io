# Notebook -> HTML
If you are doing it locally

Requirements:
- Python3
- Jupyter

```bash
bash converter.sh name_of_notebook1.ipynb name_of_notebook2.ipynb #and so on
```

If you are doing it on collaboratory copy this snippet

```python
!git clone https://github.com/bpgc-csf429/bpgc-csf429.github.io
%cd /content/bpgc-csf429.github.io/assets/notebooks
!bash converter.sh name_of_notebook1.ipynb name_of_notebook2.ipynb #and so on
```

Push the html files!
