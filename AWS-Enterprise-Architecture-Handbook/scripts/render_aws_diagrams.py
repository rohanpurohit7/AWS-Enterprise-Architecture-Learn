from __future__ import annotations

import json
import os
from pathlib import Path
import runpy
import shutil

ROOT = Path("AWS-Enterprise-Architecture-Handbook")
CANONICAL = ROOT / "architecture-diagrams"
SOURCE = CANONICAL / "sources"
OUTPUT = CANONICAL / "rendered"
CATALOG = CANONICAL / "catalog.json"
ROOT_GALLERY = CANONICAL / "README.md"

# Compatibility locations retained as generated publication layers.
LEGACY_SOURCE = ROOT / "docs" / "diagrams" / "aws-diagrams"
LEGACY_OUTPUT = ROOT / "docs" / "diagrams" / "rendered"
LEGACY_GALLERY = ROOT / "docs" / "diagrams" / "README.md"

SOURCE.mkdir(parents=True, exist_ok=True)
OUTPUT.mkdir(parents=True, exist_ok=True)
LEGACY_OUTPUT.mkdir(parents=True, exist_ok=True)


def discover_architecture_sources() -> list[Path]:
    """Collect diagram definitions from architecture subfolders into the root renderer."""
    discovered: dict[str, Path] = {}
    candidates = sorted(ROOT.rglob("*.py"))
    for path in candidates:
        if CANONICAL in path.parents or path == Path(__file__):
            continue
        # Architecture diagram code must live in a diagram-oriented folder.
        lowered = {part.lower() for part in path.parts}
        if not ({"aws-diagrams", "architecture-diagrams", "diagrams"} & lowered):
            continue
        if path.name.startswith("__"):
            continue
        previous = discovered.get(path.name)
        if previous and previous.read_bytes() != path.read_bytes():
            raise SystemExit(
                f"Conflicting architecture sources named {path.name}: {previous} and {path}"
            )
        discovered[path.name] = path

    if not discovered:
        raise SystemExit("No Python AWS architecture sources were discovered")

    # Root-level source folder is regenerated to avoid stale stragglers.
    for old in SOURCE.glob("*.py"):
        old.unlink()
    for name, original in sorted(discovered.items()):
        shutil.copy2(original, SOURCE / name)
    return sorted(SOURCE.glob("*.py"))


def architecture_documents(stems: set[str]) -> dict[str, list[Path]]:
    """Find every handbook article that discusses a known architecture."""
    mapping: dict[str, list[Path]] = {stem: [] for stem in stems}
    ignored_parts = {"architecture-diagrams", "rendered", ".git", ".venv"}
    for document in sorted(ROOT.rglob("*.md")):
        if any(part in ignored_parts for part in document.parts):
            continue
        text = document.read_text(encoding="utf-8", errors="replace")
        lower_text = text.lower()
        for stem in stems:
            explicit_reference = any(
                token in lower_text
                for token in (
                    f"{stem}.py",
                    f"{stem}.puml",
                    f"{stem}.png",
                    f"{stem}.svg",
                )
            )
            if document.stem == stem or explicit_reference:
                mapping[stem].append(document)
    return mapping


def insert_managed_diagram_block(document: Path, stem: str) -> None:
    title = stem.replace("-", " ").title()
    local_image = Path("rendered") / f"{stem}.png"
    central_image = Path(os.path.relpath(OUTPUT / f"{stem}.png", document.parent))
    central_source = Path(os.path.relpath(SOURCE / f"{stem}.py", document.parent))
    start = "<!-- GENERATED_ARCHITECTURE_DIAGRAM:START -->"
    end = "<!-- GENERATED_ARCHITECTURE_DIAGRAM:END -->"
    block = "\n".join(
        [
            start,
            "",
            f"## Rendered Architecture Diagram",
            "",
            f"![{title}]({local_image.as_posix()})",
            "",
            f"[Central rendered asset]({central_image.as_posix()}) · "
            f"[Editable Python source]({central_source.as_posix()})",
            "",
            end,
        ]
    )
    text = document.read_text(encoding="utf-8", errors="replace")
    if start in text and end in text:
        prefix, remainder = text.split(start, 1)
        _, suffix = remainder.split(end, 1)
        updated = prefix.rstrip() + "\n\n" + block + suffix
    else:
        lines = text.splitlines()
        insert_at = 1 if lines and lines[0].startswith("# ") else 0
        lines[insert_at:insert_at] = ["", block, ""]
        updated = "\n".join(lines).rstrip() + "\n"
    document.write_text(updated, encoding="utf-8")


sources = discover_architecture_sources()
source_stems = {path.stem for path in sources}

# Clean all generated central and compatibility assets.
for directory in (OUTPUT, LEGACY_OUTPUT):
    for pattern in ("*.png", "*.svg"):
        for old in directory.glob(pattern):
            old.unlink()

# Existing source definitions emit into the compatibility output path. Execute the
# root-copied definitions, then promote the results into the canonical root folder.
for source in sources:
    print(f"Rendering root architecture source {source}")
    runpy.run_path(str(source), run_name="__main__")

