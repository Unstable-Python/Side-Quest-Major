"""
Player Data Management
Handles saving/loading player progress, XP, unlocked regions, and quest completion.
"""

import json
import os
from datetime import date, datetime

class PlayerData:
    def __init__(self, save_file="adventure_save.json"):
        self.save_file = save_file
        self.data = self.load_data()
    
    def load_data(self):
        """Load player data from save file or create new data"""
        if os.path.exists(self.save_file):
            try:
                with open(self.save_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                pass
        
        # Default player data
        return {
            "xp": 0,
            "level": 1,
            "streak": 0,
            "last_activity": None,
            "unlocked_regions": [True, False, False, False, False],  # 5 regions total
            "daily_quests": {},  # date -> [completed_quest_ids]
            "inventory": [],
            "total_quests_completed": 0,
            "created_date": date.today().isoformat()
        }
    
    def save_data(self):
        """Save current player data to file"""
        try:
            with open(self.save_file, 'w') as f:
                json.dump(self.data, f, indent=2)
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def add_xp(self, amount):
        """Add XP and handle level ups"""
        old_level = self.get_level()
        self.data["xp"] += amount
        new_level = self.get_level()
        
        # Check for level up
        if new_level > old_level:
            self.handle_level_up(new_level)
        
        self.update_activity()
        self.save_data()
        
        return new_level > old_level  # Return True if leveled up
    
    def get_level(self):
        """Calculate current level based on XP"""
        xp = self.data["xp"]
        # Simple level formula: level = floor(sqrt(xp/10)) + 1
        import math
        return int(math.sqrt(xp / 10)) + 1
    
    def handle_level_up(self, new_level):
        """Handle level up rewards and region unlocking"""
        # Unlock new regions every 2 levels
        if new_level % 2 == 0 and new_level <= 10:
            region_index = min((new_level // 2) - 1, 4)
            if region_index < len(self.data["unlocked_regions"]):
                self.data["unlocked_regions"][region_index] = True
    
    def update_activity(self):
        """Update last activity and streak"""
        today = date.today().isoformat()
        last_activity = self.data.get("last_activity")
        
        if last_activity != today:
            # Check if streak should continue
            if last_activity:
                last_date = datetime.strptime(last_activity, "%Y-%m-%d").date()
                today_date = date.today()
                days_diff = (today_date - last_date).days
                
                if days_diff == 1:
                    # Consecutive day - continue streak
                    self.data["streak"] += 1
                elif days_diff > 1:
                    # Missed days - reset streak
                    self.data["streak"] = 1
                # Same day (days_diff == 0) - no change to streak
            else:
                # First activity ever
                self.data["streak"] = 1
            
            self.data["last_activity"] = today
    
    def complete_daily_quest(self, quest_id):
        """Mark a daily quest as completed"""
        today = date.today().isoformat()
        
        if today not in self.data["daily_quests"]:
            self.data["daily_quests"][today] = []
        
        if quest_id not in self.data["daily_quests"][today]:
            self.data["daily_quests"][today].append(quest_id)
            self.data["total_quests_completed"] += 1
            return True
        
        return False  # Already completed today
    
    def is_quest_completed_today(self, quest_id):
        """Check if a quest was completed today"""
        today = date.today().isoformat()
        return quest_id in self.data["daily_quests"].get(today, [])
    
    def add_inventory_item(self, item):
        """Add an item to player inventory"""
        self.data["inventory"].append({
            "item": item,
            "obtained_date": date.today().isoformat()
        })
        self.save_data()
    
    def get_stats_summary(self):
        """Get a summary of player stats"""
        return {
            "level": self.get_level(),
            "xp": self.data["xp"],
            "streak": self.data["streak"],
            "unlocked_regions": sum(self.data["unlocked_regions"]),
            "total_regions": len(self.data["unlocked_regions"]),
            "total_quests": self.data["total_quests_completed"],
            "inventory_count": len(self.data["inventory"])
        }