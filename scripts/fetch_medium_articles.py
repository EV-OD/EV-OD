#!/usr/bin/env python3
"""
Fetch latest articles from Medium and update README.md
"""

import feedparser
import os
from datetime import datetime

# Medium RSS feed URL
MEDIUM_RSS_URL = "https://medium.com/feed/@allwcons"

# Number of latest articles to fetch
NUM_ARTICLES = 5


def fetch_medium_articles():
    """Fetch latest articles from Medium RSS feed"""
    try:
        feed = feedparser.parse(MEDIUM_RSS_URL)
        articles = []
        
        for entry in feed.entries[:NUM_ARTICLES]:
            article = {
                'title': entry.title,
                'link': entry.link,
                'published': entry.published,
                'summary': entry.summary if hasattr(entry, 'summary') else ''
            }
            articles.append(article)
        
        return articles
    except Exception as e:
        print(f"Error fetching Medium articles: {e}")
        return []


def format_articles(articles):
    """Format articles for README"""
    if not articles:
        return "- [Visit Medium Profile](https://medium.com/@allwcons) — *No articles found*\n"
    
    markdown = ""
    for article in articles:
        # Parse date
        try:
            date_obj = datetime.strptime(article['published'][:10], '%Y-%m-%d')
            date_str = date_obj.strftime('%b %d, %Y')
        except:
            date_str = article['published'][:10]
        
        # Format article line
        markdown += f"- [{article['title']}]({article['link']}) — *{date_str}*\n"
    
    return markdown


def update_readme(articles_markdown):
    """Update README.md with fetched articles"""
    readme_path = "README.md"
    
    if not os.path.exists(readme_path):
        print(f"Error: {readme_path} not found")
        return False
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find and replace the articles section
    start_marker = "### 📝 Latest Articles\n"
    end_marker = "\n---"
    
    start_idx = content.find(start_marker)
    if start_idx == -1:
        print("Error: Could not find '### 📝 Latest Articles' section in README.md")
        return False
    
    start_idx += len(start_marker)
    end_idx = content.find(end_marker, start_idx)
    if end_idx == -1:
        print("Error: Could not find end marker in README.md")
        return False
    
    # Build new content
    new_content = (
        content[:start_idx] +
        "\n" +
        articles_markdown +
        content[end_idx:]
    )
    
    # Write back to README
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ Updated README.md with {len(articles_markdown.strip().split(chr(10)))} articles")
    return True


def main():
    print("🔍 Fetching latest Medium articles...")
    articles = fetch_medium_articles()
    
    if articles:
        print(f"📚 Found {len(articles)} articles")
        articles_markdown = format_articles(articles)
        print("\nFormatted articles:")
        print(articles_markdown)
        
        if update_readme(articles_markdown):
            print("\n✅ README.md updated successfully!")
        else:
            print("\n❌ Failed to update README.md")
    else:
        print("⚠️  No articles fetched, skipping README update")


if __name__ == "__main__":
    main()
