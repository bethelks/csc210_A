
from conference_system import ConferenceSystem

def add_to_favorites(system, user_id, session_id):
    if user_id not in system.favorites:
        system.favorites[user_id] = []

    if session_id not in system.favorites[user_id]:
        system.favorites[user_id].append(session_id)
        system.analytics['favorites'] += 1
        return f"Session {session_id} added to favorites"
    else:
        return "session already in favorites"
    
def get_recommendations(system, user_id, sessions):
    if user_id not in system.favorites or not system.favorites[user_id]:
        # if no favorites, return most popular sessions
        return get_popular_sessions(system, sessions, 3)
    
    # Extract topics from favorite sessions
    favorite_topics = set()
    for session_id in system.favorites[user_id]:
        session = next((s for s in sessions if s['id'] == session_id), None)
        if session and 'topics' in session:
            favorite_topics.update(session['topics'])

    # Find sessions with similar topics
    recommendations = []
    for session in sessions:
        if session['id'] in system.favorites[user_id]:
            continue  # skip already favorited sessions

        if 'topics' in session and favorite_topics.intersection(session['topics']):
            # calculate relevance score (number of matching topics)
            matching_topics = favorite_topics.intersection(session['topics'])
            recommendations.append((session, len(matching_topics)))

    # Sort by relevance score
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return [rec[0] for rec in recommendations[:3]]

def get_popular_sessions(system, sessions, count):
    # simplified popularity based on order
    return sessions[:count]  # just return first few as sample

# SAMPLE USAGE
if __name__ == "__main__":
    system = ConferenceSystem()
    # Add sample sessions
    system.sessions = [
        {'id': 1, 'title': 'Python Basics', 'topics': ['programming', 'beginner']},
        {'id': 2, 'title': 'Data Science', 'topics': ['data', 'analytics']},
        {'id': 3, 'title': 'Advanced AI', 'topics': ['AI', 'machine learning']},
        {'id': 4, 'title': 'Web Development', 'topics': ['web', 'programming']}
    ]

    add_to_favorites(system, 101, 1)
    recs = get_recommendations(system, 101, system.sessions)
    print("Recommended sessions:")
    for session in recs:
        print(f"- {session['title']}")







































