from ddgs import DDGS


def search(query, max_results=5):
    """Web search"""
    with DDGS() as ddgs:
        return list(ddgs.text(query, max_results=max_results))


def search_news(query, max_results=5):
    """News search"""
    with DDGS() as ddgs:
        return list(ddgs.news(query, max_results=max_results))


def search_images(query, max_results=5):
    """Image search"""
    with DDGS() as ddgs:
        return list(ddgs.images(query, max_results=max_results))