"""Generate the code reference pages.
Modified script from the `mkdocstrings` documentation:
    https://mkdocstrings.github.io/recipes/#automatic-code-reference-pages
"""

from pathlib import Path

import mkdocs_gen_files

nav = mkdocs_gen_files.Nav()

root = Path(__file__).parent.parent
src = root / "src"

for path in sorted(src.rglob("*.py")):
    relative_source_path = path.relative_to(src)

    module_path = relative_source_path.with_suffix("")
    module_name = module_path.parts[-1]

    if module_name == "__init__" or module_name == "__main__":
        continue

    # Remove the package name from the path
    relative_docs_path = relative_source_path.relative_to(relative_source_path.parts[0])

    titlecase_name = relative_docs_path.stem.title().strip("_").replace("_", " ")
    titlecase_docs_path = Path(relative_docs_path.parent, f"{titlecase_name}.md")

    full_doc_path = Path("reference", titlecase_docs_path)

    # Make title case the section nav names
    nav_route_path = tuple(
        map(lambda nav_path: nav_path.title(), full_doc_path.parent.parts)
    )
    nav[(*nav_route_path, titlecase_name)] = titlecase_docs_path.as_posix()

    with mkdocs_gen_files.open(full_doc_path, "w") as fd:
        identifier = ".".join(module_path.parts)
        print(f"::: {identifier}", file=fd)

    mkdocs_gen_files.set_edit_path(full_doc_path, path.relative_to(root))

with mkdocs_gen_files.open("reference/summary.md", "w") as nav_file:
    nav_file.writelines(nav.build_literate_nav())
