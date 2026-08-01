import requests
import xml.etree.ElementTree as ET
import urllib.parse
import json

# FL-07: Research Scout Agent (Core Logic)
# This script defines the tools and the prompt for the Custom GPT or local LLM agent.

SYSTEM_PROMPT = """
You are 'Research Scout', a highly technical academic research assistant for an AI Researcher.
When given a topic (e.g., "Federated Learning privacy"), you must:
1. Use the `search_arxiv` tool to find the 3 most relevant recent papers.
2. Read the abstracts and extract: (a) Problem, (b) Methodology, (c) Claimed Outcome.
3. Use the `search_github` tool to check if there is an official repository.
4. Format the output clearly. Never hallucinate DOIs or links.
"""

def search_arxiv(query, max_results=3):
    """Tool 1: Searches arXiv for recent papers matching the query."""
    print(f"[*] Agent Tool Execution: Searching arXiv for '{query}'...")
    safe_query = urllib.parse.quote(query)
    url = f"http://export.arxiv.org/api/query?search_query=all:{safe_query}&start=0&max_results={max_results}&sortBy=submittedDate&sortOrder=descending"
    
    response = requests.get(url)
    if response.status_code != 200:
        return "Error fetching from arXiv"
    
    root = ET.fromstring(response.content)
    papers = []
    
    # XML Namespace for arXiv
    ns = {'atom': 'http://www.w3.org/2005/Atom'}
    
    for entry in root.findall('atom:entry', ns):
        title = entry.find('atom:title', ns).text.strip().replace('\n', ' ')
        summary = entry.find('atom:summary', ns).text.strip().replace('\n', ' ')
        link = entry.find('atom:id', ns).text
        papers.append({'title': title, 'summary': summary, 'url': link})
        
    return papers

def search_github(paper_title):
    """Tool 2: Searches GitHub to see if code is available for the paper."""
    print(f"[*] Agent Tool Execution: Searching GitHub for '{paper_title}'...")
    # Using GitHub search API (rate limited without auth, but works for basic queries)
    safe_title = urllib.parse.quote(paper_title)
    url = f"https://api.github.com/search/repositories?q={safe_title}&per_page=1"
    
    headers = {'Accept': 'application/vnd.github.v3+json'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        if data.get('total_count', 0) > 0:
            repo = data['items'][0]
            return f"Found Repo: {repo['html_url']} (Stars: {repo['stargazers_count']})"
    
    return "No official public repository found."

# --- Example Agent Execution Loop ---
if __name__ == "__main__":
    print("=== Research Scout Agent Initialized ===")
    user_query = "Federated Learning privacy secure aggregation"
    print(f"User: Find recent papers on '{user_query}' and check for code.")
    
    # 1. Agent calls arXiv tool
    results = search_arxiv(user_query)
    
    # 2. Agent processes and formats results
    print("\n=== Agent Output ===")
    if not results:
        print("No papers found.")
    else:
        for i, paper in enumerate(results, 1):
            print(f"\n{i}. Title: {paper['title']}")
            print(f"   URL: {paper['url']}")
            # 3. Agent calls GitHub tool
            github_status = search_github(paper['title'])
            print(f"   Code Availability: {github_status}")
            print(f"   Methodology Summary: {paper['summary'][:200]}...")