legacy_rendered = sorted(LEGACY_OUTPUT.glob("*.png"))
legacy_stems = {path.stem for path in legacy_rendered}
if legacy_stems != source_stems:
    raise SystemExit(
        f"Rendered/source mismatch. Missing={sorted(source_stems - legacy_stems)}; "
        f"Extra={sorted(legacy_stems - source_stems)}"
    )

for image in legacy_rendered:
    shutil.copy2(image, OUTPUT / image.name)

# Distribute a local rendered copy into every subfolder where the architecture is discussed.
documents_by_stem = architecture_documents(source_stems)
catalog_entries: list[dict[str, object]] = []
for stem in sorted(source_stems):
    central_image = OUTPUT / f"{stem}.png"
    matched_docs = documents_by_stem.get(stem, [])
    local_assets: list[str] = []
    for document in matched_docs:
        local_dir = document.parent / "rendered"
        local_dir.mkdir(parents=True, exist_ok=True)
        local_image = local_dir / central_image.name
        shutil.copy2(central_image, local_image)
        insert_managed_diagram_block(document, stem)
        local_assets.append(local_image.as_posix())
    catalog_entries.append(
        {
            "architecture": stem,
            "source": (SOURCE / f"{stem}.py").as_posix(),
            "central_rendered_asset": central_image.as_posix(),
            "documents": [path.as_posix() for path in matched_docs],
            "local_rendered_assets": local_assets,
        }
    )

CATALOG.write_text(json.dumps({"architectures": catalog_entries}, indent=2), encoding="utf-8")

workflow_schematic = [
    "## How GitHub Actions Builds and Publishes the Diagrams",
    "",
    "```mermaid",
    "flowchart TD",
    "    A[Push to master or workflow_dispatch] --> B[Checkout repository]",
    "    B --> C[Install Python 3.12, Graphviz, diagrams]",
    "    C --> D[Discover diagram Python files across handbook subfolders]",
    "    D --> E[Copy sources into architecture-diagrams/sources]",
    "    E --> F[Validate every Python and AWS icon import]",
    "    F --> G[Run scripts/render_aws_diagrams.py]",
    "    G --> H[Execute each root source with runpy]",
    "    H --> I[Graphviz generates AWS-icon PNGs]",
    "    I --> J[Promote images into architecture-diagrams/rendered]",
    "    J --> K[Find matching architecture Markdown documents]",
    "    K --> L[Copy PNG into each document folder/rendered]",
    "    L --> M[Insert managed diagram links in each article]",
    "    M --> N[Generate catalog and gallery]",
    "    N --> O[Validate central and local publication coverage]",
    "    O --> P[github-actions bot commits generated assets]",
    "```",
    "",
    "### Source and command map",
    "",
    "| Stage | Source or command | Result |",
    "|---|---|---|",
    "| Discovery | `AWS-Enterprise-Architecture-Handbook/**/diagrams/**/*.py` | Architecture source inventory |",
    "| Root consolidation | `architecture-diagrams/sources/*.py` | Canonical editable definitions |",
    "| Renderer | `python AWS-Enterprise-Architecture-Handbook/scripts/render_aws_diagrams.py` | Executes all definitions |",
    "| Central publication | `architecture-diagrams/rendered/*.png` | Root diagram library |",
    "| Compatibility publication | `docs/diagrams/rendered/*.png` | Existing gallery paths remain valid |",
    "| Local publication | `<architecture-document-folder>/rendered/<name>.png` | Diagram beside the article/runbook |",
    "| Inventory | `architecture-diagrams/catalog.json` | Source-to-document-to-image traceability |",
    "",
]

lines = [
    "# AWS Architecture-as-Code Library",
    "",
    "This root-level folder is the canonical source and rendered asset library for architecture patterns discussed throughout the handbook.",
    "",
    *workflow_schematic,
]
for entry in catalog_entries:
    stem = str(entry["architecture"])
    title = stem.replace("-", " ").title()
    lines += [
        f"## {title}",
        "",
        f"![{title}](rendered/{stem}.png)",
        "",
        f"[Editable source](sources/{stem}.py)",
        "",
    ]
    for document in entry["documents"]:
        relative_doc = os.path.relpath(str(document), CANONICAL)
        lines.append(f"- [Architecture documentation]({Path(relative_doc).as_posix()})")
    lines.append("")

ROOT_GALLERY.write_text("\n".join(lines), encoding="utf-8")
LEGACY_GALLERY.write_text(
    "# AWS Architecture Diagram Gallery\n\n"
    "The canonical root library is [AWS Architecture-as-Code Library](../../architecture-diagrams/README.md).\n\n"
    + "\n".join(workflow_schematic)
    + "\n\n"
    + "\n".join(
        f"## {stem.replace('-', ' ').title()}\n\n![{stem}](rendered/{stem}.png)\n\n"
        f"[Root source](../../architecture-diagrams/sources/{stem}.py) · "
        f"[Root rendered asset](../../architecture-diagrams/rendered/{stem}.png)\n"
        for stem in sorted(source_stems)
    ),
    encoding="utf-8",
)

print(f"Consolidated {len(sources)} architecture sources into {SOURCE}")
print(f"Rendered {len(legacy_rendered)} central architecture images into {OUTPUT}")
print(f"Updated {sum(len(v) for v in documents_by_stem.values())} matching architecture documents")
