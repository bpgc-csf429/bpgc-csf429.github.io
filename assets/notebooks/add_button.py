import sys

if __name__ == "__main__":

    html = sys.argv[1]
    ipynb = sys.argv[2]
    flag = 0
    button = """\n<p align="center"><a href="https://colab.research.google.com/github/bpgc-csf429/bpgc-csf429.github.io/blob/master/assets/notebooks/test2.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open Collab"></a></p>\n"""
    button = button.replace("test2.ipynb", ipynb)
    with open(html, "r+") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if line.startswith(
                '<div class="text_cell_render border-box-sizing rendered_html">'
            ) and flag==0:
                lines[i] = lines[i] + button
                flag=1
        f.truncate()
        f.seek(0)
        for line in lines:
            f.write(line)
