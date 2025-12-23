# Add these methods to your Database class in database.py
# Replace the existing shiny hunt methods with these updated versions

async def set_shiny_hunt(self, user_id: int, guild_id: int, pokemon_names):
    """Set user's shiny hunt - supports single Pokemon or list of variants
    
    Args:
        pokemon_names: Either a string (single Pokemon) or list of strings (multiple variants)
    """
    # Normalize to list
    if isinstance(pokemon_names, str):
        pokemon_names = [pokemon_names]
    
    await self.db.shiny_hunts.update_one(
        {"user_id": user_id, "guild_id": guild_id},
        {"$set": {"pokemon": pokemon_names}},
        upsert=True
    )

async def clear_shiny_hunt(self, user_id: int, guild_id: int):
    """Clear user's shiny hunt"""
    result = await self.db.shiny_hunts.delete_one(
        {"user_id": user_id, "guild_id": guild_id}
    )
    return result.deleted_count > 0

async def get_user_shiny_hunt(self, user_id: int, guild_id: int):
    """Get user's current shiny hunt
    
    Returns:
        List of Pokemon names, or None if no hunt active
    """
    hunt = await self.db.shiny_hunts.find_one(
        {"user_id": user_id, "guild_id": guild_id}
    )
    if not hunt:
        return None
    
    pokemon = hunt.get('pokemon')
    
    # Handle backward compatibility - convert string to list
    if isinstance(pokemon, str):
        return [pokemon]
    
    return pokemon if pokemon else None

async def get_shiny_hunters_for_pokemon(self, guild_id: int, pokemon_names: List[str], afk_users: List[int]) -> List[int]:
    """Get all users hunting any of the Pokemon names
    
    Args:
        guild_id: Guild ID
        pokemon_names: List of Pokemon names to check (spawned Pokemon)
        afk_users: List of user IDs who are AFK
    
    Returns:
        List of tuples: (user_id, is_afk)
    """
    afk_users_set = set(afk_users)
    pokemon_names_set = set(pokemon_names)
    hunters = []

    # Get all hunts in this guild
    hunts = await self.db.shiny_hunts.find(
        {"guild_id": guild_id},
        {"user_id": 1, "pokemon": 1}
    ).to_list(length=None)

    for hunt in hunts:
        user_id = hunt['user_id']
        hunt_pokemon = hunt.get('pokemon', [])
        
        # Handle backward compatibility - convert string to list
        if isinstance(hunt_pokemon, str):
            hunt_pokemon = [hunt_pokemon]
        
        # Check if any spawned Pokemon matches any hunted Pokemon (exact match)
        if any(spawned in hunt_pokemon for spawned in pokemon_names_set):
            hunters.append((user_id, user_id in afk_users_set))

    return hunters
