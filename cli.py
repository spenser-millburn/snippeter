#!/usr/bin/env python3
"""
C++ Snippets CLI - A command-line tool for managing C++ code snippets.
"""

import typer
from typing import Optional
from rich.console import Console
from rich.table import Table
from rich.syntax import Syntax
from rich.panel import Panel
from rich.prompt import Prompt
import random
import http.server
import socketserver
import webbrowser
import threading
from pathlib import Path
from thefuzz import fuzz, process

from snippets import CPP_SNIPPETS

try:
    from InquirerPy import inquirer
    from InquirerPy.base.control import Choice
    INQUIRER_AVAILABLE = True
except ImportError:
    INQUIRER_AVAILABLE = False

app = typer.Typer(help="C++ code snippets manager")
console = Console()


def find_snippet(name: str) -> Optional[dict]:
    """Find a snippet by name."""
    for snippet in CPP_SNIPPETS:
        if snippet["name"] == name:
            return snippet
    return None


def filter_snippets(keyword: str) -> list:
    """Filter snippets by keyword in name or description."""
    keyword_lower = keyword.lower()
    return [
        s for s in CPP_SNIPPETS
        if keyword_lower in s["name"].lower() or keyword_lower in s["description"].lower()
    ]


@app.command()
def list(filter: Optional[str] = typer.Option(None, "--filter", "-f", help="Filter snippets by keyword")):
    """List all available C++ snippets."""
    snippets = CPP_SNIPPETS if not filter else filter_snippets(filter)

    if not snippets:
        console.print(f"[yellow]No snippets found matching '{filter}'[/yellow]")
        return

    table = Table(title="C++ Code Snippets", show_header=True, header_style="bold magenta")
    table.add_column("#", style="dim", width=4)
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Category", style="green", no_wrap=True)
    table.add_column("Description", style="white")

    for idx, snippet in enumerate(snippets, 1):
        table.add_row(
            str(idx),
            snippet["name"],
            snippet["category"],
            snippet["description"]
        )

    console.print(table)
    console.print(f"\n[dim]Total: {len(snippets)} snippets[/dim]")
    console.print(f"[dim]Use 'snippeter show <name>' to view a snippet[/dim]")


@app.command()
def show(
    name: str = typer.Argument(..., help="Name of the snippet to display"),
    copy: bool = typer.Option(False, "--copy", "-c", help="Copy snippet to clipboard")
):
    """Display a specific snippet with syntax highlighting."""
    snippet = find_snippet(name)

    if not snippet:
        console.print(f"[red]Error: Snippet '{name}' not found[/red]")
        console.print("[yellow]Use 'snippeter list' to see available snippets[/yellow]")
        raise typer.Exit(1)

    # Display snippet info
    console.print(Panel(
        f"[bold]{snippet['name']}[/bold]\n{snippet['description']}",
        title="Snippet Info",
        border_style="green"
    ))

    # Display code with syntax highlighting
    syntax = Syntax(snippet["snippet"], "cpp", theme="monokai", line_numbers=True)
    console.print(syntax)

    # Copy to clipboard if requested
    if copy:
        try:
            import pyperclip
            pyperclip.copy(snippet["snippet"])
            console.print("\n[green]✓ Copied to clipboard![/green]")
        except ImportError:
            console.print("\n[yellow]Warning: pyperclip not installed. Install it with: pip install pyperclip[/yellow]")
        except Exception as e:
            console.print(f"\n[red]Error copying to clipboard: {e}[/red]")


@app.command()
def search(keyword: str = typer.Argument(..., help="Keyword to search in snippets")):
    """Search snippets by keyword in name or description."""
    results = filter_snippets(keyword)

    if not results:
        console.print(f"[yellow]No snippets found matching '{keyword}'[/yellow]")
        return

    table = Table(title=f"Search Results for '{keyword}'", show_header=True, header_style="bold magenta")
    table.add_column("#", style="dim", width=4)
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Category", style="green", no_wrap=True)
    table.add_column("Description", style="white")

    for idx, snippet in enumerate(results, 1):
        table.add_row(
            str(idx),
            snippet["name"],
            snippet["category"],
            snippet["description"]
        )

    console.print(table)
    console.print(f"\n[dim]Found {len(results)} matching snippets[/dim]")


