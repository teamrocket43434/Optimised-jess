"""Starboard utility functions"""
import json
import os
from typing import Optional, Dict
from config import STARBOARD_DATA_PATH, Emojis

def load_starboard_data() -> Dict:
    """Load Pokemon image data from starboard.txt"""
    try:
        with open(STARBOARD_DATA_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading starboard data: {e}")
        return {}

def get_gender_emoji(gender: Optional[str]) -> str:
    """Get gender emoji based on gender"""
    if gender == 'male':
        return Emojis.MALE
    elif gender == 'female':
        return Emojis.FEMALE
    elif gender == 'unknown':
        return Emojis.UNKNOWN
    else:
        return ""

def find_pokemon_image_url(pokemon_name: str, is_shiny: bool = False, gender: Optional[str] = None, is_gigantamax: bool = False) -> Optional[str]:
    """Find Pokemon image URL from starboard data with gender and Gigantamax support"""
    pokemon_data = load_starboard_data()
    normalized_name = pokemon_name.strip().lower()
    
    # Special case for Eternatus with Gigantamax factor
    if is_gigantamax and normalized_name == "eternatus":
        eternamax_name = "eternamax eternatus"
        
        for key, value in pokemon_data.items():
            if key.startswith('variant_') and 'eternamax' in key.lower():
                pokemon_display_name = value.get('name', '').lower()
                if eternamax_name == pokemon_display_name:
                    base_url = value.get('image_url', '')
                    if is_shiny and base_url:
                        return base_url.replace('/images/', '/shiny/')
                    return base_url
    
    # If it's Gigantamax (but not Eternatus), search for Gigantamax variant
    elif is_gigantamax:
        gigantamax_name = f"gigantamax {normalized_name}"
        
        for key, value in pokemon_data.items():
            if key.startswith('variant_') and 'gigantamax' in key.lower():
                pokemon_display_name = value.get('name', '').lower()
                if gigantamax_name == pokemon_display_name:
                    base_url = value.get('image_url', '')
                    if is_shiny and base_url:
                        return base_url.replace('/images/', '/shiny/')
                    return base_url
    
    # Function to search for Pokemon with proper female variant handling
    def search_pokemon(search_name: str, prefer_female: bool = False) -> Optional[str]:
        # Try exact match
        for key, value in pokemon_data.items():
            pokemon_entry_name = value.get('name', '').lower()
            
            # Handle female variants
            if prefer_female and gender == 'female':
                if pokemon_entry_name == f"{search_name}_female":
                    return value.get('image_url', '')
            
            # Try exact match
            if pokemon_entry_name == search_name:
                return value.get('image_url', '')
        
        # Try partial matching
        for key, value in pokemon_data.items():
            pokemon_entry_name = value.get('name', '').lower()
            
            # Handle female variants in partial matching
            if prefer_female and gender == 'female':
                if f"{search_name}_female" in pokemon_entry_name or pokemon_entry_name in f"{search_name}_female":
                    return value.get('image_url', '')
            
            # Regular partial matching
            if search_name in pokemon_entry_name or pokemon_entry_name in search_name:
                return value.get('image_url', '')
        
        return None
    
    # Search for Pokemon image URL
    base_url = search_pokemon(normalized_name, prefer_female=True)
    
    # If female variant not found, try base name
    if base_url is None and gender == 'female':
        base_url = search_pokemon(normalized_name, prefer_female=False)
    
    if base_url and is_shiny:
        return base_url.replace('/images/', '/shiny/')
    
    return base_url

def format_iv_display(iv) -> str:
    """Format IV for display"""
    if iv == "Hidden":
        return "Hidden"
    elif iv == "???":
        return "???"
    else:
        return f"{iv}%"

def create_jump_button_view(message) -> Optional:
    """Create a view with jump to message button"""
    if not message:
        return None
    
    import discord
    view = discord.ui.View()
    jump_button = discord.ui.Button(
        label="Jump to Message",
        url=message.jump_url,
        emoji="🔗",
        style=discord.ButtonStyle.link
    )
    view.add_item(jump_button)
    return view
