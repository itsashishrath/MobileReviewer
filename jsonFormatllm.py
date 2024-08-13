import re

def parse_review(review_text, video_info):
    # Initialize the result dictionary
    result = {
        'title': '',
        'shortDescription': '',
        'subtopics': {},
        'sources' : video_info
    }

    # Extract title
    title_match = re.search(r'###\s*(.+)', review_text)
    if title_match:
        result['title'] = title_match.group(1).strip()

    # Split the text into sections
    sections = re.split(r'\*\*(.+?)\*\*', review_text)

    # Extract description (everything between title and first subtopic)
    description_match = re.search(r'###.+?\n\n(.*?)(?=\*\*|\Z)', review_text, re.DOTALL)
    if description_match:
        result['shortDescription'] = description_match.group(1).strip()

    # Process each section
    for i in range(1, len(sections), 2):
        subtopic = sections[i].strip()
        content = sections[i+1].strip() if i+1 < len(sections) else ''
        
        # Remove colon from subtopic name and use as key
        subtopic_key = subtopic.rstrip(':').strip()
        
        # Remove any leading or trailing newlines and extra whitespace
        content = re.sub(r'^\s+|\s+$', '', content, flags=re.MULTILINE)
        
        # Check if the content has bullet points
        bullet_points = [item.strip()[1:].strip() for item in content.split('\n') if item.strip().startswith('-')]
        
        if bullet_points:
            # If there are bullet points, store them as a list
            result['subtopics'][subtopic_key] = bullet_points
        else:
            # If there are no bullet points, store the entire content as a single string
            result[subtopic_key] = content.strip()

    return result

# Example usage
review_text = """
### Review of the Samsung Galaxy S24 Ultra:

The Samsung Galaxy S24 Ultra has been met with widespread praise from reviewers, being lauded as a top-tier Android phone that pushes the boundaries of what a smartphone can be. 

**Display:**
- The S24 Ultra boasts a class-leading 6.8-inch Quad HD AMOLED display with a 120Hz refresh rate and a peak brightness of 2,600 nits, making it exceptional for outdoor viewing and minimizing glare (1).
- The new Gorilla Glass Armor reduces glare significantly, surpassing previous generations of Gorilla Glass (3).
- While reviewers appreciate the brightness and clarity, some found the anti-glare coating to mute the colors slightly (2).

**Performance:**
- Powered by the Snapdragon 8 Gen 3 processor and 12GB of RAM, the S24 Ultra delivers smooth and effortless performance, handling demanding tasks and multitasking with ease (1, 2, 4). 
- Samsung's One UI software enhances the Android experience with features like Modes and Routines, split-screen multitasking, and customizable edge panels (2).

**Pros:**
- Exceptional display with high brightness and low glare
- Powerful performance with the Snapdragon 8 Gen 3 processor
- Impressive camera system with versatile zoom capabilities

**Cons:**
- Anti-glare coating may mute colors slightly
- Phone can be heavy compared to some competitors
- Camera software may overprocess images at times

**Overall:**
the Phone_Name is a strong contender in its market segment, offering a blend of high-quality hardware and impressive performance, though there are areas where it could improve, particularly in software optimization (3).

**Additional Notes:**
This section doesn't have bullet points and will be stored as a single string.
"""
video_info = []
parsed_review = parse_review(review_text, video_info)
import json
print(json.dumps(parsed_review, indent=2))