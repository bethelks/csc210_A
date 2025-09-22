# main.py
# Main program that integrates all features

from conference_system import ConferenceSystem

def display_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("      CONFERENCE MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Browse All Sessions")
    print("2. View Session Details")
    print("3. Add Session to Favorites")
    print("4. Upload Presentation (Speaker)")
    print("5. Get Session Recommendations")
    print("6. Admin Dashboard")
    print("7. Exit")
    print("-"*50)

def login_user(system):
    """Simple user login simulation"""
    print("\n=== User Login ===")
    print("Available users:")
    for i, attendee in enumerate(system.attendees, 1):
        print(f"{i}. {attendee['name']} (Attendee)")
    
    for i, speaker in enumerate(system.speakers, len(system.attendees) + 1):
        print(f"{i}. {speaker['name']} (Speaker)")
    
    try:
        choice = int(input("\nSelect user (number): ")) - 1
        all_users = system.attendees + system.speakers
        if 0 <= choice < len(all_users):
            system.current_user = all_users[choice]
            print(f"Welcome, {system.current_user['name']}!")
            return True
        else:
            print("Invalid selection.")
            return False
    except ValueError:
        print("Please enter a valid number.")
        return False

def browse_sessions(system):
    """Browse all sessions"""
    print("\n=== Browse Sessions ===")
    system.display_all_sessions()  # This will call Student 1's implementation

def view_session_details(system):
    """View details of a specific session"""
    print("\n=== Session Details ===")
    try:
        session_id = int(input("Enter session ID: "))
        system.display_session_details(session_id)
    except ValueError:
        print("Please enter a valid session ID.")

def add_to_favorites(system):
    """Add a session to user's favorites"""
    if not system.current_user:
        print("Please login first.")
        return
    
    print("\n=== Add to Favorites ===")
    try:
        session_id = int(input("Enter session ID to add to favorites: "))
        if system.validate_session_id(session_id):
            user_id = system.current_user['id']
            if user_id not in system.favorites:
                system.favorites[user_id] = []
            
            if session_id not in system.favorites[user_id]:
                system.favorites[user_id].append(session_id)
                system.analytics['favorites'] += 1
                print(f"Session {session_id} added to favorites!")
            else:
                print("Session already in favorites.")
        else:
            print("Invalid session ID.")
    except ValueError:
        print("Please enter a valid session ID.")

def upload_presentation(system):
    """Upload presentation slides"""
    if not system.current_user:
        print("Please login first.")
        return
    
    print("\n=== Upload Presentation ===")
    try:
        session_id = int(input("Enter session ID: "))
        file_path = input("Enter file path: ")
        result = system.upload_presentation(session_id, file_path)
        print(result)
    except ValueError:
        print("Please enter a valid session ID.")

def show_recommendations(system):
    """Show session recommendations"""
    if not system.current_user:
        print("Please login first.")
        return
    
    print("\n=== Session Recommendations ===")
    recommendations = system.get_recommendations(system.current_user['id'])
    if recommendations:
        print("Recommended sessions for you:")
        for session in recommendations:
            print(f"- {session['title']} (ID: {session['id']})")
    else:
        print("No recommendations available yet.")

def admin_dashboard(system):
    """Show admin dashboard"""
    print("\n=== Admin Dashboard ===")
    system.show_admin_dashboard()

def main():
    """Main program loop"""
    system = ConferenceSystem()
    system.load_data()
    
    print("Welcome to the Conference Management System!")
    
    # Simple login
    if not login_user(system):
        return
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            browse_sessions(system)
        elif choice == '2':
            view_session_details(system)
        elif choice == '3':
            add_to_favorites(system)
        elif choice == '4':
            upload_presentation(system)
        elif choice == '5':
            show_recommendations(system)
        elif choice == '6':
            admin_dashboard(system)
        elif choice == '7':
            system.save_data()
            print("Thank you for using the Conference Management System!")
            break
        else:
            print("Invalid choice. Please try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()