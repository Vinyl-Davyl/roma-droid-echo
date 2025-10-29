
import os
import aiohttp
import json
from src.utils.logger import setup_logger

# Setup logger
logger = setup_logger(__name__)

# Constants
FIREWORKS_API_URL = "https://api.fireworks.ai/inference/v1/completions"

async def get_api_key():
    """Get Fireworks API key from environment variables"""
    api_key = os.getenv("FIREWORKS_API_KEY")
    if not api_key:
        logger.error("FIREWORKS_API_KEY not found in environment variables. AI services will not function.")
        return None
    return api_key

async def get_ai_response(query, model="accounts/sentientfoundation-serverless/models/dobby-mini-unhinged-plus-llama-3-1-8b"):
    """Get AI response from Fireworks API"""
    api_key = await get_api_key()
    if not api_key:
        return "AI services are not configured. Please set FIREWORKS_API_KEY."
    
    # Enhance the prompt with ROMA context
    enhanced_prompt = (
        "You are ROMA Droid Echo, a helpful assistant connected to the Sentient ecosystem. "
        "You provide information about ROMA (Recursive Open Meta Agent) and Sentient. "
        "Be concise, helpful, and informative. If you don't know something, admit it politely. "
        "\n\nUser query: " + query
    )
    
    payload = {
        "model": model,
        "prompt": enhanced_prompt,
        "max_tokens": 500,
        "temperature": 0.7,
        "top_p": 0.9,
    }
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(FIREWORKS_API_URL, json=payload, headers=headers) as response:
                if response.status == 200:
                    result = await response.json()
                    return result.get('choices', [{}])[0].get('text', '').strip()
                else:
                    error_text = await response.text()
                    logger.error(f"API error: {response.status}, {error_text}")
                    return "Sorry, I'm having trouble connecting to my AI services right now. Please try again later."
    except Exception as e:
        logger.exception(f"Error calling Fireworks API: {e}")
        return "Sorry, I encountereded an error while processing your request. Please try again later."
        return "Sorry, I encountered an error while processing your request. Please try again later."

async def summarize_content(content, model="accounts/fireworks/models/mixtral-8x7b-instruct"):
    """Summarize content using Fireworks API"""
    api_key = await get_api_key()
    if not api_key:
        return "AI services are not configured. Please set FIREWORKS_API_KEY."
    
    # Check if content is a URL or text
    is_url = content.startswith("http") and " " not in content
    
    if is_url:
        prompt = f"Please summarize the content from this URL: {content}. Provide a concise summary highlighting the key points."
    else:
        prompt = f"Please summarize the following text:\n\n{content}\n\nProvide a concise summary highlighting the key points."
    
    payload = {
        "model": model,
        "prompt": prompt,
        "max_tokens": 800,
        "temperature": 0.5,
        "top_p": 0.9,
    }
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(FIREWORKS_API_URL, json=payload, headers=headers) as response:
                if response.status == 200:
                    result = await response.json()
                    return result.get('choices', [{}])[0].get('text', '').strip()
                else:
                    error_text = await response.text()
                    logger.error(f"API error: {response.status}, {error_text}")
                    return "Sorry, I'm having trouble summarizing that content right now. Please try again later."
    except Exception as e:
        logger.exception(f"Error calling Fireworks API: {e}")
        return "Sorry, I encountered an error while summarizing your content. Please try again later."
        return "Sorry, I encountered an error while summarizing your content. Please try again later."
