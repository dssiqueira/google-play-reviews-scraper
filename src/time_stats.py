#!/usr/bin/env python3
"""
Sistema simples para salvar estatísticas de tempo economizado
"""

import json
import os
from datetime import datetime

class TimeStats:
    """Manages time saved statistics"""
    
    def __init__(self, stats_file="time_stats.json"):
        self.stats_file = stats_file
        self.stats = self.load_stats()
    
    def load_stats(self):
        """Loads statistics from file"""
        default_stats = {
            "total_reviews_collected": 0,
            "total_time_saved_seconds": 0,
            "total_sessions": 0,
            "first_use": None,
            "last_use": None
        }
        
        try:
            if os.path.exists(self.stats_file):
                with open(self.stats_file, 'r', encoding='utf-8') as f:
                    loaded_stats = json.load(f)
                    # Merge com defaults para garantir compatibilidade
                    default_stats.update(loaded_stats)
            return default_stats
        except Exception as e:
            print(f"Erro ao carregar estatísticas: {e}")
            return default_stats
    
    def save_stats(self):
        """Saves statistics to file"""
        try:
            with open(self.stats_file, 'w', encoding='utf-8') as f:
                json.dump(self.stats, f, ensure_ascii=False, indent=2, default=str)
        except Exception as e:
            print(f"Erro ao salvar estatísticas: {e}")
    
    def add_session(self, reviews_count):
        """Adds a new session and returns time saved"""
        if reviews_count <= 0:
            return 0
        
        # Calculate time saved (30 seconds per review)
        time_saved = reviews_count * 30
        
        # Update statistics
        self.stats["total_reviews_collected"] += reviews_count
        self.stats["total_time_saved_seconds"] += time_saved
        self.stats["total_sessions"] += 1
        
        # Update dates
        now = datetime.now().isoformat()
        if not self.stats["first_use"]:
            self.stats["first_use"] = now
        self.stats["last_use"] = now
        
        # Save to file
        self.save_stats()
        
        return time_saved
    
    def get_total_time_saved(self):
        """Retorna tempo total economizado em segundos"""
        return self.stats["total_time_saved_seconds"]
    
    def get_total_reviews(self):
        """Retorna total de reviews coletadas"""
        return self.stats["total_reviews_collected"]
    
    def get_total_sessions(self):
        """Returns total sessions"""
        return self.stats["total_sessions"]
    
    def format_time(self, seconds):
        """Formats time in readable format"""
        if seconds < 60:
            return f"{seconds}s"
        elif seconds < 3600:
            minutes = seconds // 60
            remaining_seconds = seconds % 60
            if remaining_seconds > 0:
                return f"{minutes}min {remaining_seconds}s"
            else:
                return f"{minutes}min"
        else:
            hours = seconds // 3600
            remaining_minutes = (seconds % 3600) // 60
            if remaining_minutes > 0:
                return f"{hours}h {remaining_minutes}min"
            else:
                return f"{hours}h"
    
    def get_formatted_total_time(self):
        """Retorna tempo total formatado"""
        return self.format_time(self.get_total_time_saved())
    
    def get_stats_summary(self):
        """Returns statistics summary"""
        return {
            "total_reviews": self.get_total_reviews(),
            "total_time_saved_seconds": self.get_total_time_saved(),
            "total_time_saved_formatted": self.get_formatted_total_time(),
            "total_sessions": self.get_total_sessions(),
            "first_use": self.stats["first_use"],
            "last_use": self.stats["last_use"]
        }

# Global instance
time_stats = TimeStats()