@app.command()
def fuzzy(
    query: str = typer.Argument(..., help="Fuzzy search query"),
    copy: bool = typer.Option(False, "--copy", "-c", help="Copy best match to clipboard"),
    limit: int = typer.Option(5, "--limit", "-l", help="Number of results to show")
):
    """Fuzzy search for snippets and optionally copy the best match."""
    # Calculate scores for each snippet with name prioritization
    scored_snippets = []
    for snippet in CPP_SNIPPETS:
        # Score the name heavily (weighted more)
        name_score = fuzz.ratio(query.lower(), snippet['name'].lower())
        # Score the description
        desc_score = fuzz.partial_ratio(query.lower(), snippet['description'].lower())
        # Combined score: prioritize name matches
        combined_score = max(name_score, desc_score * 0.7)
        scored_snippets.append((snippet, int(combined_score)))

    # Sort by score descending and take top results
    scored_snippets.sort(key=lambda x: x[1], reverse=True)
    results = scored_snippets[:limit]

    if not results or results[0][1] == 0:
        console.print(f"[yellow]No fuzzy matches found for '{query}'[/yellow]")
        return

    # Display results in a table
    table = Table(title=f"Fuzzy Search Results for '{query}'", show_header=True, header_style="bold magenta")
    table.add_column("#", style="dim", width=4)
    table.add_column("Score", style="yellow", width=7)
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Category", style="green", no_wrap=True)
    table.add_column("Description", style="white")

    matched_snippets = []
    for idx, (snippet, score) in enumerate(results, 1):
        matched_snippets.append((snippet, score))
        table.add_row(
            str(idx),
            f"{score}%",
            snippet["name"],
            snippet["category"],
            snippet["description"]
        )

    console.print(table)
    console.print(f"\n[dim]Found {len(results)} fuzzy matches[/dim]")

    # Always show the top result
    if matched_snippets:
        best_match = matched_snippets[0][0]
        console.print(Panel(
            f"[bold]{best_match['name']}[/bold] ({best_match['category']})\n{best_match['description']}",
            title=f"Top Match ({matched_snippets[0][1]}% confidence)",
            border_style="green"
        ))

        syntax = Syntax(best_match["snippet"], "cpp", theme="monokai", line_numbers=True)
        console.print(syntax)

        # Copy best match if requested
        if copy:
            try:
                import pyperclip
                pyperclip.copy(best_match["snippet"])
                console.print(f"\n[green]✓ Copied to clipboard![/green]")
            except ImportError:
                console.print("\n[yellow]Warning: pyperclip not installed. Install it with: pip install pyperclip[/yellow]")
            except Exception as e:
                console.print(f"\n[red]Error copying to clipboard: {e}[/red]")


@app.command()
def fuzzyi(
    copy: bool = typer.Option(False, "--copy", "-c", help="Copy selected snippet to clipboard")
):
    """Interactive fuzzy finder for snippets (like fzf)."""
    if not INQUIRER_AVAILABLE:
        console.print("[red]Error: InquirerPy not installed[/red]")
        console.print("[yellow]Install it with: pip install InquirerPy[/yellow]")
        raise typer.Exit(1)

    # Create choices for the fuzzy finder
    choices = []
    for snippet in CPP_SNIPPETS:
        choice_label = f"{snippet['name']} - {snippet['description']}"
        choices.append(Choice(value=snippet, name=choice_label))

    # Show fuzzy finder
    selected = inquirer.fuzzy(
        message="Search snippets:",
        choices=choices,
        default=None,
        max_height="70%",
        instruction="(Use fuzzy search to filter)",
    ).execute()

    if not selected:
        console.print("[yellow]No snippet selected[/yellow]")
        return

    # Display selected snippet
    console.print(Panel(
        f"[bold]{selected['name']}[/bold]\n{selected['description']}",
        title="Selected Snippet",
        border_style="green"
    ))

    syntax = Syntax(selected["snippet"], "cpp", theme="monokai", line_numbers=True)
    console.print(syntax)

    # Copy if requested or ask
    should_copy = copy
    if not should_copy:
        copy_choice = Prompt.ask("\n[bold]Copy to clipboard?[/bold]", choices=["y", "n"], default="n")
        should_copy = copy_choice == 'y'

    if should_copy:
        try:
            import pyperclip
            pyperclip.copy(selected["snippet"])
            console.print("[green]✓ Copied to clipboard![/green]")
        except ImportError:
            console.print("[yellow]Warning: pyperclip not installed. Install it with: pip install pyperclip[/yellow]")
        except Exception as e:
            console.print(f"[red]Error: {e}[/red]")


