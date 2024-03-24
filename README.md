**Flask Application Design**

**HTML Files**

- **index.html**:
    - The main page of the application.
    - Contains the necessary HTML elements for user interaction, such as a form for creating a user profile and buttons for communication tools.
- **profile.html**:
    - The page where users can create and edit their profiles.
    - Contains fields for personal information, preferences, and interests.
- **matching.html**:
    - The page where users can search for potential peer supporters.
    - Displays a list of user profiles based on matching criteria.
- **chat.html**:
    - The page where users can communicate with their matched peers.
    - Includes a chat interface with real-time messaging capabilities.

**Routes**

- **/**: This is the root route that maps to the index.html file.
- **profile**: The route for creating and editing user profiles. Receives user input and stores it in a database.
- **matching**: The route for searching for potential peer supporters. Queries the database based on user preferences and interests.
- **chat**: The route for establishing communication between matched peers. Handles real-time messaging.
- **resources**: The route for accessing the resource library. Provides a list of available mental health resources.
- **forum**: The route for topic-specific forums. Allows users to share experiences, ask questions, and receive support from the community.
- **emergency**: The route for accessing emergency mental health services or contacting a professional counselor.
- **feedback**: The route for collecting user feedback and suggestions.
- **privacy**: The route for displaying the privacy policy and obtaining user consent for data usage.