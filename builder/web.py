from staticjinja import Site
from pathlib import Path

from .paths import web_template_dir, content_dir
from .content import ContentProvider



def build_site(version: str, config: dict, output_dir: Path):
    linked_content_dir = web_template_dir / "content"
    try:
        linked_content_dir.symlink_to(content_dir)
    except FileExistsError:
        pass

    provider = ContentProvider()
    site = Site.make_site(
        searchpath=str(web_template_dir),
        outpath=str(output_dir),
        env_globals={
            'version': version,
            'config': config,
            'provider': provider,
        },
        contexts=[(r".*\.md", provider.context)],
        rules=[(r".*\.md", provider.render)],
    )
    site.render()
    linked_content_dir.unlink()
