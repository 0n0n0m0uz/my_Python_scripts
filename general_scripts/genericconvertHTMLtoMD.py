def convert_html_img_tags_in_markdown_to_markdown_syntax(markdown_content):
    # Regular expression to find <img> tags
    img_tag_regex = r'<img\s+[^>]*src="([^"]*)"[^>]*alt="([^"]*)"(?:[^>]*title="([^"]*)")?[^>]*>'
    
    # Function to convert each match to Markdown
    def replace_with_markdown(match):
        url = match.group(1)
        alt_text = match.group(2)
        title = match.group(3)
        if title:
            return f'![{alt_text}]({url} "{title}")'
        else:
            return f'![{alt_text}]({url})'
    
    # Replace all instances of <img> tags with Markdown
    markdown_with_converted_images = re.sub(img_tag_regex, replace_with_markdown, markdown_content)
    
    return markdown_with_converted_images