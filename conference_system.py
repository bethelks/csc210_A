# conference_system.py
# Base structure for Conference Management System


import os
import json
from datetime import datetime


class ConferenceSystem:
    def __init__(self):
        self.sessions = []
        self.attendees = []
        self.speakers = []
        self.favorites = {}  # {user_id: [session_ids]}
        self.uploads = {}    # {session_id: [file_info]}
        self.analytics = {
            'views': 0,
            'favorites': 0,
            'downloads': 0,
            'session_views': {}  # {session_id: view_count}
        }
        self.current_user = None
       
        # Create necessary directories
        self.create_directories()
        self.load_sample_data()
   
    def create_directories(self):
        """Create necessary directories for the system"""
        directories = ['uploads', 'reports', 'data']
        for directory in directories:
            if not os.path.exists(directory):
                os.makedirs(directory)
   
    def load_sample_data(self):
        """Load sample data for demonstration"""
        # Sample sessions
        self.sessions = [
            {
                'id': 1,
                'title': 'Python for Beginners',
                'speaker': 'Alice Johnson',
                'time': '10:00 AM',
                'room': 'Room A',
                'topics': ['programming', 'beginner', 'python'],
                'description': 'Learn Python fundamentals'
            },
            {
                'id': 2,
                'title': 'Advanced Data Structures',
                'speaker': 'Bob Smith',
                'time': '11:30 AM',
                'room': 'Room B',
                'topics': ['programming', 'advanced', 'data structures'],
                'description': 'Deep dive into data structures'
            },
            {
                'id': 3,
                'title': 'Machine Learning Basics',
                'speaker': 'Carol Davis',
                'time': '2:00 PM',
                'room': 'Room C',
                'topics': ['AI', 'machine learning', 'data science'],
                'description': 'Introduction to ML concepts'
            },
            {
                'id': 4,
                'title': 'Web Development with Django',
                'speaker': 'David Wilson',
                'time': '3:30 PM',
                'room': 'Room A',
                'topics': ['web', 'django', 'python'],
                'description': 'Build web applications with Django'
            },
            {
                'id': 5,
                'title': 'Data Visualization',
                'speaker': 'Eva Brown',
                'time': '4:45 PM',
                'room': 'Room D',
                'topics': ['data', 'visualization', 'analytics'],
                'description': 'Create effective data visualizations'
            }
        ]
       
        # Sample attendees
        self.attendees = [
            {'id': 101, 'name': 'John Doe', 'interests': ['programming', 'python']},
            {'id': 102, 'name': 'Jane Smith', 'interests': ['data science', 'analytics']}
        ]
       
        # Sample speakers
        self.speakers = [
            {'id': 201, 'name': 'Alice Johnson', 'sessions': [1]},
            {'id': 202, 'name': 'Bob Smith', 'sessions': [2]}
        ]
   
    def save_data(self):
        """Save system data to files (for persistence)"""
        data = {
            'sessions': self.sessions,
            'favorites': self.favorites,
            'uploads': self.uploads,
            'analytics': self.analytics
        }
       
        with open('data/system_data.json', 'w') as f:
            json.dump(data, f, indent=2)
   
    def load_data(self):
        """Load system data from files"""
        try:
            with open('data/system_data.json', 'r') as f:
                data = json.load(f)
                self.favorites = data.get('favorites', {})
                self.uploads = data.get('uploads', {})
                self.analytics = data.get('analytics', self.analytics)
        except FileNotFoundError:
            print("No saved data found. Starting with sample data.")
   
    # Common utility methods
    def find_session_by_id(self, session_id):
        """Find a session by ID"""
        for session in self.sessions:
            if session['id'] == session_id:
                return session
        return None
   
    def validate_session_id(self, session_id):
        """Check if session ID exists"""
        return any(session['id'] == session_id for session in self.sessions)
   
    def get_user_favorites(self, user_id):
        """Get favorite sessions for a user"""
        return self.favorites.get(user_id, [])
   
    def display_session_details(self, session_id):
        """Display detailed information about a session"""
        session = self.find_session_by_id(session_id)
        if session:
            print(f"\n=== {session['title']} ===")
            print(f"Speaker: {session['speaker']}")
            print(f"Time: {session['time']} | Room: {session['room']}")
            print(f"Description: {session['description']}")
            print(f"Topics: {', '.join(session.get('topics', []))}")
           
            # Track view
            self.track_session_view(session_id)
           
            return True
        else:
            print("Session not found.")
            return False
   
    def track_session_view(self, session_id):
        """Track when a session is viewed"""
        self.analytics['views'] += 1
        if session_id in self.analytics['session_views']:
            self.analytics['session_views'][session_id] += 1
        else:
            self.analytics['session_views'][session_id] = 1
   
    # Placeholder methods for students to implement
    def display_all_sessions(self):
        """Student 1: Display all conference sessions"""
        print("=== Session Browser Feature ===")
        print("This feature will be implemented by Student 1")
        # TODO: Student 1 will implement this
   
    def upload_presentation(self, session_id, file_path):
        """Student 2: Upload presentation slides"""
        print("=== File Upload Feature ===")
        print("This feature will be implemented by Student 2")
        # TODO: Student 2 will implement this
        return "Upload feature not yet implemented"
   
    def get_recommendations(self, user_id):
        """Student 3: Get session recommendations"""
        print("=== Session Recommendations Feature ===")
        print("This feature will be implemented by Student 3")
        # TODO: Student 3 will implement this
        return []
   
    def show_admin_dashboard(self):
        """Student 4: Display admin dashboard"""
        print("=== Admin Dashboard Feature ===")
        print("This feature will be implemented by Student 4")
        # TODO: Student 4 will implement this
