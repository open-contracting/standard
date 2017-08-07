all

exclude_rule 'MD024' # Multiple headers with the same content (see https://github.com/markdownlint/markdownlint/issues/175)
exclude_rule 'MD013' # Line length (breaking lines in paragraphs produces longer diffs)
exclude_rule 'MD033' # Inline HTML (some files require HTML)
