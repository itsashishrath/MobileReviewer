import re

# Sample text input
text = """
### Review of Samsung Galaxy S24 Ultra:

The Samsung Galaxy S24 Ultra has been met with widespread acclaim, touted as a peak slab phone (1) and one of the best phones available (2). With its powerful hardware, innovative features, and software enhancements, the S24 Ultra sets the bar high in the 2024 flagship phone market.

**Display**: 
- The 6.8-inch Quad HD AMOLED display is exceptionally sharp and bright, reaching a peak brightness of 2600 nits (1). 
- It features a completely flat design with some of the thinnest bezels seen on any phone (1), which many reviewers found to be a welcome change (3, 4).
- The display is protected by Gorilla Glass Armor, offering improved scratch and drop resistance (2, 3).
- The display is also said to have a 75% reduction in glare compared to previous models (2, 3).

**Performance**: 
- Powered by the Snapdragon 8 Gen 3 processor (1), the S24 Ultra delivers top-notch performance with rapid app loading and smooth multitasking (1, 2, 4).
- The phone boasts 12 GB of RAM, making it a multitasking champion (1).
- The S24 Ultra incorporates a larger vapor chamber for improved cooling during prolonged gaming sessions (1).

**Camera**:
- The camera system is highly versatile, featuring a 200MP primary camera (1, 2), 12MP ultra-wide camera (3), 50MP 5x telephoto camera (1, 2), and a 10MP 3x telephoto camera (1).
- The zoom capabilities are considered one of the best features, with smooth transitions between optical zoom levels (2, 4, 5).
- The camera system excels in low-light conditions (1, 4) and delivers vibrant shots with good color balance (2).
- Some reviewers noted that images can appear overly sharpened at times (2).
- The S24 Ultra incorporates Google's Ultra HDR format for enhanced photo quality (1).

**Battery Life**:
- The S24 Ultra features a 5000mAh battery that delivers impressive battery life (1, 2).
- Reviewers achieved long screen-on times, often exceeding six hours with moderate usage (1, 2).
- The phone also boasts excellent standby battery life (2).

**Software**:
- One UI, Samsung's custom skin over Android, provides a more customizable and flexible operating system than iOS (4).
- The S24 Ultra introduces Galaxy AI features, including Circle to Search (1, 4, 5), Live Translate (5), and Generative Edit (4, 5).
- The S24 Ultra offers seven years of security updates and seven generations of major software updates (1).

**Build Quality**:
- The S24 Ultra features a titanium frame (3, 4), making it more durable and premium than previous models. 
- The phone's weight can be a concern for some users (2, 4).

**Pros**:
- Excellent display quality (1, 2, 3, 4)
- Powerful performance (1, 2, 4)
- Impressive camera system (1, 2, 4, 5)
- Long battery life (1, 2)
- Customizable software (1, 4, 5)
- Premium build quality (2, 3, 4)
- S Pen compatibility (1, 4)
- Excellent software support with seven years of updates (1)

**Cons**:
- Can be bulky and heavy (2, 4)
- Camera processing can be inconsistent (2, 3)
- Some reviewers found the display to be overly saturated (5)

**Overall**: The Samsung Galaxy S24 Ultra is a powerful and feature-rich phone that excels in many areas, offering a compelling combination of hardware and software. While the phone does have a few minor drawbacks, it remains a top contender in the premium smartphone market. (1, 2, 3, 4, 5)
"""

# Function to parse the review text
def parse_review(text):
    # Extract title
    title = re.search(r'### (.+?):', text).group(1).strip()

    # Extract overall description
    overall_description = re.search(r'Overall\:\s*(.+)', text, re.DOTALL).group(1).strip()

    # Extract subtopics and their content
    subtopics = re.findall(r'\*\*(.+?)\*\*:\s*(.+?)(?=\*\*|$)', text, re.DOTALL)

    # Create a structured dictionary to hold the parsed data
    review_structure = {
        "title": title,
        "overall_description": overall_description,
        "subtopics": {}
    }

    # Fill the subtopics into the structure
    for subtopic, content in subtopics:
        review_structure["subtopics"][subtopic.strip()] = [line.strip() for line in content.strip().splitlines() if line.strip()]

    return review_structure

# Parse the review text
parsed_review = parse_review(text)

# Print the structured output
import pprint
pprint.pprint(parsed_review)