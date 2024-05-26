# Mobile Reviewer

A Python application to fetch YouTube video captions for a specific phone model and generate a concise, well-cited review using a Large Language Model (LLM).

## Table of Contents
1. [Project Title and Description](#project-title-and-description)
2. [Table of Contents](#table-of-contents)
3. [Installation](#installation)
4. [Usage](#usage)

## Project Title and Description
**Mobile Reviewer**: This project automates the process of gathering and analyzing YouTube reviews for a specific phone model, summarizing the pros and cons based on video captions and generating a professional review using an LLM.

## Installation
Follow these steps to install and run the Mobile Reviewer project on your local machine:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/mobilereviewer.git
    cd mobilereviewer
    ```

2. **Create and Activate a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Required Packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up API Keys**:
    - Obtain a YouTube Data API key from [Google Cloud Console](https://console.cloud.google.com/).
    - Obtain an API key for Google Generative AI from [Google AI](https://ai.google.dev/).
    - Set up the environment variables:
        ```bash
        export GOOGLEAPIKEY='your_youtube_data_api_key'
        export GEMINISTUDIOKEY='your_google_ai_api_key'
        ```

## Usage
1. **Run the Application**:
    ```bash
    python main.py
    ```

2. **Example Usage**:
    - The application will prompt you to enter the phone model you want to review.
    - It will then fetch captions from the top 5 YouTube videos related to that phone model.
    - Using the LLM, it generates a detailed review with citations to the respective videos.

3. **Sample Output**:
    ```
    Generated Review:
    The Samsung S24 Ultra has been reviewed extensively, with a variety of opinions across different aspects.

    **Camera Quality**:
    - The camera hardware is excellent, providing sharp and detailed photos. However, the software seems to lag behind, causing occasional issues with color accuracy and processing speed (3).
    - Several reviewers praised the low-light performance of the camera, noting that it captures clear and bright images even in poor lighting conditions (1, 4).

    **Battery Life**:
    - The battery life is impressive, lasting well over a day with moderate use (2).
    - Some reviewers mentioned that heavy gaming or video streaming can drain the battery faster than expected (5).

    **Performance**:
    - The phone's performance is top-notch, handling multitasking and demanding applications with ease (1, 2, 4).
    - There were a few mentions of occasional stutters when switching between apps quickly (3).

    **Build Quality**:
    - The build quality is solid, with a premium feel and durable materials used throughout (2, 5).
    - A couple of reviewers pointed out that the phone is slightly heavier than its competitors (4).

    **Display**:
    - The display is vibrant and bright, making it great for media consumption (1, 3).
    - However, some found the display to be overly saturated in certain conditions (5).

    Overall, the Samsung S24 Ultra is a strong contender in its market segment, offering a blend of high-quality hardware and impressive performance, though there are areas where it could improve, particularly in software optimization (3).
    ```

Feel free to explore and modify the code to suit your needs. Contributions are welcome!
