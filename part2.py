import re

def remove_tags(html_string):
    # Use regex to find all content between <li> tags, including potential inner <p> tags
    pattern = r'<li[^>]*>(.*?)</li>'
    matches = re.findall(pattern, html_string, re.DOTALL)
    
    cleaned_results = []
    for match in matches:
        if not match.strip():  # Skip empty items
            continue
        # Remove any inner HTML tags (like <p>) and strip whitespace
        text = re.sub(r'<[^>]+>', '', match).strip()
        if text:  # Only add if there's actual text content
            cleaned_results.append(text)
    
    return cleaned_results

# Sample usage
results = """
<li>100% Cotton</li>
<li class="highlight-gray">Imported</li>
<li></li>
<li><p>Machine Wash in Cold Water</p></li>
"""

print(remove_tags(results))
# Output: ["100% Cotton", "Imported", "Machine Wash in Cold Water"]