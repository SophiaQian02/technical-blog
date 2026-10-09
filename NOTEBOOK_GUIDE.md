# Technical notebook editing guide

The technical blog is https://blog.sophiaqian.com/, published from `SophiaQian02/technical-blog`. The academic homepage remains at https://sophiaqian.com/ in its separate repository.

## Edit and preview

- `notebook/content/rubrics-and-rl.html`: English article body. Each FIG marker gives filename, intrinsic dimensions, caption, and PDF source page.
- `assets/rubric-rl/`: seven original experimental figures extracted from pages 15–17 of the supplied notes. The full private PDF is not published.
- `assets/notebook.css`: white-background serif styling, a centered 736px reading column, desktop side navigation, and mobile layouts.
- `assets/notebook.js`: search, category filters, reading progress, and active section links. No external dependencies.
- `scripts/build_notebook.py`: shared headers, navigation, article metadata, index cards, and generated routes.

Run `python3 scripts/build_notebook.py`, then `python3 -m http.server 8770 --bind 127.0.0.1`. Open http://127.0.0.1:8770/.

Commit sources and generated HTML together. GitHub Pages serves the main branch root. `.nojekyll` keeps the generated static site unchanged. Historical archive and taxonomy pages retain their layouts, with links to the removed article cleared. The GraphRAG article has been removed.

## Adding an article

Add the body under `notebook/content/`, generate it using `article()` in the builder, and add its card to the index. Add a link in the separate academic repository's `_pages/about.md` and `_pages/blog.md` as appropriate. The academic navigation's Technical Blog link points directly to the root notebook.

## Research provenance

The Rubric-RL article is a preliminary interpretation of the user-supplied “Rubric-based OPD” notes, especially pages 15–17. Figures are original extracted images, not digitized or fabricated data. Small differences are not presented as statistically significant. Generator/judge and rubric-version confounds are identified. Future directions are separated from completed experiments.

## Reading layout

Articles use a Georgia/system-serif reading layout inspired by the reference at https://nrehiew.github.io/blog/sft_rl_opd/. At widths above 1250px the contents panel sits to the left of the centered article; on smaller screens it is a collapsible Contents control. The index uses a simple article list. Figures remain available at full resolution. Styles and scripts carry a version query in the builder; update it when publishing visual changes to avoid stale cached assets.

## Domain and legacy links

`CNAME` must contain `blog.sophiaqian.com`. Aliyun DNS uses a `blog` CNAME pointing to `sophiaqian02.github.io`. The separate `SophiaQian02.github.io` repository only serves redirects for old URLs; do not publish blog content there. Local blog source remains in `/Users/qianfeifei/Sophia-blog-publish`.
