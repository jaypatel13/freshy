import requests as req
from loguru import logger
import random


class Scraper:

    user_agents = [ 
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36', 
	'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36', 
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36', 
	'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148', 
	'Mozilla/5.0 (Linux; Android 11; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36' 
    ]32 sz ``
    
    def scrape(self, url: str) -> str:
        
        user_agent = random.choice(self.user_agents) 
        headers = {'User-Agent': user_agent} 
        
        response = req.get(url, headers=headers)
        logger.info(f"Scraped {url} in {response.elapsed.total_seconds()} seconds")
        logger.debug(f"Request Code: {response.status_code}")
        
        return response.json()
