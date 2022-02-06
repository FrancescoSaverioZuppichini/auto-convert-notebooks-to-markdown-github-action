import os
from nbconvert import MarkdownExporter

def main():
    nb_filename = os.environ.get("INPUT_NB_FILENAME", 'notebook.ipynb')
    md_filename = os.environ.get("INPUT_MD_FILENAME", 'README.md')

    print(f"::debug::Converting {nb_filename}")

    md_exporter = MarkdownExporter()
    # Convert the notebook to RST format
    (body, resources) = md_exporter.from_filename(nb_filename)
    print(f"::debug::Saving{md_filename}")

    with open(md_filename, 'w') as f:
        f.write(body)

    print(f"::set-output name=state::Converted {nb_filename} to {md_filename}")

if __name__ == '__main__':
    main()