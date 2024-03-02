def convert_html_image_to_MD(markdown_content):
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
import os
import argparse
  # noqa: E302
def process_file(filepath):
    # Placeholder for file processing logic
    print(f"Processing {filepath}...")
  # noqa: E302
def process_directory(directory, extension):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                process_file(os.path.join(root, file))
  # noqa: E302
def main():
    parser=argparse.ArgumentParser(
        description="Process files with a specific extension recursively in directories.")
    parser.add_argument("path", help="Path to a file or directory")
    parser.add_argument("--ext", default=".txt",
                        help="File extension to process (default: .txt)")

    args=parser.parse_args()

    if os.path.isdir(args.path):
        process_directory(args.path, args.ext)
    elif os.path.isfile(args.path):
        if args.path.endswith(args.ext):
            process_file(args.path)
        else:
            print(f"The file does not have the expected extension: {args.ext}")
    else:
        print("The path provided does not exist.")

if __name__ == "__main__":
    main()