@app.command()
def info(name: str = typer.Argument(..., help="Name of the snippet")):
    """Show detailed information about a snippet."""
    snippet = find_snippet(name)

    if not snippet:
        console.print(f"[red]Error: Snippet '{name}' not found[/red]")
        raise typer.Exit(1)

    lines = snippet["snippet"].count('\n') + 1
    chars = len(snippet["snippet"])

    table = Table(title="Snippet Details", show_header=False, box=None)
    table.add_column("Field", style="bold cyan")
    table.add_column("Value", style="white")

    table.add_row("Name", snippet["name"])
    table.add_row("Description", snippet["description"])
    table.add_row("Lines of code", str(lines))
    table.add_row("Characters", str(chars))

    console.print(table)


@app.command()
def copy(name: str = typer.Argument(..., help="Name of the snippet to copy")):
    """Copy a snippet directly to clipboard."""
    snippet = find_snippet(name)

    if not snippet:
        console.print(f"[red]Error: Snippet '{name}' not found[/red]")
        raise typer.Exit(1)

    try:
        import pyperclip
        pyperclip.copy(snippet["snippet"])
        console.print(f"[green]✓ Copied '{snippet['name']}' to clipboard![/green]")
    except ImportError:
        console.print("[red]Error: pyperclip not installed[/red]")
        console.print("[yellow]Install it with: pip install pyperclip[/yellow]")
        raise typer.Exit(1)
    except Exception as e:
        console.print(f"[red]Error copying to clipboard: {e}[/red]")
        raise typer.Exit(1)


@app.command()
def interactive():
    """Interactive mode to browse and select snippets."""
    console.print(Panel("[bold cyan]Interactive Snippet Browser[/bold cyan]", border_style="blue"))

    # Display all snippets
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("#", style="dim", width=4)
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Category", style="green", no_wrap=True)
    table.add_column("Description", style="white")

    for idx, snippet in enumerate(CPP_SNIPPETS, 1):
        table.add_row(
            str(idx),
            snippet["name"],
            snippet["category"],
            snippet["description"]
        )

    console.print(table)

    # Prompt for selection
    choice = Prompt.ask(
        "\n[bold]Enter snippet number or name[/bold] (or 'q' to quit)",
        default="q"
    )

    if choice.lower() == 'q':
        console.print("[yellow]Exiting...[/yellow]")
        return

    # Try to parse as number first
    snippet = None
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(CPP_SNIPPETS):
            snippet = CPP_SNIPPETS[idx]
    else:
        snippet = find_snippet(choice)

    if not snippet:
        console.print(f"[red]Invalid selection: '{choice}'[/red]")
        return

    # Display selected snippet
    console.print(Panel(
        f"[bold]{snippet['name']}[/bold]\n{snippet['description']}",
        title="Selected Snippet",
        border_style="green"
    ))

    syntax = Syntax(snippet["snippet"], "cpp", theme="monokai", line_numbers=True)
    console.print(syntax)

    # Ask if user wants to copy
    copy_choice = Prompt.ask("\n[bold]Copy to clipboard?[/bold]", choices=["y", "n"], default="n")

    if copy_choice == 'y':
        try:
            import pyperclip
            pyperclip.copy(snippet["snippet"])
            console.print("[green]✓ Copied to clipboard![/green]")
        except ImportError:
            console.print("[yellow]pyperclip not installed. Install it with: pip install pyperclip[/yellow]")
        except Exception as e:
            console.print(f"[red]Error: {e}[/red]")


