import subprocess
import os

def run_scraper(query, category, pages, verbose):
    input_data = f"{query}\n{category}\n{pages}\n{verbose}\n"
    process = subprocess.run(
        ['python', 'HackerNews.py'],
        input=input_data,
        capture_output=True,
        text=True
    )
    return process

if __name__ == "__main__":
    # Test with a query
    process = run_scraper("test", "story", "1", "n")
    print("--- Testing with query ---")
    print(process.stdout)
    print(process.stderr)

    file_path = f"HackerNews/test_story_NewsPage1.txt"
    if os.path.exists(file_path):
        print(f"File '{file_path}' created successfully.")
    else:
        print(f"File '{file_path}' not found.")

    # Test without a query
    process = run_scraper("", "story", "1", "n")
    print("\n--- Testing without query ---")
    print(process.stdout)
    print(process.stderr)

    file_path = f"HackerNews/_story_NewsPage1.txt"
    if os.path.exists(file_path):
        print(f"File '{file_path}' created successfully.")
    else:
        print(f"File '{file_path}' not found.")
