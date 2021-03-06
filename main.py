import os
from nbconvert import MarkdownExporter

def main():
    work_dir = os.environ.get('GITHUB_WORKSPACE', '.')
    nb_filename = os.path.join(work_dir, 
        os.environ.get("INPUT_NB-FILENAME", 'notebook.ipynb')
    )
    md_filename = os.path.join(work_dir, os.environ.get("INPUT_MD-FILENAME", 'README.md'))


    print(f"::debug::Converting {nb_filename}")

    md_exporter = MarkdownExporter()
    # Convert the notebook to RST format
    (body, resources) = md_exporter.from_filename(nb_filename)
    print(f"::debug::Saving{md_filename}")

    with open(md_filename, 'w') as f:
        f.write(body)
    
    print(f"::set-output name=result::Converted {work_dir} to {work_dir}")

if __name__ == '__main__':
    main()