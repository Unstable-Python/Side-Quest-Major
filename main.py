#!/usr/bin/env python3
"""
Desktop Adventure Map - MVP
A gamified productivity tracker that turns daily tasks into an RPG-style adventure.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime, date
from adventure_map import AdventureMap
from quest_manager import QuestManager
from player_data import PlayerData

class DesktopAdventureApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Desktop Adventure Map")
        self.root.geometry("800x600")
        self.root.configure(bg="#2c3e50")
        
        # Initialize game components
        self.player_data = PlayerData()
        self.quest_manager = QuestManager(self.player_data)
        self.adventure_map = AdventureMap(self.player_data)
        
        self.setup_ui()
        self.update_display()
    
    def setup_ui(self):
        """Create the main UI layout"""
        # Main container
        main_frame = tk.Frame(self.root, bg="#2c3e50")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title
        title_label = tk.Label(
            main_frame, 
            text="🗺️ Desktop Adventure Map", 
            font=("Arial", 20, "bold"),
            fg="#ecf0f1", 
            bg="#2c3e50"
        )
        title_label.pack(pady=(0, 20))
        
        # Top stats panel
        self.create_stats_panel(main_frame)
        
        # Map display
        self.create_map_display(main_frame)
        
        # Quest panel
        self.create_quest_panel(main_frame)
    
    def create_stats_panel(self, parent):
        """Create the player stats display"""
        stats_frame = tk.Frame(parent, bg="#34495e", relief=tk.RAISED, bd=2)
        stats_frame.pack(fill=tk.X, pady=(0, 10))
        
        # XP and Level
        self.xp_label = tk.Label(
            stats_frame, 
            text="XP: 0 | Level: 1", 
            font=("Arial", 12, "bold"),
            fg="#f39c12", 
            bg="#34495e"
        )
        self.xp_label.pack(side=tk.LEFT, padx=10, pady=5)
        
        # Streak
        self.streak_label = tk.Label(
            stats_frame, 
            text="Streak: 0 days", 
            font=("Arial", 12),
            fg="#e74c3c", 
            bg="#34495e"
        )
        self.streak_label.pack(side=tk.LEFT, padx=10, pady=5)
        
        # Unlocked regions
        self.regions_label = tk.Label(
            stats_frame, 
            text="Regions: 1/5", 
            font=("Arial", 12),
            fg="#27ae60", 
            bg="#34495e"
        )
        self.regions_label.pack(side=tk.LEFT, padx=10, pady=5)
    
    def create_map_display(self, parent):
        """Create the adventure map visualization"""
        map_frame = tk.Frame(parent, bg="#34495e", relief=tk.RAISED, bd=2)
        map_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        map_title = tk.Label(
            map_frame, 
            text="🌍 Adventure Map", 
            font=("Arial", 14, "bold"),
            fg="#ecf0f1", 
            bg="#34495e"
        )
        map_title.pack(pady=5)
        
        # Map canvas
        self.map_canvas = tk.Canvas(
            map_frame, 
            width=600, 
            height=300, 
            bg="#1a252f",
            highlightthickness=0
        )
        self.map_canvas.pack(pady=10)
        
        # Draw initial map
        self.adventure_map.draw_map(self.map_canvas)
    
    def create_quest_panel(self, parent):
        """Create the quest/task panel"""
        quest_frame = tk.Frame(parent, bg="#34495e", relief=tk.RAISED, bd=2)
        quest_frame.pack(fill=tk.X)
        
        quest_title = tk.Label(
            quest_frame, 
            text="⚔️ Daily Quests", 
            font=("Arial", 14, "bold"),
            fg="#ecf0f1", 
            bg="#34495e"
        )
        quest_title.pack(pady=5)
        
        # Quest buttons
        button_frame = tk.Frame(quest_frame, bg="#34495e")
        button_frame.pack(pady=10)
        
        # File organization quest
        self.file_quest_btn = tk.Button(
            button_frame,
            text="📁 Organize Files (+10 XP)",
            command=self.complete_file_quest,
            bg="#3498db",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=20,
            pady=5
        )
        self.file_quest_btn.pack(side=tk.LEFT, padx=5)
        
        # Work session quest
        self.work_quest_btn = tk.Button(
            button_frame,
            text="💻 Complete Work Session (+15 XP)",
            command=self.complete_work_quest,
            bg="#e67e22",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=20,
            pady=5
        )
        self.work_quest_btn.pack(side=tk.LEFT, padx=5)
        
        # Learning quest
        self.learn_quest_btn = tk.Button(
            button_frame,
            text="📚 Learn Something New (+20 XP)",
            command=self.complete_learn_quest,
            bg="#9b59b6",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=20,
            pady=5
        )
        self.learn_quest_btn.pack(side=tk.LEFT, padx=5)
    
    def complete_file_quest(self):
        """Handle file organization quest completion"""
        if self.quest_manager.complete_quest("file_organization"):
            self.show_reward_message("File Quest Complete!", "You organized your files and earned 10 XP! 📁✨")
            self.update_display()
    
    def complete_work_quest(self):
        """Handle work session quest completion"""
        if self.quest_manager.complete_quest("work_session"):
            self.show_reward_message("Work Session Complete!", "You completed a productive work session and earned 15 XP! 💻⚡")
            self.update_display()
    
    def complete_learn_quest(self):
        """Handle learning quest completion"""
        if self.quest_manager.complete_quest("learning"):
            self.show_reward_message("Learning Quest Complete!", "You expanded your knowledge and earned 20 XP! 📚🧠")
            self.update_display()
    
    def show_reward_message(self, title, message):
        """Show a reward popup message"""
        messagebox.showinfo(title, message)
    
    def update_display(self):
        """Update all UI elements with current data"""
        # Update stats
        level = self.player_data.get_level()
        xp = self.player_data.data["xp"]
        streak = self.player_data.data["streak"]
        unlocked_regions = len([r for r in self.player_data.data["unlocked_regions"] if r])
        
        self.xp_label.config(text=f"XP: {xp} | Level: {level}")
        self.streak_label.config(text=f"Streak: {streak} days")
        self.regions_label.config(text=f"Regions: {unlocked_regions}/5")
        
        # Update map
        self.map_canvas.delete("all")
        self.adventure_map.draw_map(self.map_canvas)
        
        # Update quest buttons based on completion status
        today = date.today().isoformat()
        completed_today = self.player_data.data["daily_quests"].get(today, [])
        
        self.file_quest_btn.config(
            state=tk.DISABLED if "file_organization" in completed_today else tk.NORMAL
        )
        self.work_quest_btn.config(
            state=tk.DISABLED if "work_session" in completed_today else tk.NORMAL
        )
        self.learn_quest_btn.config(
            state=tk.DISABLED if "learning" in completed_today else tk.NORMAL
        )
    
    def run(self):
        """Start the application"""
        self.root.mainloop()

if __name__ == "__main__":
    app = DesktopAdventureApp()
    app.run()