@app.command()
def random_snippet():
    """Display a random snippet for learning/practice."""
    snippet = random.choice(CPP_SNIPPETS)

    console.print(Panel(
        "[bold cyan]Random Snippet of the Day![/bold cyan]",
        border_style="blue"
    ))

    console.print(Panel(
        f"[bold]{snippet['name']}[/bold]\n{snippet['description']}",
        title="Snippet Info",
        border_style="green"
    ))

    syntax = Syntax(snippet["snippet"], "cpp", theme="monokai", line_numbers=True)
    console.print(syntax)


@app.command()
def stats():
    """Show statistics about the snippet collection."""
    total = len(CPP_SNIPPETS)
    total_lines = sum(s["snippet"].count('\n') + 1 for s in CPP_SNIPPETS)
    avg_lines = total_lines // total

    longest = max(CPP_SNIPPETS, key=lambda s: s["snippet"].count('\n'))
    shortest = min(CPP_SNIPPETS, key=lambda s: s["snippet"].count('\n'))

    table = Table(title="Snippet Collection Statistics", show_header=False, box=None)
    table.add_column("Metric", style="bold cyan")
    table.add_column("Value", style="white")

    table.add_row("Total snippets", str(total))
    table.add_row("Total lines of code", str(total_lines))
    table.add_row("Average lines per snippet", str(avg_lines))
    table.add_row("Longest snippet", f"{longest['name']} ({longest['snippet'].count(chr(10)) + 1} lines)")
    table.add_row("Shortest snippet", f"{shortest['name']} ({shortest['snippet'].count(chr(10)) + 1} lines)")

    console.print(table)


@app.command()
def web(
    port: int = typer.Option(8000, "--port", "-p", help="Port to run the web server on"),
    no_browser: bool = typer.Option(False, "--no-browser", help="Don't open browser automatically")
):
    """Start the web interface for browsing snippets."""
    import json
    import os

    # Get the directory where this script is located
    script_dir = Path(__file__).parent

    # Generate snippets.json if it doesn't exist or is outdated
    json_file = script_dir / "snippets.json"
    snippets_py = script_dir / "snippets.py"

    if not json_file.exists() or (snippets_py.exists() and json_file.stat().st_mtime < snippets_py.stat().st_mtime):
        console.print("[yellow]Generating snippets.json...[/yellow]")
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(CPP_SNIPPETS, f, indent=2, ensure_ascii=False)
        console.print("[green]✓ Generated snippets.json[/green]")

    # Change to script directory to serve files
    os.chdir(script_dir)

    class QuietHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
        def log_message(self, format, *args):
            # Only log errors
            if args[1][0] != '2':
                super().log_message(format, *args)

        def end_headers(self):
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
            super().end_headers()

    url = f"http://localhost:{port}/index.html"

    console.print(f"[bold green]Starting web server...[/bold green]")
    console.print(f"[cyan]URL:[/cyan] {url}")
    console.print(f"[cyan]Snippets:[/cyan] {len(CPP_SNIPPETS)}")
    console.print(f"\n[yellow]Press Ctrl+C to stop the server[/yellow]\n")

    # Open browser
    if not no_browser:
        def open_browser():
            import time
            time.sleep(0.5)  # Wait for server to start
            try:
                webbrowser.open(url)
            except Exception as e:
                console.print(f"[red]Could not open browser: {e}[/red]")

        threading.Thread(target=open_browser, daemon=True).start()

    # Start server
    try:
        with socketserver.TCPServer(("", port), QuietHTTPRequestHandler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        console.print("\n[green]Server stopped.[/green]")
    except OSError as e:
        if "Address already in use" in str(e):
            console.print(f"[red]Error: Port {port} is already in use. Try a different port with --port[/red]")
        else:
            console.print(f"[red]Error: {e}[/red]")


if __name__ == "__main__":
    app()
