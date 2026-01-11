# 🗺️ Desktop Adventure Map

Turn your daily computer usage into a mini RPG-style adventure! Complete tasks, earn XP, unlock new regions, and build productive habits in a fun, gamified way.

## 🎮 Features

### MVP (Current Version)
- **Adventure Map Visualization**: 5 unique regions to unlock as you progress
- **Daily Quests**: Complete productivity tasks to earn XP and rewards
- **Progression System**: Level up and unlock new map areas
- **Streak Tracking**: Build daily habits and maintain your adventure streak
- **Inventory System**: Collect badges, treasures, and milestone rewards

### Quest Types
- 📁 **File Organization** (+10 XP): Organize files on your desktop or folders
- 💻 **Work Session** (+15 XP): Complete focused work or study sessions  
- 📚 **Learning Quest** (+20 XP): Learn something new or practice skills

### Map Regions
1. 🏘️ **Starting Village** - Your humble beginnings (Level 1)
2. 🌲 **Mystic Forest** - Ancient trees hold secrets (Level 2)
3. 💎 **Crystal Caves** - Glittering depths await (Level 4)
4. ⛩️ **Sky Temple** - Floating among clouds (Level 6)
5. 🐉 **Dragon's Peak** - The ultimate challenge (Level 8)

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- No external dependencies required (uses Tkinter)

### Installation & Running
1. Clone or download this project
2. Navigate to the project directory
3. Run the application:
   ```bash
   python main.py
   ```

### First Time Setup
- The app creates an `adventure_save.json` file to track your progress
- Start by completing your first quest to begin your adventure!
- Your progress is automatically saved after each quest completion

## 🎯 How to Play

1. **Complete Daily Quests**: Click quest buttons to mark tasks as complete
2. **Earn XP & Level Up**: Each quest gives XP, level up to unlock new regions
3. **Explore the Map**: Watch new areas unlock as you progress
4. **Build Streaks**: Complete quests daily to maintain your adventure streak
5. **Collect Rewards**: Earn badges, treasures, and milestone achievements

## 📊 Progression System

- **XP Formula**: Level = floor(sqrt(XP/10)) + 1
- **Region Unlocking**: New regions unlock every 2 levels
- **Streak Rewards**: Weekly streak badges (every 7 days)
- **Milestone Rewards**: Special badges at 10, 25, 50, 100+ quests
- **Random Treasures**: 10% chance for bonus rewards on quest completion

## 🔧 Technical Details

### File Structure
- `main.py` - Main application and UI
- `player_data.py` - Save/load system and player progress
- `quest_manager.py` - Quest logic and reward system
- `adventure_map.py` - Map visualization and region management
- `adventure_save.json` - Your progress data (auto-created)

### Customization
The code is designed to be easily extensible:
- Add new quest types in `quest_manager.py`
- Create new regions in `adventure_map.py`
- Modify XP/level formulas in `player_data.py`
- Customize UI colors and layout in `main.py`

## 🚧 Future Enhancements

### Planned Features
- **Random Daily Events**: Special challenges and bonus opportunities
- **Achievement System**: Unlock titles and special rewards
- **Quest Chains**: Multi-step adventures with story elements
- **Seasonal Events**: Holiday-themed quests and decorations
- **Export Progress**: Share your adventure map with friends

### Advanced Ideas
- **Pygame Integration**: Smoother animations and better graphics
- **Sound Effects**: Audio feedback for quest completion
- **Custom Quest Creator**: Let users define their own productivity tasks
- **Cloud Sync**: Backup progress across multiple devices
- **Team Adventures**: Collaborative quests with friends or colleagues

## 🤝 Contributing

This is a fun, educational project perfect for:
- Adding new quest types or regions
- Improving the UI/UX design
- Adding animations or visual effects
- Creating themed content packs
- Building advanced features

## 📝 License

This project is open source and available under the MIT License.

## 🎉 Have Fun!

Remember, this is about building positive habits while having fun. Complete quests at your own pace and enjoy watching your adventure map grow!

---

*Happy adventuring! 🧙‍♂️✨*