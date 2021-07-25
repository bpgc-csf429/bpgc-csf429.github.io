# Notebook -> HTML
Store all your notebooks in the ipynb directory / upload them on collab in the ipynb directory and follow the next steps

## Local

Requirements:
- Python3
- Jupyter

```bash
bash converter.sh name_of_notebook1.ipynb name_of_notebook2.ipynb #and so on
#Add, Commit and Push
```

## Collaboratory

Set User
```bash
!git config --global user.email "you@example.com"
!git config --global user.name "Your Name"
```

Convert to html and add button
```python
!git clone https://github.com/bpgc-csf429/bpgc-csf429.github.io
%cd /content/bpgc-csf429.github.io/assets/notebooks
!bash converter.sh name_of_notebook1.ipynb name_of_notebook2.ipynb #and so on
```

Add, commit, and push the html files!
```bash
%cd /content/bpgc-csf429.github.io
!git add .
!git commit -m "Fix HTML Notebooks Button"
!git remote rm origin
!git remote add origin https://<your_username>:<your_password>@github.com/bpgc-csf429/bpgc-csf429.github.io.git
!git push --set-upstream origin master
```