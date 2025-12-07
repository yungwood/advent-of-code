import click
from bs4 import Tag
from bs4.element import NavigableString

STYLE_MAP = {
    "code": {"fg": "bright_cyan"},
    "em": {"bold": True},
    "h2": {"fg": "bright_white", "bold": True},
    "pre": {"bg": "bright_black"},
}


def merge_styles(style_stack: list[dict]) -> dict:
    """Merge a stack of style dicts into one kwargs dict."""
    merged: dict = {}
    for s in style_stack:
        merged.update(s)
    return merged


def render(node, style_stack: list[dict] | None = None) -> str:
    if style_stack is None:
        style_stack = []

    parts: list[str] = []

    for child in node.children:
        if isinstance(child, NavigableString):
            text = str(child)
            style_kwargs = merge_styles(style_stack)
            if style_kwargs:
                lines = text.splitlines()
                if len(lines) > 1:
                    parts.extend(
                        "\n".join([click.style(line, **style_kwargs) for line in lines])
                    )
                else:
                    parts.append(click.style(text, **style_kwargs))
            else:
                text = text.lstrip("\n")
                parts.append(text)
            continue

        if not isinstance(child, Tag):
            continue

        tag = child.name.lower()
        tag_style = STYLE_MAP.get(tag)

        if tag_style:
            new_stack = style_stack + [tag_style]
        else:
            new_stack = style_stack

        parts.append(render(child, new_stack))

        if child.name in ["h2", "p", "pre"]:
            parts.append("\n\n")
        elif child.name in ["li"]:
            parts.append("\n")

    return "".join(parts)
