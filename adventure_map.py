"""
Adventure Map Visualization
Handles the visual representation of the player's progress through different regions.
"""

import tkinter as tk
import math

class AdventureMap:
    def __init__(self, player_data):
        self.player_data = player_data
        self.regions = self.define_regions()
        self.map_width = 600
        self.map_height = 300
    
    def define_regions(self):
        """Define the map regions and their properties"""
        return [
            {
                "name": "Starting Village",
                "description": "Your humble beginnings",
                "color": "#27ae60",
                "unlock_level": 1,
                "position": (100, 150),
                "size": 60,
                "icon": "🏘️"
            },
            {
                "name": "Mystic Forest",
                "description": "Ancient trees hold secrets",
                "color": "#2ecc71",
                "unlock_level": 2,
                "position": (250, 100),
                "size": 70,
                "icon": "🌲"
            },
            {
                "name": "Crystal Caves",
                "description": "Glittering depths await",
                "color": "#3498db",
                "unlock_level": 4,
                "position": (400, 200),
                "size": 65,
                "icon": "💎"
            },
            {
                "name": "Sky Temple",
                "description": "Floating among the clouds",
                "color": "#9b59b6",
                "unlock_level": 6,
                "position": (300, 50),
                "size": 75,
                "icon": "⛩️"
            },
            {
                "name": "Dragon's Peak",
                "description": "The ultimate challenge",
                "color": "#e74c3c",
                "unlock_level": 8,
                "position": (500, 120),
                "size": 80,
                "icon": "🐉"
            }
        ]
    
    def draw_map(self, canvas):
        """Draw the adventure map on the given canvas"""
        # Clear canvas
        canvas.delete("all")
        
        # Draw background
        self.draw_background(canvas)
        
        # Draw paths between regions
        self.draw_paths(canvas)
        
        # Draw regions
        self.draw_regions(canvas)
        
        # Draw player position indicator
        self.draw_player_indicator(canvas)
    
    def draw_background(self, canvas):
        """Draw the map background"""
        # Create a gradient-like background
        for i in range(0, self.map_height, 20):
            color_intensity = int(26 + (i / self.map_height) * 20)  # Gradient from dark to slightly lighter
            color = f"#{color_intensity:02x}{color_intensity + 5:02x}{color_intensity + 10:02x}"
            canvas.create_rectangle(0, i, self.map_width, i + 20, fill=color, outline="")
        
        # Add some decorative stars
        import random
        random.seed(42)  # Consistent star positions
        for _ in range(15):
            x = random.randint(20, self.map_width - 20)
            y = random.randint(20, self.map_height - 20)
            canvas.create_text(x, y, text="✨", font=("Arial", 8), fill="#f1c40f")
    
    def draw_paths(self, canvas):
        """Draw paths connecting unlocked regions"""
        unlocked_regions = self.player_data.data["unlocked_regions"]
        
        for i in range(len(self.regions) - 1):
            if unlocked_regions[i] and unlocked_regions[i + 1]:
                # Draw path to next region
                start_pos = self.regions[i]["position"]
                end_pos = self.regions[i + 1]["position"]
                
                canvas.create_line(
                    start_pos[0], start_pos[1],
                    end_pos[0], end_pos[1],
                    fill="#f39c12", width=3, dash=(5, 3)
                )
    
    def draw_regions(self, canvas):
        """Draw all regions on the map"""
        unlocked_regions = self.player_data.data["unlocked_regions"]
        player_level = self.player_data.get_level()
        
        for i, region in enumerate(self.regions):
            x, y = region["position"]
            size = region["size"]
            is_unlocked = unlocked_regions[i]
            
            if is_unlocked:
                # Unlocked region - full color
                self.draw_unlocked_region(canvas, region, x, y, size)
            elif player_level >= region["unlock_level"]:
                # Available to unlock - highlighted
                self.draw_available_region(canvas, region, x, y, size)
            else:
                # Locked region - grayed out
                self.draw_locked_region(canvas, region, x, y, size)
    
    def draw_unlocked_region(self, canvas, region, x, y, size):
        """Draw an unlocked region"""
        # Main region circle
        canvas.create_oval(
            x - size//2, y - size//2,
            x + size//2, y + size//2,
            fill=region["color"], outline="#ecf0f1", width=3
        )
        
        # Region icon
        canvas.create_text(
            x, y - 10, text=region["icon"], 
            font=("Arial", 16), fill="white"
        )
        
        # Region name
        canvas.create_text(
            x, y + size//2 + 15, text=region["name"],
            font=("Arial", 9, "bold"), fill="#ecf0f1"
        )
        
        # Glow effect
        canvas.create_oval(
            x - size//2 - 5, y - size//2 - 5,
            x + size//2 + 5, y + size//2 + 5,
            outline=region["color"], width=2, dash=(3, 3)
        )
    
    def draw_available_region(self, canvas, region, x, y, size):
        """Draw a region that's available to unlock"""
        # Pulsing outline effect
        canvas.create_oval(
            x - size//2, y - size//2,
            x + size//2, y + size//2,
            fill="#34495e", outline="#f39c12", width=4
        )
        
        # Question mark icon
        canvas.create_text(
            x, y - 5, text="❓", 
            font=("Arial", 14), fill="#f39c12"
        )
        
        # "UNLOCK" text
        canvas.create_text(
            x, y + size//2 + 15, text="UNLOCK NEXT!",
            font=("Arial", 8, "bold"), fill="#f39c12"
        )
    
    def draw_locked_region(self, canvas, region, x, y, size):
        """Draw a locked region"""
        # Grayed out circle
        canvas.create_oval(
            x - size//2, y - size//2,
            x + size//2, y + size//2,
            fill="#2c3e50", outline="#7f8c8d", width=2
        )
        
        # Lock icon
        canvas.create_text(
            x, y - 5, text="🔒", 
            font=("Arial", 12), fill="#7f8c8d"
        )
        
        # Level requirement
        canvas.create_text(
            x, y + size//2 + 15, text=f"Level {region['unlock_level']}",
            font=("Arial", 8), fill="#7f8c8d"
        )
    
    def draw_player_indicator(self, canvas):
        """Draw the player's current position indicator"""
        # Find the highest unlocked region
        unlocked_regions = self.player_data.data["unlocked_regions"]
        current_region_index = 0
        
        for i, unlocked in enumerate(unlocked_regions):
            if unlocked:
                current_region_index = i
        
        if current_region_index < len(self.regions):
            region = self.regions[current_region_index]
            x, y = region["position"]
            
            # Animated player indicator
            canvas.create_text(
                x + 25, y - 25, text="🧙‍♂️", 
                font=("Arial", 16), fill="white"
            )
            
            # Player label
            canvas.create_text(
                x + 25, y - 5, text="YOU",
                font=("Arial", 7, "bold"), fill="#f1c40f"
            )
    
    def get_region_info(self, region_index):
        """Get detailed information about a specific region"""
        if 0 <= region_index < len(self.regions):
            region = self.regions[region_index]
            is_unlocked = self.player_data.data["unlocked_regions"][region_index]
            
            return {
                "name": region["name"],
                "description": region["description"],
                "unlocked": is_unlocked,
                "unlock_level": region["unlock_level"],
                "icon": region["icon"]
            }
        
        return None