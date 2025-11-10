#!/usr/bin/env python3
"""Generate snippets.json from snippets.py for the web frontend."""

import json
from snippets import CPP_SNIPPETS

def generate_json():
    """Convert Python snippets to JSON format for web frontend."""
    output_file = "snippets.json"

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(CPP_SNIPPETS, f, indent=2, ensure_ascii=False)

    print(f"✓ Generated {output_file} with {len(CPP_SNIPPETS)} snippets")

    # Print statistics
    categories = {}
    for snippet in CPP_SNIPPETS:
        cat = snippet['category']
        categories[cat] = categories.get(cat, 0) + 1

    print(f"\nCategories:")
    for cat, count in sorted(categories.items()):
        print(f"  {cat}: {count} snippets")

if __name__ == "__main__":
    generate_json()
