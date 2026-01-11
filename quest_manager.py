"""
Quest Management System
Handles quest definitions, completion logic, and rewards.
"""

import random
from datetime import date

class QuestManager:
    def __init__(self, player_data):
        self.player_data = player_data
        self.quests = self.define_quests()
    
    def define_quests(self):
        """Define available quests with their rewards"""
        return {
            "file_organization": {
                "name": "File Organization",
                "description": "Organize files on your desktop or in a folder",
                "xp_reward": 10,
                "icon": "📁",
                "completion_messages": [
                    "Your digital space is now pristine!",
                    "Files organized like a true adventurer!",
                    "The chaos has been tamed!"
                ]
            },
            "work_session": {
                "name": "Work Session",
                "description": "Complete a focused work or study session",
                "xp_reward": 15,
                "icon": "💻",
                "completion_messages": [
                    "Productivity level: Maximum!",
                    "Another successful quest in the books!",
                    "Your focus powers grow stronger!"
                ]
            },
            "learning": {
                "name": "Learning Quest",
                "description": "Learn something new or practice a skill",
                "xp_reward": 20,
                "icon": "📚",
                "completion_messages": [
                    "Knowledge is the greatest treasure!",
                    "Your wisdom stat has increased!",
                    "The path of learning never ends!"
                ]
            }
        }
    
    def complete_quest(self, quest_id):
        """Complete a quest and award rewards"""
        if quest_id not in self.quests:
            return False
        
        # Check if already completed today
        if self.player_data.is_quest_completed_today(quest_id):
            return False
        
        quest = self.quests[quest_id]
        
        # Mark quest as completed
        if self.player_data.complete_daily_quest(quest_id):
            # Award XP
            leveled_up = self.player_data.add_xp(quest["xp_reward"])
            
            # Random chance for bonus rewards
            self.check_bonus_rewards(quest_id, leveled_up)
            
            return True
        
        return False
    
    def check_bonus_rewards(self, quest_id, leveled_up):
        """Check for and award bonus rewards"""
        # Level up bonus
        if leveled_up:
            self.player_data.add_inventory_item("🌟 Level Up Star")
        
        # Random treasure chance (10%)
        if random.random() < 0.1:
            treasures = ["💎 Rare Gem", "🏆 Achievement Trophy", "🎁 Mystery Box", "⚡ Energy Crystal"]
            treasure = random.choice(treasures)
            self.player_data.add_inventory_item(treasure)
        
        # Streak milestone rewards
        streak = self.player_data.data["streak"]
        if streak > 0 and streak % 7 == 0:  # Weekly streak
            self.player_data.add_inventory_item(f"🔥 {streak}-Day Streak Badge")
        
        # Quest milestone rewards
        total_quests = self.player_data.data["total_quests_completed"]
        milestones = [10, 25, 50, 100, 250, 500]
        if total_quests in milestones:
            self.player_data.add_inventory_item(f"🏅 {total_quests} Quest Milestone")
    
    def get_daily_quest_status(self):
        """Get status of all daily quests"""
        today = date.today().isoformat()
        completed_today = self.player_data.data["daily_quests"].get(today, [])
        
        status = {}
        for quest_id, quest_data in self.quests.items():
            status[quest_id] = {
                "completed": quest_id in completed_today,
                "quest_data": quest_data
            }
        
        return status
    
    def get_random_event(self):
        """Generate a random daily event (future feature)"""
        events = [
            {
                "title": "Treasure Chest Discovered!",
                "description": "A mysterious chest appeared on your map. Complete any quest to open it!",
                "reward": "💰 Gold Coins"
            },
            {
                "title": "Double XP Day!",
                "description": "The stars align perfectly. All quests give double XP today!",
                "reward": "2x XP Multiplier"
            },
            {
                "title": "Ancient Scroll Found!",
                "description": "You discovered an ancient scroll. It whispers of hidden knowledge...",
                "reward": "📜 Wisdom Scroll"
            }
        ]
        
        if random.random() < 0.15:  # 15% chance for random event
            return random.choice(events)
        
        return None